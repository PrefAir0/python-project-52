from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from statuses.models import Status
from tasks.models import Task

class TaskCRUDTestCase(TestCase):
    def setUp(self):
        self.author = User.objects.create_user(username='author', password='password123')
        self.non_author = User.objects.create_user(username='non_author', password='password123')

        self.status = Status.objects.create(name='В работе')

        self.task = Task.objects.create(
            name='Первая задача',
            description='Описание',
            status=self.status,
            author=self.author
        )

    def test_task_list_and_detail(self):
        self.client.login(username='author', password='password123')

        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Первая задача')
        
        response = self.client.get(reverse('tasks:view', kwargs={'pk': self.task.id}))
        self.assertEqual(response.status_code, 200)

    def test_create_task(self):
        self.client.login(username='author', password='password123')
        task_data = {
            'name': 'Вторая задача',
            'description': 'Сделать CRUD',
            'status': self.status.id,
            'executor': self.author.id
        }
        response = self.client.post(reverse('tasks:create'), data=task_data)
        self.assertRedirects(response, reverse('tasks:index'))
        self.assertTrue(Task.objects.filter(name='Вторая задача').exists())

    def test_delete_task_by_author(self):
        self.client.login(username='author', password='password123')
        response = self.client.post(reverse('tasks:delete', kwargs={'pk': self.task.id}))
        self.assertRedirects(response, reverse('tasks:index'))
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_delete_task_by_non_author(self):
        self.client.login(username='non_author', password='password123')
        response = self.client.post(reverse('tasks:delete', kwargs={'pk': self.task.id}))

        self.assertRedirects(response, reverse('tasks:index'))
        self.assertTrue(Task.objects.filter(id=self.task.id).exists())

    def test_unauthorized_redirect(self):
        response = self.client.get(reverse('tasks:index'))
        self.assertEqual(response.status_code, 302)

    def test_filter_tasks_by_status(self):
        self.client.login(username='author', password='password123')

        status2 = Status.objects.create(name='Завершен')
        Task.objects.create(
            name='Вторая задача',
            status=status2,
            author=self.author
        )

        response = self.client.get(reverse('tasks:index'), data={'status': self.status.id})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Первая задача')
        self.assertNotContains(response, 'Вторая задача')

    def test_filter_self_tasks(self):
        self.client.login(username='author', password='password123')
        
        Task.objects.create(
            name='Чужая задача',
            status=self.status,
            author=self.non_author
        )

        response = self.client.get(reverse('tasks:index'), data={'self_tasks': 'on'})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Первая задача')
        self.assertNotContains(response, 'Чужая задача')
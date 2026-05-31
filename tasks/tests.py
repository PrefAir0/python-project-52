from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from tasks.models import Task
from statuses.models import Status
from labels.models import Label


class TaskCRUDTestCase(TestCase):
    def setUp(self):

        User = get_user_model()
        self.author = User.objects.create_user(
            username='author',
            password='password123'
        )
        self.executor = User.objects.create_user(
            username='executor',
            password='password123'
        )
        self.another_user = User.objects.create_user(
            username='stranger',
            password='password123'
        )

        self.status = Status.objects.create(name='New')
        self.label = Label.objects.create(name='Bug')

        self.task_data = {
            'name': 'Test Task',
            'description': 'Task description',
            'status': self.status.id,
            'executor': self.executor.id,
            'labels': [self.label.id]
        }

        self.client.login(username='author', password='password123')

    def test_task_list_and_detail(self):
        
        response = self.client.get(reverse_lazy('tasks:index'))
        self.assertEqual(response.status_code, 200)

        
        task = Task.objects.create(
            name='View Task',
            author=self.author,
            status=self.status
        )
        response = self.client.get(reverse_lazy('tasks:detail', kwargs={'pk': task.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Task')

    def test_create_task(self):
        
        response = self.client.post(reverse_lazy('tasks:create'), data=self.task_data)
        
        
        self.assertRedirects(response, reverse_lazy('tasks:index'))
        
        
        task = Task.objects.filter(name='Test Task').first()
        self.assertIsNotNone(task)
        self.assertEqual(task.author, self.author)
        self.assertEqual(task.executor, self.executor)

    def test_update_task(self):
        task = Task.objects.create(
            name='Old Name',
            author=self.author,
            status=self.status
        )
        
        updated_data = self.task_data.copy()
        updated_data['name'] = 'Updated Name'

        response = self.client.post(
            reverse_lazy('tasks:update', kwargs={'pk': task.id}),
            data=updated_data
        )
        self.assertRedirects(response, reverse_lazy('tasks:index'))

        task.refresh_from_db()
        self.assertEqual(task.name, 'Updated Name')

    def test_delete_task_by_author(self):
        task = Task.objects.create(
            name='To Be Deleted',
            author=self.author,
            status=self.status
        )

        response = self.client.post(reverse_lazy('tasks:delete', kwargs={'pk': task.id}))
        self.assertRedirects(response, reverse_lazy('tasks:index'))
        

        self.assertFalse(Task.objects.filter(id=task.id).exists())

    def test_delete_task_by_stranger_fails(self):
        task = Task.objects.create(
            name='Protected Task',
            author=self.author,
            status=self.status
        )

        self.client.login(username='stranger', password='password123')

        response = self.client.post(reverse_lazy('tasks:delete', kwargs={'pk': task.id}))
        self.assertRedirects(response, reverse_lazy('tasks:index'))
        
        
        self.assertTrue(Task.objects.filter(id=task.id).exists())
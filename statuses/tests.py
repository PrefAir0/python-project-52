from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from statuses.models import Status

class StatusCRUDTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password321')
        self.client.login(username='testuser', password='password321')
        self.status = Status.objects.create(name='Новый')

    def test_statuses_list_view(self):
        response = self.client.get(reverse('statuses:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/index.html')
        self.assertContains(response, 'Новый')

    def test_create_status(self):
        status_data = {'name': 'В работе'}
        response = self.client.post(reverse('statuses:create'), data=status_data)
        self.assertRedirects(response, reverse('statuses:index'))
        self.assertTrue(Status.objects.filter(name='В работе').exists())

    def test_update_status(self):
        status_data = {'name': 'На тестировании'}
        response = self.client.post(
            reverse('statuses:update', kwargs={'pk': self.status.id}),
            data=status_data
        )
        self.assertRedirects(response, reverse('statuses:index'))

        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'На тестировании')

    def test_delete_status(self):
        response = self.client.post(reverse('statuses:delete', kwargs={'pk': self.status.id}))
        self.assertRedirects(response, reverse('statuses:index'))

        self.assertFalse(Status.objects.filter(id=self.status.id).exists())

    def test_statuses_view_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse('statuses:index'))

        self.assertEqual(response.status_code, 302)
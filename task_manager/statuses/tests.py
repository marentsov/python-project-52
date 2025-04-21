from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.utils.translation import gettext as _

from django.urls import reverse

from task_manager.statuses.models import Status


class StatusTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="user1",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_create_status(self):

        test_data = {'name': 'status1'}
        response = self.client.post(reverse('statuses:create'), test_data)

        self.assertRedirects(response, reverse('statuses:statuses'))

        self.assertTrue(Status.objects.filter(name='status1').exists())

    def test_update_statuses(self):

        test_data = {'name': 'status1'}
        self.client.post(reverse('statuses:create'), test_data)

        status = Status.objects.get(name=test_data['name'])
        update_data = {'name': 'status1upd'}
        response = self.client.post(reverse('statuses:update', args=[status.id]), update_data)

        self.assertRedirects(response, reverse('statuses:statuses'))

        self.assertTrue(Status.objects.filter(name='status1upd').exists())


    def test_delete_statuses(self):

        test_data = {'name': 'status1'}
        self.client.post(reverse('statuses:create'), test_data)

        status = Status.objects.get(name=test_data['name'])

        self.client.post(reverse('statuses:delete', args=[status.id]))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(name=test_data["name"])








# Create your tests here.

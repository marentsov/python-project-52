from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label


class LabelTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="user1",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_create_label(self):

        test_data = {'name': 'label1'}
        response = self.client.post(reverse('labels:create'), test_data)

        self.assertRedirects(response, reverse('labels:labels'))

        self.assertTrue(Label.objects.filter(name='label1').exists())

    def test_update_labels(self):

        test_data = {'name': 'status1'}
        self.client.post(reverse('labels:create'), test_data)

        label = Label.objects.get(name=test_data['name'])
        update_data = {'name': 'label1upd'}
        response = self.client.post(reverse(
            'labels:update', args=[label.id]), update_data)

        self.assertRedirects(response, reverse('labels:labels'))

        self.assertTrue(Label.objects.filter(name='label1upd').exists())

    def test_delete_labels(self):

        test_data = {'name': 'label1'}
        self.client.post(reverse('labels:create'), test_data)

        label = Label.objects.get(name=test_data['name'])

        self.client.post(reverse('labels:delete', args=[label.id]))
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(name=test_data["name"])


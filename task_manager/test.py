from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TitlesTestNotAuthorized(TestCase):

    def test_user_login_title(self):

        response = self.client.get(reverse('login'))
        title = _('Task manager - authorization')
        self.assertEqual(response.context['title'], title)

    def test_user_registration_title(self):

        response = self.client.get(reverse('users:create'))
        title = _('Task manager - registration')
        self.assertEqual(response.context['title'], title)


class TitlesTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user1 = User.objects.create_user(
            username='user1',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='password123'
        )
        self.client.login(
            username='user1',
            password='password123'
        )
        self.status1 = Status.objects.create(name='status1')
        self.status2 = Status.objects.create(name='status2')

        self.label1 = Label.objects.create(name='label1')
        self.label2 = Label.objects.create(name='label2')
        self.label3 = Label.objects.create(name='label3')

        self.task1 = Task.objects.create(
            name='task1',
            creator=self.user1,
            status=self.status1,
            executor=self.user1,
        )
        self.task1.labels.add(self.label1, self.label2)

        self.task2 = Task.objects.create(
            name='task2',
            creator=self.user2,
            status=self.status2,
            executor=self.user2,
        )
        self.task2.labels.add(self.label3)

        self.task3 = Task.objects.create(
            name='task3',
            creator=self.user1,
            status=self.status2,
            executor=self.user2,
        )
        self.task3.labels.add(self.label2, self.label3)

    def test_user_update_title(self):

        response = self.client.get(reverse('users:update', args=[1]))
        title = _('Task manager - update user info')
        self.assertEqual(response.context['title'], title)

    def test_user_delete_title(self):

        response = self.client.get(reverse('users:delete', args=[1]))
        title = _('Task manager - delete user')
        self.assertEqual(response.context['title'], title)

    def test_task_create_title(self):

        response = self.client.get(reverse('tasks:create'))
        title = _('Task manager - create task')
        self.assertEqual(response.context['title'], title)

    def test_task_update_title(self):

        response = self.client.get(reverse('tasks:update', args=[1]))
        title = _('Task manager - update task')
        self.assertEqual(response.context['title'], title)

    def test_task_delete_title(self):

        response = self.client.get(reverse('tasks:delete', args=[1]))
        title = _('Task manager - delete task')
        self.assertEqual(response.context['title'], title)

    def test_status_create_title(self):

        response = self.client.get(reverse('statuses:create'))
        title = _('Task manager - create status')
        self.assertEqual(response.context['title'], title)

    def test_status_update_title(self):

        response = self.client.get(reverse('statuses:update', args=[1]))
        title = _('Task manager - update status info')
        self.assertEqual(response.context['title'], title)

    def test_status_delete_title(self):

        response = self.client.get(reverse('statuses:delete', args=[1]))
        title = _('Task manager - delete status')
        self.assertEqual(response.context['title'], title)

    def test_label_create_title(self):

        response = self.client.get(reverse('labels:create'))
        title = _('Task manager - create label')
        self.assertEqual(response.context['title'], title)

    def test_label_update_title(self):

        response = self.client.get(reverse('labels:update', args=[1]))
        title = _('Task manager - update label info')
        self.assertEqual(response.context['title'], title)

    def test_label_delete_title(self):

        response = self.client.get(reverse('labels:delete', args=[1]))
        title = _('Task manager - delete label')
        self.assertEqual(response.context['title'], title)








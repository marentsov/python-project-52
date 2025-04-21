from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskTest(TestCase):
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


    def test_filter_task_my_tasks(self):
        test_data = {
            'my_tasks': 'on'
        }
        response = self.client.get(reverse('tasks:tasks'), test_data)
        self.assertContains(response, self.task1.name)
        self.assertContains(response, self.task3.name)
        self.assertNotContains(response, self.task2.name)



    def test_filter_task_labels(self):
        test_data = {
            'labels': self.label1.pk
        }
        response = self.client.get(reverse('tasks:tasks'), test_data)
        self.assertContains(response, self.task1.name)
        self.assertNotContains(response, self.task2.name)
        self.assertNotContains(response, self.task3.name)


    def test_filter_task_statuses(self):
        test_data = {
            'status': self.status1.pk
        }
        response = self.client.get(reverse('tasks:tasks'), test_data)
        self.assertContains(response, self.task1.name)
        self.assertNotContains(response, self.task2.name)
        self.assertNotContains(response, self.task3.name)


    def test_filter_task_executor(self):
        test_data = {
            'executor': self.user2.pk
        }
        response = self.client.get(reverse('tasks:tasks'), test_data)
        self.assertContains(response, self.task2.name)
        self.assertContains(response, self.task3.name)
        self.assertNotContains(response, self.task1.name)


    def test_list_of_tasks(self):

        response = self.client.get(reverse('tasks:tasks'))

        self.assertContains(response, self.task2.name)
        self.assertContains(response, self.task3.name)
        self.assertContains(response, self.task1.name)

        title = _('Task manager - tasks')
        self.assertEqual(response.context['title'], title)


    def test_task_update(self):

        test_data = {
            "name": "task1upd",
            "description": "description1",
            "status": self.status1.pk,
        }

        response = self.client.post(
            reverse('tasks:update', args=[self.task1.pk]), test_data
        )

        self.assertRedirects(response, reverse('tasks:tasks'))

        updated_task = Task.objects.get(pk=self.task1.pk)
        self.assertEqual(updated_task.name, test_data['name'])
        self.assertEqual(updated_task.description, test_data['description'])


    def test_task_delete(self):

        response = self.client.post(reverse('tasks:delete', args=[self.task3.pk]))

        self.assertRedirects(response, reverse('tasks:tasks'))

        response = self.client.get(reverse('tasks:tasks'))

        self.assertContains(response, self.task2.name)
        self.assertNotContains(response, self.task3.name)
        self.assertContains(response, self.task1.name)







# Create your tests here.

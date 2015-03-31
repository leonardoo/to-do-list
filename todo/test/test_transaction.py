import unittest
from django.core.urlresolvers import reverse

from django.test import Client
from django.test.testcases import TransactionTestCase
from django.shortcuts import resolve_url

from todo.models import Todo

class TransactionTest(TransactionTestCase):

    def setUp(self):
        self.client = Client()

    def test_create(self):
        response = self.client.post(resolve_url("add"), {"activity":"esto es un texto"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")
        self.assertTemplateUsed(response.context['list'].count(),1)


    def test_models_str(self):
        todo = Todo()
        todo.activity = "hola"
        todo.save()
        self.assertEqual(str(todo),"{} - {}".format(str(todo.pk), "hola"))

    @unittest.expectedFailure
    def test_models_str_2(self):
        todo = Todo()
        todo.activity = "hola"
        todo.save()
        self.assertEqual(str(todo),"{} {}".format(str(todo.pk), "hola"))


class TransactionTest2(TransactionTestCase):

    def setUp(self):
        self.client = Client()
        self.todo = Todo()
        self.todo.activity = "hola"
        self.todo.save()

    def test_edit_view(self):
        response = self.client.get(reverse("edit", kwargs={"pk":self.todo.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"add.html")

    def test_edit(self):
        response = self.client.post(reverse("edit",kwargs={"pk":self.todo.pk}),
                                    {"activity":"actividad"},
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")
        self.assertEqual(response.context['list'].count(),1)
        self.assertEqual(Todo.objects.get(pk=self.todo.pk).activity, "actividad")

    def test_view_delete(self):
        response = self.client.post(reverse("delete",kwargs={"pk":self.todo.pk}),
                                    follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")
        self.assertEqual(response.context['list'].count(),0)


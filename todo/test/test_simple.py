import unittest

from django.test import Client
from django.test.testcases import SimpleTestCase
from django.shortcuts import resolve_url

from todo.forms import TodoForm

class SimpleTest(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_view_list(self):
        response = self.client.get(resolve_url("list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")

    def test_view_create(self):
        response = self.client.get(resolve_url("add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"add.html")

    def test_create(self):
        response = self.client.post(resolve_url("add"), {"activity":"esto es un texto"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")
        self.assertTemplateUsed(response.context['list'].count(),0)

    def test_form_invalid(self):
        todo = TodoForm()
        self.assertEqual(todo.is_valid(),False)

    def test_form(self):
        todo = TodoForm({"activity":"esto es un texto"})
        self.assertEqual(todo.is_valid(), True)








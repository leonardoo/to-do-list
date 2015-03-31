from django.core.urlresolvers import reverse

from django.test.testcases import TestCase

class TransactionTest(TestCase):

    fixtures = ['todo.json']

    def test_view_list(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"index.html")
        self.assertEqual(response.context['list'].count(), 3)



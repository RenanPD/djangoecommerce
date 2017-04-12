from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

    def setup(self):
        self.cliente = Client()

    def tearDown(self):
        pass

    def test_status_code(self):
        response = self.cliente.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        response = self.cliente.get(self.url)
        self.assertTemplateUsed(response.status_code, 'index.html')



from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Ap.views import *

class TestUrls(SimpleTestCase):
    
    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_logowanie_url(self):
        url = reverse('logowanie')
        self.assertEquals(resolve(url).func, logowanie)

    def test_rejestracja_url(self):
        url = reverse('rejestracja')
        self.assertEquals(resolve(url).func, rejestracja)

    def test_gruba_url(self):
        url = reverse('gruba')
        self.assertEquals(resolve(url).func, gruba)

    def test_drobna_url(self):
        url = reverse('drobna')
        self.assertEquals(resolve(url).func, drobna)
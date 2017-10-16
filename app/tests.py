from django.test import TestCase
from .models import Category

# Create your tests here.
class CategoryTests(TestCase):

  def test_display_shows_sources_1(self):
    c1 = Category.objects.create(name='test name', code_leb='l1', code_dub='d1')
    actual = c1.__str__()
    expected = 'test name (LB, AE)'
    self.assertEquals(expected, actual)

  def test_display_shows_sources_2(self):
    c1 = Category.objects.create(name='test name', code_leb='l1', code_dub=None)
    actual = c1.__str__()
    expected = 'test name (LB)'
    self.assertEquals(expected, actual)

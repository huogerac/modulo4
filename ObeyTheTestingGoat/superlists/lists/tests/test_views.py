from django.core.urlresolvers import resolve
from django.test import Client, TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape

from lists.views import home_page
from lists.models import Item, List

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)


		
	def test_home_page_only_saves_items_when_necessary(self):
		request = HttpRequest()
		home_page(request)
		self.assertEqual(Item.objects.all().count(), 0)	
		
#	def test_home_page_displays_all_list_items(self):
#		Item.objects.create(text='itemey 1')
#		Item.objects.create(text='itemey 2')

#		request = HttpRequest()
#		response = home_page(request)

#		self.assertIn('itemey 1', response.content.decode())
#		self.assertIn('itemey 2', response.content.decode())
		

class NewListTest(TestCase):
	
	def test_saving_a_POST_request(self):
		client = Client()
		response = client.post(
			'/lists/new',
			data={'item_text': 'A new list item'}
		)
		self.assertEqual(response.status_code, 302)
		
		self.assertEqual(Item.objects.all().count(), 1)
		new_item = Item.objects.all()[0]
		self.assertEqual(new_item.text, 'A new list item')
		self.assertEqual(List.objects.all().count(), 1)
		new_list = List.objects.all()[0]
		self.assertEqual(new_item.list, new_list)
		
		self.assertRedirects(response, '/lists/%d/' % (new_list.id,))
		#self.assertNotContains(response, 'other list item 2')
		#self.assertTemplateUsed(response, 'list.html')
		#self.assertEqual(response.context['list'], list)			

	def test_validation_errors_sent_back_to_home_page_template(self):
		response = Client().post('/lists/new', data={'item_text': ''})
		self.assertEqual(Item.objects.all().count(), 0)
		self.assertTemplateUsed(response, 'home.html')
		expected_error =  escape("You can't have an empty list item")
		self.assertContains(response, expected_error)

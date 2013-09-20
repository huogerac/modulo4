from django.core.urlresolvers import resolve
from django.test import Client, TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

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

class ListAndItemModelsTest(TestCase):

	def test_saving_and_retrieving_items(self):
		list = List()
		list.save()		
		
		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list
		second_item.save()

		saved_lists = List.objects.all()
		self.assertEqual(saved_lists.count(), 1)
		self.assertEqual(saved_lists[0], list)
		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]
		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, list)
		
		self.assertEqual(second_saved_item.text, 'Item the second')		
		self.assertEqual(second_saved_item.list, list)
		
class ListViewTest(TestCase):

	def test_list_view_displays_all_items(self):
		""" this test show how to use client instead of 
		    make request to the view directly and use decode over the response. 
		"""
		list = List.objects.create()
		Item.objects.create(text='itemey 1', list=list)
		Item.objects.create(text='itemey 2', list=list)
		
		other_list = List.objects.create()
		Item.objects.create(text='other list item 1', list=other_list)
		Item.objects.create(text='other list item 2', list=other_list)

		client = Client() #1
		response = client.get('/lists/%d/' % (list.id,))

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2') #4
		self.assertNotContains(response, 'other list item 1')
		self.assertNotContains(response, 'other list item 2')
		self.assertTemplateUsed(response, 'list.html')


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


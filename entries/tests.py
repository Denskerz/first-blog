from django.test import TestCase
from django.urls import reverse
from .models import Entry


class PostModelTest(TestCase):
    def setUp(self):
        self.entry = Entry.objects.create(title='Test Post', content='This is a test post.')

    def test_title(self):
        self.assertEqual(self.entry.title, 'Test Post')

    def test_content(self):
        self.assertEqual(self.entry.content, 'This is a test post.')

    def test_get_absolute_url(self):
        expected_url = reverse('entry-detail', kwargs={'pk': self.entry.pk})
        self.assertEqual(self.entry.get_absolute_url(), expected_url)


class PostViewTest(TestCase):
    def setUp(self):
        self.entry = Entry.objects.create(title='Test Post', content='This is a test post.')

    def test_post_list_view(self):
        url = reverse('entry-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entries/entry_list.html')

    def test_post_detail_view(self):
        url = reverse('entry-detail', kwargs={'pk': self.entry.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entries/entry_detail.html')
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

    def test_post_create_view(self):
        url = reverse('entry-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entries/entry_form.html')

    def test_post_update_view(self):
        url = reverse('entry-update', kwargs={'pk': self.entry.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entries/entry_form.html')

    def test_post_delete_view(self):
        url = reverse('entry-delete', kwargs={'pk': self.entry.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'entries/entry_confirm_delete.html')

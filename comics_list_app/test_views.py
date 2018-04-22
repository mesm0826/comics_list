from django.test import TestCase
from django.urls import reverse


class test_views(TestCase):
    def test_views_add(self):
        response = self.client.get('/comics_list_app/add')

        self.assertTemplateUsed(response, 'comics_list_app/edit.html')
        assert response.status_code == 200
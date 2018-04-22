from django.test import TestCase


class TestViews(TestCase):
    def test_views_add(self):
        response = self.client.get('/comics_list_app/add')

        self.assertTemplateUsed(response, 'comics_list_app/edit.html')
        assert response.status_code == 200
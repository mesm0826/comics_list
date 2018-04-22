from django.urls import resolve
from django.urls.exceptions import Resolver404
import pytest
from .views import *


class TestUrls(object):
    @classmethod
    def setup_class(cls):
        print('start')

    @classmethod
    def teardown_class(cls):
        print('end')

    def setup_method(self, method):
        print('start method={}'.format(method.__name__))

    def teardown_method(self, method):
        print('end method={}'.format(method.__name__))

    def test_add_not_exist(self):
        with pytest.raises(Resolver404):
            resolve('/comics_list_app/not-exist')

    def test_index_exist(self):
        found = resolve('/comics_list_app/')
        assert found.func.__name__ == index.__name__

    def test_add_exist(self):
        found = resolve('/comics_list_app/add')
        assert found.func.__name__ == edit.__name__

    # def test_delete_exist(self):
    #     found = resolve('/comics_list_app/delete/11')
    #     assert found.func.__name__ == delete.__name__

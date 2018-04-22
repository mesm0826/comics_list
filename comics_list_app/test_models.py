from django.core.exceptions import ValidationError
import pytest
from .models import ComicsList


class TestModels(object):
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

    def test_models_collect(self):
        model = ComicsList(title='test', volume=1, username='admin')
        model.full_clean()

    def test_models_title(self):
        with pytest.raises(ValidationError):
            model = ComicsList(title='1'*256, volume=1, username='admin')
            model.full_clean()

    def test_models_volume(self):
        with pytest.raises(ValidationError):
            model = ComicsList(title='test', volume='aaa', username='admin')
            model.full_clean()

    def test_models_username(self):
        with pytest.raises(ValidationError):
            model = ComicsList(title='test', volume=1, username='')
            model.full_clean()



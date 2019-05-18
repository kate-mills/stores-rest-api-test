import json

from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as c:
            with self.app_context():
                response = c.post('/store/test')
                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({'name': 'test', 'items': []},
                                     json.load(response.data))



    def test_create_duplicate_store(self):
        pass

    def test_delete_store(self):
        pass

    def test_find_store(self):
        pass

    def test_store_not_found(self):
        pass

    def test_store_found_with_items(self):
        pass

    def test_store_list(self):
        pass

    def test_store_list_with_items(self):
        pass


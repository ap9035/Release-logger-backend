import unittest
from src.controller import app
from tests.utils import prepare_test_data, delete_test_data


class TestController(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True
        prepare_test_data()

    def tearDown(self) -> None:
        delete_test_data()

    def test_get_latest_two_release(self):
        response = self.app.get('/release/latest-two')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['firstRelease']['app_name'], 'test_channel_fxex')
        self.assertEqual(response.json[0]['firstRelease']['version'], '1.0.2')
        self.assertEqual(response.json[0]['firstRelease']['update_time'], '2023-01-01 00:00:00')
        self.assertEqual(response.json[0]['secondRelease']['app_name'], '')
        self.assertEqual(response.json[0]['secondRelease']['version'], '')
        self.assertEqual(response.json[0]['secondRelease']['update_time'], '2023-01-01 00:00:00')
        self.assertEqual(response.json[2]['firstRelease']['app_name'], 'test_channel_twtx')
        self.assertEqual(response.json[2]['firstRelease']['version'], '1.0.1')
        self.assertEqual(response.json[2]['firstRelease']['update_time'], '2022-01-01 00:00:00')
        self.assertEqual(response.json[2]['secondRelease']['app_name'], 'test_channel_twtx')
        self.assertEqual(response.json[2]['secondRelease']['version'], '1.0.0')
        self.assertEqual(response.json[2]['secondRelease']['update_time'], '2021-01-01 00:00:00')

    def test_get_release_by_app_name(self):
        response = self.app.get('/release/test_channel_mmb')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 3)
        self.assertEqual(response.json[0]['app_name'], 'test_channel_mmb')
        self.assertEqual(response.json[0]['version'], '1.0.2')
        self.assertEqual(response.json[0]['update_time'], '2023-01-01 00:00:00')
        self.assertEqual(response.json[1]['app_name'], 'test_channel_mmb')
        self.assertEqual(response.json[1]['version'], '1.0.1')
        self.assertEqual(response.json[1]['update_time'], '2022-01-01 00:00:00')
        self.assertEqual(response.json[2]['app_name'], 'test_channel_mmb')
        self.assertEqual(response.json[2]['version'], '1.0.0')
        self.assertEqual(response.json[2]['update_time'], '2021-01-01 00:00:00')


if __name__ == '__main__':
    unittest.main()

import os
import unittest
from datetime import datetime

from src.model import Release


class TestRelease(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        """
        delete all data which app_name is started with 'test'
        :return:
        """
        Release.objects(app_name__startswith='test').delete()

    def test_insert_release(self):
        release = Release(
            app_name='test',
            version='1.0.0',
            release_date=datetime.now(),
            branch='master'
        )
        release.save()
        self.assertEqual(release.app_name, 'test')
        self.assertEqual(release.version, '1.0.0')
        self.assertIsNotNone(release.release_date)


if __name__ == '__main__':
    unittest.main()

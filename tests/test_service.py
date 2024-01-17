import unittest
from datetime import datetime
from typing import List

from src.dto import LatestTwoReleaseDto, ReleaseDto
from src.model import Release
from src.service import ReleaseService
from tests.utils import delete_test_data, prepare_test_data


class TestReleaseService(unittest.TestCase):

    releaseService: ReleaseService = ReleaseService()

    def setUp(self) -> None:
        prepare_test_data()

    def tearDown(self) -> None:
        """
        delete all data which app_name is started with 'test'
        :return:
        """
        delete_test_data()

    def test_insert_release(self):

        self.releaseService.insert_release(
            app_name='test_insert',
            version='1.0.0',
            release_date=datetime.now(),
            branch='master'
        )

        release = Release.objects(app_name='test_insert').first()
        self.assertEqual(release.app_name, 'test_insert')

    def test_get_latest_two_release(self):
        release_list: List[LatestTwoReleaseDto] = self.releaseService.get_latest_two_release()
        self.assertEqual(len(release_list), 3)
        self.assertEqual(release_list[0].app_name, 'test_channel_fxex')
        self.assertEqual(release_list[0].firstRelease.version, '1.0.2')
        self.assertEqual(release_list[0].secondRelease.version, '')
        self.assertEqual(release_list[1].app_name, 'test_channel_mmb')
        self.assertEqual(release_list[1].firstRelease.version, '1.0.2')
        self.assertEqual(release_list[1].secondRelease.version, '1.0.1')
        self.assertEqual(release_list[2].app_name, 'test_channel_twtx')
        self.assertEqual(release_list[2].firstRelease.version, '1.0.1')
        self.assertEqual(release_list[2].secondRelease.version, '1.0.0')

    def test_get_release_by_app_name(self):
        release_list: List[ReleaseDto] = self.releaseService.get_release_by_app_name('test_channel_mmb')
        self.assertEqual(len(release_list), 3)


if __name__ == '__main__':
    unittest.main()

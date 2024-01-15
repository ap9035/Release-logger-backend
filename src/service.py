from typing import List

from src.dto import LatestTwoReleaseDto, ReleaseDto
from src.model import Release


class ReleaseService:
    @staticmethod
    def insert_release(app_name, version, update_time):
        release = Release(
            app_name=app_name,
            version=version,
            update_time=update_time
        )
        release.save()

    @staticmethod
    def get_latest_two_release() -> List[LatestTwoReleaseDto]:
        """
        get latest two release, group by app_name
        """
        # Get distinct app_name
        app_names = Release.objects().order_by('app_name').distinct('app_name')
        latest_two_release_list = []
        for app_name in app_names:
            # Get latest two release by app_name
            releases = Release.objects(app_name=app_name).order_by('-update_time')[:2]
            if len(releases) == 2:
                release_dto1: ReleaseDto = ReleaseDto(releases[0].app_name, releases[0].version, releases[0].update_time)
                release_dto2: ReleaseDto = ReleaseDto(releases[1].app_name, releases[1].version, releases[1].update_time)
                latest_two_release_list.append(LatestTwoReleaseDto(release_dto1, release_dto2))
            elif len(releases) == 1:
                release_dto1: ReleaseDto = ReleaseDto(releases[0].app_name, releases[0].version, releases[0].update_time)
                release_dto2: ReleaseDto = ReleaseDto("", "", releases[0].update_time)
                latest_two_release_list.append(LatestTwoReleaseDto(release_dto1, release_dto2))
        return latest_two_release_list

    @staticmethod
    def get_release_by_app_name(app_name: str) -> List[ReleaseDto]:
        """
        get release by app_name
        :param app_name:
        :return:
        """
        releases = Release.objects(app_name=app_name).order_by('-update_time')
        releaseDtoList = []
        for release in releases:
            releaseDtoList.append(ReleaseDto(release.app_name, release.version, release.update_time))
        return releaseDtoList

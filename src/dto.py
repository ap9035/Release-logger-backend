from datetime import datetime


class ReleaseDto:
    def __init__(self, app_name: str, version: str, update_time: datetime):
        self.app_name = app_name
        self.version = version
        self.update_time = update_time

    def serialize(self):
        return {
            'app_name': self.app_name,
            'version': self.version,
            'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')
        }


class LatestTwoReleaseDto:
    def __init__(self, first_release: ReleaseDto, second_release: ReleaseDto):
        self.app_name = first_release.app_name
        self.firstRelease = first_release
        self.secondRelease = second_release

    def serialize(self):
        return {
            'app_name': self.app_name,
            'firstRelease': self.firstRelease.serialize(),
            'secondRelease': self.secondRelease.serialize()
        }

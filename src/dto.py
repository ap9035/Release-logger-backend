from datetime import datetime


class ReleaseDto:
    def __init__(self, app_name: str, version: str, release_date: datetime, branch: str):
        self.app_name = app_name
        self.version = version
        self.release_date = release_date
        self.branch = branch

    def serialize(self):
        return {
            'app_name': self.app_name,
            'version': self.version,
            'release_date': self.release_date.strftime('%Y-%m-%d %H:%M:%S'),
            'branch': self.branch
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

from datetime import datetime

from src.model import Release


def prepare_test_data():
    release_1 = Release(
        app_name='test_channel_mmb',
        version='1.0.0',
        release_date=datetime.strptime('2021-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        branch='master'
    )

    release_2 = Release(
        app_name='test_channel_mmb',
        version='1.0.1',
        release_date=datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        branch='master'
    )

    release_3 = Release(
        app_name='test_channel_mmb',
        version='1.0.2',
        release_date=datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        branch='release/2023-01-01'
    )

    release_4 = Release(
        app_name='test_channel_twtx',
        version='1.0.0',
        release_date=datetime.strptime('2021-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        branch='master'
    )

    release_5 = Release(
        app_name='test_channel_twtx',
        version='1.0.1',
        release_date=datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        branch='release/2023-01-05'
    )

    release_6 = Release(
        app_name='test_channel_fxex',
        version='1.0.2',
        release_date=datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
        branch='release/2023-01-06'
    )

    release_1.save()
    release_2.save()
    release_3.save()
    release_4.save()
    release_5.save()
    release_6.save()


def delete_test_data():
    """
    delete all data which app_name is started with 'test'
    :return:
    """
    Release.objects(app_name__startswith='test').delete()

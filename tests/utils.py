from datetime import datetime

from src.model import Release


def prepare_test_data():
    release_1 = Release(
        app_name='test_channel_mmb',
        version='1.0.0',
        update_time=datetime.strptime('2021-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    )

    release_2 = Release(
        app_name='test_channel_mmb',
        version='1.0.1',
        update_time=datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    )

    release_3 = Release(
        app_name='test_channel_mmb',
        version='1.0.2',
        update_time=datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    )

    release_4 = Release(
        app_name='test_channel_twtx',
        version='1.0.0',
        update_time=datetime.strptime('2021-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    )

    release_5 = Release(
        app_name='test_channel_twtx',
        version='1.0.1',
        update_time=datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    )

    release_6 = Release(
        app_name='test_channel_fxex',
        version='1.0.2',
        update_time=datetime.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
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

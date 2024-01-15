from src.service import ReleaseService
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

releaseService: ReleaseService = ReleaseService()


@app.route('/release', methods=['POST'])
def insert_release():
    """
    insert release
    get data from json
    :return:
    """
    app_name = request.json['app_name']
    version = request.json['version']
    update_time = datetime.strptime(request.json['update_time'], '%Y-%m-%d %H:%M:%S')
    releaseService.insert_release(app_name, version, update_time)
    return jsonify({'result': 'success'})


@app.route('/release/latest-two', methods=['GET'])
def get_latest_two_release():
    """
    get latest two release, group by app_name
    """
    latest_two_release_list = releaseService.get_latest_two_release()
    return jsonify([latest_two_release.serialize() for latest_two_release in latest_two_release_list])


@app.route('/release/<app_name>', methods=['GET'])
def get_release_by_app_name(app_name: str):
    """
    get release by app_name
    :param app_name:
    :return:
    """
    releases = releaseService.get_release_by_app_name(app_name)
    return jsonify([release.serialize() for release in releases])


if __name__ == '__main__':
    app.run(debug=True)
from flask.views import MethodView
from flask import Blueprint, jsonify


class UserRequests(MethodView):
    def post(self):
        return jsonify({'hello': 'created request'}), 200

user_requests = Blueprint("user_requests", __name__)

user_requests_view = UserRequests.as_view('user_requests')

user_requests.add_url_rule("/api/v1/users/requests",  view_func=user_requests_view, methods=['POST'])
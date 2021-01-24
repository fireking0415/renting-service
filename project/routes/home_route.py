from flask import Blueprint, jsonify

from project.routes.result_common import Result

home = Blueprint('home', __name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# 首页接口
@home.route("/home/", methods=["GET"])
def home_index():
    result = Result()
    result.update(data=tasks)
    return jsonify(result.data)

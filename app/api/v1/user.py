from flask import Blueprint, jsonify, g

from app.libs.error_code import NotFound, DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.model.base import db
from app.model.user import User

api = Redprint('user')


#
@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    # token 是否合法
    user = User.query.filter_by(id=uid).first_or_not_found()
    return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    # token 是否合法
    user = User.query.filter_by(id=uid).first_or_not_found()
    return jsonify(user)


# 管理员
@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass


@api.route('', methods=['PUt'])
def update_user():
    return 'update noodles'


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_not_found()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['POST'])
def create_user():
    return 'create noodles'









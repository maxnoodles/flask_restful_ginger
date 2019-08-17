from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake'
    error_code = 999


class ClientTypeError(APIException):
    # 400 参数错误 401 未授权 403 禁止访问 404 找不到页面
    # 500 服务器未知错误
    # 200 请求成功 201 创建，更新成功 204 删除成功
    # 301 302  重定向
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the resource are not_found'
    error_code = 1001


class AuthFailed(APIException):
    # 授权失败
    code = 401
    msg = 'authorization failed'
    error_code = 1005


class Forbidden(APIException):
    # 权限不够
    code = 403
    msg = 'forbidden, not in scope'
    error_code = 1004


class DuplicateGift(APIException):
    # 权限不够
    code = 400
    msg = 'the book has already in gift'
    error_code = 2001

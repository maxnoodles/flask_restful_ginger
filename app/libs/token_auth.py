from collections import namedtuple

from flask import current_app, g, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired
from itsdangerous import BadSignature

from app.libs.error_code import AuthFailed, Forbidden
from app.libs.scope import is_in_scope

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    # HTTP 账号密码
    # key= Authorization
    # value =basic base64(account:password)
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
    return True


User = namedtuple('User', ['uid', 'ac_type', 'scope'])


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    # 验证 token 是否正确
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    uid = data['uid']
    ac_type = data['type']
    scope = data['scope']
    # request 试图函数
    allow = is_in_scope(scope, request.endpoint)
    if not allow:
        raise Forbidden()
    return User(uid, ac_type, scope)

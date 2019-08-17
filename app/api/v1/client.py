from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.model.user import User
from validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 注册 登录
    # 参数 校验 接受参数
    # WTForm 验证表单
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: _register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def _register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                           form.account.data,
                           form.secret.data
                           )

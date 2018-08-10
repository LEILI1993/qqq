from flask import request
from flask_login import login_user, logout_user
from flask_restful import Resource, reqparse, fields, marshal

# 获取数据 get
# post  提交数据
# put  更新
# delete  删除
from apps.account.models import User

#
from apps.ext import login_manager, db
from apps.tools.result_tools import Result, ResponseMsg


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


user_fields = {
    'uid': fields.Integer,
    'username': fields.String
}

ARG_USERNAME_KEY = 'username'

ARG_PASSWORD_KEY = 'password'


class UserLoginApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(ARG_USERNAME_KEY, type=str, required=True, help=u'用户名不能为空')
        self.parser.add_argument(ARG_PASSWORD_KEY, type=str, required=True)

    def get(self):
        args = self.parser.parse_args()
        username = args.get(ARG_USERNAME_KEY)
        password = args.get(ARG_PASSWORD_KEY)
        if username and password:
            user = User.query.filter(User.username == username).first()
            if user:
                if user.verify_password(password):
                    # 登录的方法
                    login_user(user,remember=True)
                    return Result.generate_result_success(marshal(user, user_fields))
                else:
                    return Result.generate_result_error(msg=ResponseMsg.LOGIN_PASSWORD_ERROR_MSG)
            else:
                return {'status': 2, 'msg': '用户账号不存在'}
                pass
        else:
            return {'status': 404, 'msg': '用户名密码不符合规范,请检查后重试'}


# 注册
class UserRegisterApi(Resource):
    def __init__(self):
        # request.form   post
        # args  get
        # request.files  文件上传

        request.values
        # args form  files header   cookie  移动端不支持cookie  header
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, help=u'用户名不能为空', location='form')
        self.parser.add_argument('password', type=str, required=True, location='form')

    def post(self):
        args = self.parser.parse_args()
        username = args.get('username')
        password = args.get('password')

        if username and password:
            try:
                user = User()
                user.username = username
                user.password = password
                db.session.add(user)
                db.session.commit()
            except:
                db.session.rollback()

# 登出
class UserLogoutApi(Resource):
    def post(self):
        logout_user()
        pass

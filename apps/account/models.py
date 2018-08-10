from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from apps.ext import db
"""
登录
login_user(user)
记住状态
login_user(user,rem=True)
登出
logout_user()
验证
login_requird
获取当前用户的信息 request.user
current_user

User用户接口相关
#@property

is_authenticated 认证
is_active 是否激活
is_anonymous 匿名

回调函数
@login_manager_user_loader



"""

class User(db.Model,UserMixin):
    #这里继承的必须改成id  不是id要重写底层
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(64), unique=True,nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    # 0 表示未激活 1 表示激活
    is_delete = db.Column(db.Integer, default=0)

    #  验证数据
    #  声明的时候是方法
    #  使用的时候是属性
    @property
    def password(self):
        return self.password_hash

    # md5
    @password.setter
    def password(self, password):
        if len(password) >= 8:
            # 对密码进行加密
            self.password_hash = generate_password_hash(password)
        else:
            raise Exception('密码不符合规范')

    # 明文   123456
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

from flask_sqlalchemy import SQLAlchemy



#实例化第三方插件
def init_ext(app):
    init_db(app)
    init_cache(app)
    init_cors(app)
    init_login(app)

#===============================数据库配置=================================
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)



#缓存========================================================================

from flask_caching import Cache
#实例化缓存
cache = Cache()

def init_cache(app):
    def init_cache(app):
        cache_config = {
            'CACHE_TYPE': 'redis',
            'CACHE_DEFAULT_TIMEOUT': 60,
            'CACHE_REDIS_HOST': '123456',
            'CACHE_REDIS_PORT': '6379',
            'CACHE_REDIS_PASSWORD': '123456',
            'CACHE__REDIS_DB': 8
        }
        cache.init_app(app, cache_config)


#================================跨域请求配置=============================
from flask_cors import CORS

cors = CORS()

def init_cors(app):
    #针对所有的
    cors.init_app(app,supports_credentials=True)
    #路由前面要加api/vl 针对部分接口提供跨区域请求
    cors.init_app(app, resources={'/api/*': {'orgins': '*'}})
#============================登录=====================
from flask_login import LoginManager
#
# 用户系统
login_manager = LoginManager()

"""
session 存储到redis

"""


def init_login(app):
    # 表示当用户没有登录 跳转的登录方法
    login_manager.login_view = ''
    # basic 默认  strong  None  禁用
    login_manager.session_protection = 'strong'
    login_manager.login_message = '登录之后才能访问'
    login_manager.init_app(app)

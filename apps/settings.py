# 通过类的方式去配置flask项目的配置文件


def get_db_uri(db_config):
    engine = db_config.get('ENGINE') or 'mysql'
    driver = db_config.get('DRIVER') or 'pymysql'
    user = db_config.get('USER') or 'root'
    password = db_config.get('PASSWORD') or '123456'
    host = db_config.get('HOST') or '127.0.0.1'
    port = db_config.get('PORT') or '3306'
    db_name = db_config.get('DB_NAME')
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, db_name)
import datetime

class Config:
    DEBUG = False
    # 登录的对密码,对session数据加密的秘钥
    SECRET_KEY = '110'
    # session存储到redis
    SESSION_TYPE = 'redis'
    # 默认 浏览器关闭之后就过期   设置过期时间为10天
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=10)
    # cookie   默认365
    REMEMBER_COOKIE_DURATION = datetime.timedelta(days=10)

    #  key   value
    #  过期时间
    #  限制获取的路径
    #   DOMAIN
    #   PATH
    #   HTTPONLY
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    DATABASE = {
        #
        # 'ENGINE': 'mysql',
        # 'DRIVER': 'pymysql',
        # 数据库用户名
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': '127,0,0,1',
        # 'PORT': '3306',
        'DB_NAME': 'tpp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        # 数据库用户名
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '远程数据库地址',
        'PORT': '3306',
        'DB_NAME': 'tpp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

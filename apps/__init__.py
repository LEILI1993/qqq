from flask import Flask

from apps.ext import init_ext
from apps.settings import Config, DevConfig, ProductConfig
from apps.urls import init_api

app = Flask(__name__)


def create_app():
    # 项目的配置文件
    app.config.from_object(DevConfig())
    # 路由初始化
    init_api(app)
    # 第三方插件初始化
    init_ext(app)
    return app

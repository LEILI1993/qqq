import datetime

from apps.ext import db

#电影
class Movies(db.Model):
    __tablename__ = 'movies'
    mid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    id = db.Column(db.Integer)
    #电影中文名
    chinese_name = db.Column(db.String(64),unique=False)
    #英文名称
    englist_name = db.Column(db.String(64),unique=False)
    # 导演
    director = db.Column(db.String(64))
    #主演
    leadingRole = db.Column(db.String(64))
    #电影类型
    type = db.Column(db.String(64))
    #国家
    country = db.Column(db.String(64))
    #语言
    language = db.Column(db.String(64))
    #时长
    duration = db.Column(db.String(64))
    # 放映模式
    screening_model = db.Column(db.String(10))
    #上映的时间
    openday = db.Column(db.DateTime, default=datetime.datetime.now())
     #影片背景图
    bg_pic = db.Column(db.String(64))
    # 状态   1 表示热映   2 即将上映
    flag = db.Column(db.Integer, default=1)
    # 是否删除
    is_delete = db.Column(db.Boolean, default=False)

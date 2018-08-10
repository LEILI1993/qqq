import datetime

from apps.ext import db

# 影院
from apps.movies.models import Movies

#影院
class Cinemas(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 影院的名称
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    # 城市
    city = db.Column(db.String(64))
    # 区域
    district = db.Column(db.String(64))
    # 地址
    address = db.Column(db.String(255))
    # 联系电话
    phone = db.Column(db.String(255))
    # 评分
    score = db.Column(db.Float(3, 1))
    # 影厅的数量
    hallnum = db.Column(db.String(100))
    # 手续费
    servicecharge = db.Column(db.String(100))
    # 限购数量
    astrict = db.Column(db.String(100))
    # True 营业    false 休息
    flag = db.Column(db.Integer, default=1)
    # 是否删除
    isdelete = db.Column(db.Boolean, default=True)



# 影厅
class Halls(db.Model):
    hid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    # 1表示 2D 21 3D 3表示4D  4 表示  3D MAX
    screen_type = db.Column(db.Integer, nullable=False)
    seat_num = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)
    cid = db.Column(db.Integer, db.ForeignKey(Cinemas.cid))
    platoons = db.relationship('Platoon', backref='halls', lazy='dynamic')


"""
座位 seat
seat_id

座位类型
x
y
状态(损坏,正常)
是否删除


影厅id
影院id
"""

#座位
class Seats(db.Model):
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 1.普通  2.豪华 3 超豪华
    type = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)
    # 是否可选
    is_choose = db.Column(db.Boolean, default=True)
    #     外键设置
    cid = db.Column(db.Integer, db.ForeignKey(Cinemas.cid))
    hid = db.Column(db.Integer, db.ForeignKey(Halls.hid))

#排片
class Platoon(db.Model):
    pid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 原始价格
    origin_price = db.Column(db.Numeric(7, 2), default=0.00)
    # 折扣价
    discount_price = db.Column(db.Numeric(7, 2), default=0.00)
    # 影片开始时间
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    # 1 未放映   2 正在放映   3结束放映
    status = db.Column(db.Integer, default=1)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    update_date = db.Column(db.DateTime, default=datetime.datetime.now())
    is_delete = db.Column(db.Boolean, default=False)
    # 外键相关
    mid = db.Column(db.Integer, db.ForeignKey(Movies.mid))
    hid = db.Column(db.Integer, db.ForeignKey(Halls.hid))
    cid = db.Column(db.Integer, db.ForeignKey(Cinemas.cid))







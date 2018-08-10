# 参数传递
# /list/<int:page>/<int:size>
# ?page=1&size=10
# cinemas?city='武汉'
'''
1>restful  参数的基本使用
parser.add_argument(arguments,type=None,help='',default=)
# arguments  参数的key
# type   要转化的参数的类型
help   参数出现错误时的提示信息
default  参数的默认值

必要参数
required=True
'''
# 列表 一个键对应多个值  列表
# 位置参数  form 表单 heads   cookies files(文件上传)  args
from flask_restful import Resource, reqparse, marshal_with, fields

from apps.cinema.models import Cinemas, Platoon, Halls, Seats
from apps.movies.models import Movies

cinemas_fields = {
    'cid': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'district': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'score': fields.Float,
    'hallnum': fields.Integer,
    'servicecharge': fields.Float,
    'astrict': fields.Integer,
    'flag': fields.Integer,
    'isdelete': fields.Integer
}
districts_fields = {
    'cid': fields.Integer,
    'district': fields.String,
}

data = {

    'cinemas': fields.List(fields.Nested(cinemas_fields)),
    'districts': fields.List(fields.Nested(districts_fields)),
}

result = {
    'msg': fields.String(default='success'),
    'status': fields.Integer(default=200),
    'data': fields.Nested(data),

}


class CinemasResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('city', type=str, default='深圳', required=True, help='必要参数')
        self.parser.add_argument('page', type=int, default=1)
        self.parser.add_argument('size', type=int, default=10)
        self.parser.add_argument('district', type=str)
        self.parser.add_argument('keyword', type=str)
        # 1 表示升序 0 表示降序
        self.parser.add_argument('score_sort', type=int)

    @marshal_with(result)
    def get(self):
        # 获取所有的参数 返回一个字典对象
        args = self.parser.parse_args()
        # 获取城市参数
        city = args.get('city')
        # 获取区域参数
        district = args.get('district')
        # 搜索 关键字查找影院
        keyword = args.get('keyword')
        # 评分排序字段
        score_sort = args.get('score_sort')
        # 如果参数有传值
        query = Cinemas.query.filter(Cinemas.city == city)
        # query = Cinemas.query.filter_by(city=city)
        # 判断区域  /?city=  & district=
        if district:
            query = query.filter_by(district=district)
            # query = query.filter(Cinemas.district == district)
        # 通过关键字查询  /?city=  & keyword=   模糊查询
        if keyword:
            query = query.filter(Cinemas.name.like('%{}%'.format(keyword)))
        #  如果用户选择按评分进行排序  /?city=  & score_sort=1  模糊查询
        if score_sort:
            if score_sort == 1:
                # 降序  从大到小
                query = query.order_by(Cinemas.score.desc())
            else:
                # 升序  从小到大
                query = query.order_by(Cinemas.score.asc())
        cinemas = query.all()
        # 查询区域 在这里过滤排序去从
        districts = Cinemas.query.filter(Cinemas.city == city).group_by(Cinemas.district).all()
        data = {
            'cinemas': cinemas,
            'districts': districts
        }
        result = {
            'data': data
        }
        return result


# ===================放映===================
cinema_field = {
    'cid': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'district': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'score': fields.Float,
    'hallnum': fields.Integer,
    'servicecharge': fields.Float,
    'astrict': fields.Integer,
    'flag': fields.Integer,
    'isdelete': fields.Integer,
}

movie_field = {
    'mid': fields.Integer,
    'showname': fields.String,
    'shownameen': fields.String,
    'director': fields.String,
    'leading_role': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.String,
    'screening_model': fields.String,
    'backgroundpicture': fields.String,
    'openday': fields.DateTime,
}
plat_field = {
    'pid': fields.Integer,
    'origin_price': fields.Float,
    'discount_price': fields.Float,
    'start_time': fields.DateTime,
    'end_time': fields.DateTime,
}
districts_field = {
    'cid': fields.Integer,
    'district': fields.String,
}


data1 = {
    'districts': fields.List(fields.Nested(districts_field)),
    'cinemas': fields.List(fields.Nested(cinema_field)),
    'cinema': fields.Nested(cinema_field),
    'movies': fields.List(fields.Nested(movie_field)),
    'plats': fields.List(fields.Nested(plat_field))
}

result1 = {
    'msg': fields.String(default='success'),
    'status': fields.Integer(default=200),
    'data': fields.Nested(data),
}


class CinemasDetail(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('cid', type=int, required=True)
    @marshal_with(result1)
    def get(self):
        args = self.parser.parse_args()
        cid = args.get('cid')
        # 获取当前影院所有的排片信息
        plats = Platoon.query.filter(Platoon.cid == cid).all()
        # 影院的信息
        cinema = Cinemas.query.get(cid)
        # 影片的数据
        movies = []
        for plat in plats:
            movie = Movies.query.get(plat.mid)
            movies = Halls.query.get(plat.mid)
            mov = Seats.query.get(plat.mid)
            movies.append(movie)
        data1 = {
            'movies': movies,
            'plats': plats,
            'cinema': cinema,
        }
        result1 = {
            'data': data1
        }
        return result1

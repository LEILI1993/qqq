from flask_restful import Resource, fields, marshal_with, reqparse

# page=1&size=10

# page per_page
from apps.cinema.models import Cinemas, Platoon
from apps.movies.models import Movies

"""
{ 
     'status': 200,
     'msg': 'success',
    'data':{
            'pager':{
                这个是前端页面要的总记录数  和 总页数
                'total':100 总的记录数
                'size':10  总页数
            }
            movies:[
                {}, 这个是查询出的数据详细
                {},
            
            ]
    }
}

"""
pager = {
    # 返回的的总记录数
    'total': fields.Integer,
    # 设定的页数
    'pages': fields.Integer(default=10),

}

movies = {
    'mid':fields.Integer,
    'chinese_name': fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'country': fields.String,
    'duration': fields.String,
    'bg_pic': fields.String,
}
data = {
    # 热映分页数据
    'pager1': fields.Nested(pager),
    # 即将上映分页数据
    'pager2': fields.Nested(pager),
    # 热映
    'hots': fields.List(fields.Nested(movies)),
    # 即将上映
    'upcomings': fields.List(fields.Nested(movies)),

}
result = {
    'status': fields.Integer(default=200),
    'msg': fields.String(default='success'),
    'data': fields.Nested(data)

}


class MoviesListApi(Resource):
    @marshal_with(result)
    def get(self, page, size):
        paginate1 = Movies.query.filter_by(flag=1).paginate(page=page, per_page=size, error_out=False)
        paginate2 = Movies.query.filter_by(flag=2).paginate(page=page, per_page=size, error_out=False)
        data = {
            'pager1': {'total': paginate1.total, 'pages': paginate1.pages},
            'pager2': {'total': paginate2.total, 'pages': paginate2.pages},
            'hots': paginate1.items,
            'upcomings': paginate2.items
        }
        result = {
            'data': data
        }
        return result

#===============================通过点击电影  电影详情======================


"""
# 请求地址movies/detail?mid=1

必要参数   mid
必要参数   city
{
    'data':{
        'movie': {'导演':a,',名字:战狼}
        ' district':[{},{},{}]
        'cinema';[{},{},{}]
        'platoons':[{},{},{}],
    }  
}

"""


movies = {
    'mid':fields.Integer,
    'chinese_name': fields.String,
    'englist_name': fields.String,
    'director': fields.String,
    'leadingRole': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.String,
    'screening_model': fields.String,
    'openday': fields.DateTime,
    'bg_pic': fields.String,
}
#地区
cinema_director = {
    'cid':fields.Integer,
    'director':fields.String,

}
cinema_name = {
    'cid':fields.Integer,
    'cinema': fields.String,
    'address': fields.String,
    'phone': fields.String,
}
platoon_details = {
    'pid': fields.Integer,
    'origin_price': fields.Float,
    'discount_price': fields.Float,
    'start_time': fields.DateTime,
    'end_time': fields.DateTime,
}

data = {
    # 电影表字段
    'movie': fields.List(fields.Nested(movies)),
    # 通过城市查到区域
    'district': fields.List(fields.Nested(cinema_director)),
    # 通过城市查影院名字
    'cinema': fields.List(fields.Nested(cinema_name)),
    #通过影院查到电影的排片
    'platoon': fields.List(fields.Nested(platoon_details)),

}

result1 = {
    'status': fields.Integer(default=200),
    'msg': fields.String(default='success'),
    'data': fields.Nested(data)

}


class MoviesDetail(Resource):
    def __init__(self):
        # 掉父类的方法
        super(MoviesDetail, self).__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('mid', type=int, required=True)
        self.parser.add_argument('city', type=str, required=True)
        self.parser.add_argument('district', type=str, required=True)

    @marshal_with(result1)
    def get(self):
        args = self.parser.parse_args()
        mid = args.get('mid')
        city = args.get('city')
        city = args.get('district')
        movie = Movies.query.get(mid)
        #获取所有的区域
        dists = Cinemas.query.filter(Cinemas.city == city).group_by(Cinemas.district).all()

        cinemas = Cinemas.query.filter(Cinemas.city == city).all()
        plats = Platoon.query.filter(Platoon.cid == cinemas[0].cid).filter(Platoon.mid == mid).all()
        data = {
            'movie': movie,
            'district': dists,
            'cinema': cinemas,
            'platoon': plats,
        }

        detail_result = {
            'data': data
        }
        return result1

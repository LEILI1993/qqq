from flask_restful import Resource, marshal_with, fields

from apps.movies.models import Movies
import datetime
from apps.cinema.models import Cinemas

# {
#     'msg': 'success',
#     'status': 200,
#     'data': {
#           'banners':[]
#            'hots':[]
#            'nows':[]

banners = {
    'id': fields.Integer,
    'url': fields.String,
}

movies = {
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

data = {
    'hots ': fields.List(fields.Nested(movies)),
    'nows': fields.List(fields.Nested(movies)),
    'hots_count': fields.Integer,
    'nows_count': fields.Integer,
}

result = {
    'status': fields.Integer(default=200),
    'msg': fields.String(default='success'),
    'data': fields.Nested(data)

}


class IndexApi(Resource):
    @marshal_with(result)
    def get(self):
        hot = Movies.query.filter_by(flag=1).limit(5).all()
        now = Movies.query.filter_by(flag=2).limit(5).all()
        hot_count = Movies.query.filter_by(flag=1).count()
        now_count = Movies.query.filter_by(flag=2).count()
        data = {
            'hots ': hot,
            'nows': now,
            'hots_count': hot_count,
            'nows_count': now_count,
        }
        result = {
            'start': 200,
            'msg': 'success',
            'data': data
        }

        return result

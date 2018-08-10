from flask_restful import Api


from apps.cinema.apis import CinemasResource, CinemasDetail
from apps.main.apis import IndexApi

# http://xxx//api/v1/idnex/
from apps.movies.apis import MoviesListApi

api = Api()
# 前缀
#api = Api(prefix='/api/vl')

# url('', ''.name)
api.add_resource(IndexApi, '/index/')
api.add_resource(MoviesListApi, '/movies/list/<int:page>/<int:size>/')
api.add_resource(CinemasResource, '/cinemas/list/')
# cinemas?city='武汉' # ?page=1&size=10
api.add_resource(CinemasDetail, '/cinemas/list1/')


#用户相关胚子
# api.add_resource(UserApi, '/user/login/','/user/register/','user/logout/','/user/update/')


def init_api(app):
    api.init_app(app)

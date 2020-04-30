from flask import Blueprint

from common.libs.Helper import ops_render

router_goods = Blueprint('goods_page',__name__)

@router_goods.route('/index')
def index():
    resp_data = {}
    return ops_render('goods/index.html')

@router_goods.route('/info')
def info():
    resp_data = {}
    return ops_render('goods/info.html')

@router_goods.route('/set')
def set():
    resp_data = {}
    return ops_render('goods/set.html')

@router_goods.route('/cat')
def cat():
    resp_data = {}
    return ops_render('goods/cat.html')

@router_goods.route('/cat_set')
def cat_set():
    resp_data = {}
    return ops_render('goods/cat_set.html')




from flask import Blueprint,request,redirect,jsonify
from sqlalchemy import or_

from common.libs.Helper import ops_render,getCurrentDate,iPagenation
from common.libs.UrlManager import UrlManager
from common.libs.user.UserService import UserService
from common.models.User import User
from application import db,app

router_account = Blueprint("account_page",__name__)

@router_account.route("/index")
def index():
    resp_data = {}
    query = User.query
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(User.status == int(req['status']))
    if 'mix_kw' in req:
        rule = or_( User.nickname.ilike("%{0}%".format(req['mix_kw'])), User.mobile.ilike("%{0}%".format(req['mix_kw'])) )
        query = query.filter(rule)

    params = {
        "total":query.count(),
        "page_size":2,
        "page":page,
        "url":request.full_path.replace("&p={}".format(page),"")
    }
    pages = iPagenation(params)
    # 当前页数据开始位置  
    offset = (page-1) * 2
    # 当前页数据结束位置  
    limit = page * 2

    list = query.all()[offset:limit]


    resp_data['list'] = list
    resp_data['status'] = app.config['STATUS']
    resp_data['pages'] = pages
    return ops_render("/account/index.html",resp_data)

@router_account.route("/info")
def info():
    resp_data = {}
    req = request.args
    uid = int(req.get("id",0))
    reback_url = UrlManager.buildUrl("/account/index")
    if uid < 1:
        return redirect(reback_url)
    info = User.query.filter_by(uid=uid).first()
    if not info:
        return redirect(reback_url)
    resp_data['info'] = info
    return ops_render("/account/info.html",resp_data)

'''
    带id参数，就是修改：更新数据库
    不带id参数，就是添加：创建数据，插入数据库
'''
@router_account.route("/set",methods=['GET','POST'])
def set():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        uid = int(req.get("id",0))
        info = None
        if uid:
            info = User.query.filter_by(uid=uid).first()
        resp_data['info'] = info
        return ops_render("/account/set.html",resp_data)
    # POST
    resp = {
        'code':200,
        'msg':"操作成功",
        'datat':{}
    }

    # 获取前端ajax传递的data
    req = request.values
    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'id' in req else ''
    mobile = req['mobile'] if 'id' in req else ''
    email = req['email'] if 'id' in req else ''
    login_name = req['login_name'] if 'id' in req else ''
    login_pwd = req['login_pwd'] if 'id' in req else ''

    # 校检
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入规范的昵称"
        return jsonify(resp)

    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入规范的手机"
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入规范的邮箱"
        return jsonify(resp)

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入规范的登录名"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入规范的登录密码"
        return jsonify(resp)

    # 筛选
    is_exits = User.query.filter(User.login_name == login_name,User.uid != id).first()
    if is_exits:
        resp['code'] = -1
        resp['msg'] = "该登录名已经存在，请更换"
        return jsonify(resp)


    user_info = User.query.filter_by(uid=id).first()

    if user_info:
        model_user = user_info
    else:
        model_user = User()
        # 插入格式化的时间
        model_user.created_time = getCurrentDate()
        # 生成16位的加密字符串
        model_user.login_salt = UserService.generateSalt()
    model_user.nickname = nickname
    model_user.mobile = mobile
    model_user.email = email
    model_user.login_name = login_name
    if user_info and user_info.uid == 1:
        resp['code'] = -1
        resp['msg'] = "该用户为Bruce"
        return jsonify(resp)

    model_user.login_pwd =  UserService.generatePwd(login_pwd,model_user.login_salt)
    # 插入格式化的时间
    model_user.updated_time = getCurrentDate()

    db.session.add(model_user)
    db.session.commit()     
    return jsonify(resp) 

@router_account.route("remove-or-recover",methods=['GET','POST'])
def removeOrRecover():
    resp = {
        'code':200,
        'msg':"操作成功",
        'data':{}
    }

    req = request.values
    id = req['id'] if 'id' in req else 0
    acts = req['acts'] if 'acts' in req else ''
    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号"
        return jsonify(resp)
    if acts not in ['remove','recover']:
        resp['code'] = -1
        resp['msg'] = "操作有误"
        return jsonify(resp)

    user_info = User.query.filter_by(uid=id).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "该账号不存在"
        return jsonify(resp)
    if user_info and user_info.uid == 1:
        resp['code'] = -1
        resp['msg'] = "该账号是Bruce，不允许操作"
        return jsonify(resp)

    if acts == 'remove':
        user_info.status = 0
    elif acts == 'recover':
        user_info.status = 1

    user_info.updated_time = getCurrentDate()
    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp) 
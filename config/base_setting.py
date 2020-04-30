import pymysql
pymysql.install_as_MySQLdb()
# 设置服务器端口
SERVER_PORT = 8999
# 连接到数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:741100nie@127.0.0.1/hmsx_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# cookie
AUTH_COOKIE_NAME = '1903_hmsx'

#拦截器规则
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
] 

STATUS = {
    '1':'正常',
    '0':'已删除'
}

UOLOAD = {
    'ext':['jpg','png','gif','bmp','jpeg'],
    'perfix_path':'/web/static/upload',
    'prerix_url':'/static/upload'
}
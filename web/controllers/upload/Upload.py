
@router_upload.route('/pic',methods=['GET'.'GET'])
def uploadpic():
    file_target = request.files
    filename =file_target['pic'].filename
    #讲图片保存到 static/upload/pic.jpg
    print
;

var user_reset_pwd_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $("#save").click(function(){
            var btn_target = $(this)
            if (btn_target.hasClass("disabled")){
                alert("正在运行")
                return
            }
            var old_password = $("#old_password").val()
            var new_password = $("#new_password").val()

            if (!old_password || old_password.length < 6){
                alert("旧密码错误")
                return false
            }

            if (!new_password || new_password.length < 6){
                alert("新密码格式错误")
                return false
            }

            btn_target.addClass("disabled")

            $.ajax({
                url:common_ops.buildUrl("/user/reset-pwd"),
                type:"POST",
                data:{"old_password":old_password,"new_password":new_password},
                dataType:"json",
                success:function(resp){
                    common_ops.alert("ok")
                    console.log(resp.msg)
                    btn_target.removeClass("disabled")
                },
                error:function(error){
                    console.log(error)
                    common_ops.alert("修改密码失败")
                }
            })
        })
    }
}

$(document).ready(function(){
    user_reset_pwd_ops.init()
})
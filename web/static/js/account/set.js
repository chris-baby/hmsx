;

var account_set_ops = {
    init:function(){
        this.eventBind()
    },
    eventBind:function(){
        $(".wrap_account_set .save").click(function(){
            var nickname = $(".wrap_account_set input[name=nickname]").val();
            var mobile = $(".wrap_account_set input[name=mobile]").val();
            var email = $(".wrap_account_set input[name=email]").val();
            var login_name = $(".wrap_account_set input[name=login_name]").val();
            var login_pwd = $(".wrap_account_set input[name=login_pwd]").val();
            // 前端校检
            if (nickname.length < 1) {
                alert("请输入符合规范的昵称")
                return false
            }
            if (mobile.length < 1) {
                alert("请输入符合规范的手机号")
                return false
            }
            if (email.length < 1) {
                alert("请输入符合规范的邮箱")
                return false
            }
            if (login_name.length < 1) {
                alert("请输入符合规范的登录名")
                return false
            }
            if (login_pwd.length < 1) {
                alert("请输入符合规范的登录密码")
                return false
            }

            id = $(".wrap_account_set input[name=id]").val()
            var data = {
                nickname:nickname,
                mobile:mobile,
                email:email,
                login_name:login_name,
                login_pwd:login_pwd,
                id:id
            }

            $.ajax({
                url:common_ops.buildUrl("/account/set"),
                type:"POST",
                data:data,
                dataType:"json",
                success:function(resp){
                    console.log(resp.msg)
                    if (resp.code == 200) {
                        window.location.href = common_ops.buildUrl("/account/index")
                    }
                },
                error:function(error){
                    console.log(error)
                }
            })
        })
    }
}

$(document).ready(function(){
    account_set_ops.init()
}) 
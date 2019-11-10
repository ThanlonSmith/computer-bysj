console.log('已加载register.js');
$(document).ready(function () {
    // 表单控件的验证
    $('#name').bind('input', function () {
        // 获取name的值并赋值给变量
        var name_value = $('#name').val();
        var reg_name = /^[a-zA-Z0-9_-]{0,10}$/;
        if (!reg_name.test(name_value)) {
            $('#name_error').text('必须是大小写字母数字,不能是空格或特殊字符!');
        }
        if (reg_name.test(name_value)) {
            $('#name_error').text('');
        }
        if (name_value.length === 0) {
            $('#name_error').text('');
        }
    });
    $('#mobile_number').bind('input', function () {
        var mobile_number = $('#mobile_number').val();
        var reg_mobile_number = /^1[345789]\d{9}$/;
        if (mobile_number.length < 11) {
            $('#mobile_number_error').text('不能少于11位数！')
        }
        if (mobile_number.length === 11 && !reg_mobile_number.test(mobile_number)) {
            $('#mobile_number_error').text("不是有效的手机号码!");
        }
        if (reg_mobile_number.test(mobile_number) || mobile_number.length === 0) {
            $('#mobile_number_error').text("");
        }
    });

    $('#pwd').bind('input', function () {
        // 获取name的值并赋值给变量
        var pwd_value = $('#pwd').val();
        var reg_pwd = /^[a-zA-Z][a-zA-Z0-9_]{6,15}$/;
        if (!reg_pwd.test(pwd_value)) {
            $('#pwd_error').text('必须以字母开头,允许字母数字下划线，不少于6位!');
        } else {
            $('#pwd_error').text('');
        }
        if (pwd_value.length === 0) {
            $('#pwd_error').text('');
            $('#sure_pwd_error').text('');
            $('#sure_pwd').val("");
        }
    });
    $('#sure_pwd').bind('input', function () {
        // 获取name的值并赋值给变量
        var sure_pwd_value = $('#sure_pwd').val();
        var pwd_value = $('#pwd').val();
        if (pwd_value.length === 0) {
            $('#pwd_error').text('请输入密码！');
        }
        if (sure_pwd_value !== pwd_value) {
            $('#sure_pwd_error').text('两次输入密码不一致！');
        } else {
            $('#sure_pwd_error').text('');
        }
        if (sure_pwd_value.length === 0) {
            $('#sure_pwd_error').text('');
            $('#pwd_error').text('');
        }
    });
    $('#verify_code').bind('input', function () {
        var reg_code = /[0-9]{6,6}$/;
        var verify_code = $('#verify_code').val();
        // alert(verify_code);
        // alert(verify_code.length);
        if (verify_code.length < 6) {
            $('#code_error').text('验证码必须是6位');
        }
        if (!reg_code.test(verify_code)) {
            $('#code_error').text('验证码必须是6位,必须都是数字!');
        }
        if (reg_code.test(verify_code) || verify_code.length === 0) {
            $('#code_error').text('');
        }
    })
});

function send_verification_code(ths) {
    //获取手机号
    var mobile_number = $('#mobile_number').val();
    // alert(mobile_number);
    // 定义手机号的正则
    var pattern = /^1[345789]\d{9}$/;
    // 判断是否输入手机号以及格式格式是否正确
    if (mobile_number === "" || mobile_number.length == 0) {
        alert("手机号不能为空!");
        return;
    }
    if (!pattern.test(mobile_number)) {
        alert("手机号格式错误!");
        return;
    } else {
        $.ajax({
            url: '/v1/send_code',
            type: 'post',
            data: {
                'mobile_number': mobile_number
            },
            success: function (data) {
                if (data) {
                    if (data == 'ok') {
                        alert('发送成功！')
                    }
                }
            }
        });
        // 如果输入手机号先让发送按钮不可用
        // ths.setAttribute("disabled", "disabled");
        // 设置倒计时时间
        var count = 60;
        // 设置定时器控制用户发送请求验证码的时间间隔
        var timer = setInterval(function () {
            ths.value = count + "s";
            count--;
            if (count < 0) {
                ths.removeAttribute("disabled");
                clearInterval(timer);
                ths.value = "获取手机验证码";
            }
        }, 1000);
    }
}

function user_register() {
    var name = $('#name').val();
    var mobile_number = $('#mobile_number').val();
    var pwd = $('#pwd').val();
    var sure_pwd = $('#sure_pwd').val();
    var verify_code = $('#verify_code').val();
    if (name == null || name.length === 0) {
        $('#name_error').text('用户名不能为空！');
        return;
    }
    var reg_name = /^[a-zA-Z0-9_-]{0,10}$/;
    if (!reg_name.test(name)) {
        $('#name_error').text('用户名格式不正确！');
    }
    if (mobile_number == null || mobile_number.length === 0) {
        $('#mobile_number_error').text('手机号不能为空！');
        return;
    }
    var reg_mobile_number = /^1[345789]\d{9}$/;
    if (!reg_mobile_number.test(mobile_number)) {
        $('#mobile_number_error').text('手机号格式不正确！');
        return;
    }
    if (pwd == null || pwd.length === 0) {
        $('#pwd_error').text('密码不能为空！');
        return;
    }
    var reg_pwd = /^[a-zA-Z][a-zA-Z0-9_]{6,15}$/;
    if (!reg_pwd.test(pwd)) {
        $('#pwd_error').text('密码格式错误！');
        return;
    }
    if (sure_pwd == null || sure_pwd.length === 0) {
        $('#sure_pwd_error').text('确认密码不能为空！');
        return;
    }
    if (!reg_pwd.test(name)) {
        $('#sure_pwd_error').text('确认密格式不正确！');
        return;
    }
    if (sure_pwd !== pwd) {
        $('#sure_pwd_error').text('两次输入密码不一致！');
        return;
    }
    if (verify_code == null || verify_code.length === 0) {
        $('#code_error').text('手机验证码不能为空！');
        return;
    }
    var reg_code = /[0-9]{6,6}$/;
    if (!reg_code.test(verify_code)) {
        $('#code_error').text('手机验证码格式错误！');
        return;
    }

    $.ajax({
        url: '/v1/register',
        type: 'post',
        data: {
            'name': name,
            'mobile_number': mobile_number,
            'pwd': pwd,
            'verify_code': verify_code,
        },
        success: function (data) {
            // alert(data);
            if (data == 'ok') {
                $('#reg_success').text('注册成功，您可以登录了……')
                location.href = '/'
            }
            if (data == 'verify_code_err') {
                $('#code_error').text('手机验证码输入错误！')
            }
            if (data == 'mobile_error') {
                $('#mobile_number_error').text('此手机号已经注册过!')
            }
            if (data == 'name_error') {
                $('#name_error').text('此账号已经被注册过!')
            }
            if (data == 'db_error') {
                $('#reg_error').text('注册失败！')
            }
        }
    })
}
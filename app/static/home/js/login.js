function user_login() {
    // alert('1');
    name = $('#login_name').val();
    pwd = $('#login_pwd').val();
    // console.log(name);
    // console.log(pwd);
    if (name == null || name.length == 0) {
        $('#login_name_error').text('账号不能为空！');
        return;
    }
    if (pwd == null || pwd.length == 0) {
        $('#login_pwd_error').text('密码不能为空！');
        return;
    }
    reg_pwd = /^[a-zA-Z][a-zA-Z0-9_]{6,15}$/;
    if (!reg_pwd.test(pwd)) {
        $('#login_pwd_error').text('密码格式不正确！');
        return;
    }
    $('#login_error').text('登录中 ');
    $('#login-img').removeAttr('hidden');
    $.ajax({
        url: '/v1/login/',
        type: 'post',
        data: {
            'name': name,
            'pwd': pwd
        },
        success: function (data) {
            // alert(data);
            if (data == 'ok') {
                location.href = '/'
            }
            if (data == 'error') {
                $('#login_error').text('用户名或密码错误！')
            }
        }
    })
}
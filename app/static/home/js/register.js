import da from "../../admin/adminlte-master/bower_components/moment/src/locale/da";

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
        var verify_code = $('#vertification_code').val();
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
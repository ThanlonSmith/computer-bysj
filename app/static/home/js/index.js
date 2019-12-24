$(document).ready(function () {
    var content_right = $('#container-right');
    // 浏览器窗口的高度
    var windowHeight = $(window).height();
    // 距离文档顶部的高度，是固定值
    var offset_top_height = content_right.offset().top;
    // 右侧内容的高度，是固定值
    var content_height = content_right.height();
    // 距浏览器窗口顶部的距离
    var content_right_height = 0;
    $(window).scroll(function () {
            //  标签距离文档顶部的高-窗口与文档顶部的距离
            content_right_height = offset_top_height + content_height - $(window).scrollTop();
            // 随着内容向上翻，一旦标签距浏览器窗口顶部的距不大于窗口的高度，就让标签贴近最下面
            if (content_right_height < windowHeight) {
                content_right.css({'margin-top': '255px'});
            } else {
                content_right.css({'margin-top': '0'})
            }
        }
    );
});
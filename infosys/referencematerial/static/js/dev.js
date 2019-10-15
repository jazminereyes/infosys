$(document).ready(function(){
    $(window).scroll(function(){
        if($(this).scrollTop()>5){
            $('#site-logo').attr('src', '/static/images/pupie-black.png');
        } else{
            $('#site-logo').attr('src', '/static/images/pupie-light.png');
        }
    });
});
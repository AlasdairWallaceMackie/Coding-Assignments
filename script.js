console.log("Script has been linked");
var imgLength = 100;
$('img').attr("src", "https://loremflickr.com/"+imgLength+"/"+imgLength);

$('button.hide').click(function(){
    console.log("Hiding...");
    $(this).parent().hide();
});

$('button.show').click(function(){
    console.log("Showing...");
    $('.hidden').show();
    $('.hidden').css("display", "inline-block");
});

$('button.toggle').click(function(){
    console.log("Toggling");
    $('img.toggleable').toggle();
});

$('button.slide_up').click(function(){
    $(".slide").slideUp();
});

$('button.slide_down').click(function(){
    $(".slide").slideDown();
});

$('button.slide_toggle').click(function(){
    $('.slide').slideToggle();
});

$('button.fade_in').click(function(){
    $('.slide').fadeIn();
});

$('button.fade_out').click(function(){
    $('.slide').fadeOut();
});

$('button.add_class').click(function(){
    $(this).parent().addClass("light_blue_background");
});

$('button.before').click(function(){
    $('.before_or_after .text').before("<p>You added a paragraph before!");
});

$('button.after').click(function(){
    $('.before_or_after .text').after("<p>You added a paragraph after!");
});

var appended=false;
$('.append').click(function(){
    console.log("Appending");
    if(appended==false){
        $(".to_append").append(" Falls Mainly on the Plain.");
        appended=true;
    }
    
});

$(".to_HTML").click(function(){
    console.log("Show HTML");
    var a = $(this).html();
    $(this).text(a);
});

$("button.attr").click(function(){
    // $('img').attr("src", "https://loremflickr.com/150/150");
    if($(this).hasClass('smaller')){
        imgLength-=20;
    }
    else if($(this).hasClass('larger')){
        imgLength+=20;
    }
    $('img').attr("src", "https://loremflickr.com/"+imgLength+"/"+imgLength);
});
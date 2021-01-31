
for(var i=1;i<=8;i++){
    console.log("loop");
            $("#boxes").append("<div class='img_box'><img src='ninja.png'></div>");
}

$('img').click(function(){
    console.log("Image clicked");
    $(this).css("display", "none");
});

$("#restore").click(function(){
    console.log("Restore clicked");
    $('img').css("display","inline");
});
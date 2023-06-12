var parentElem = document.getElementById('maincontainer').parentNode;
var parentWidth = parentElem.offsetWidth;
var parentHeight = parentElem.offsetHeight;
var howmanyboxes=parentWidth/64;
console.log(parentWidth + "--"+ parentHeight + "---" + Math.ceil(howmanyboxes));
var createBoard = function()
{
    rank = ["A","B","C","D","E","F","G","H" ,"I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
    file = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30];
    var currentTile = {};
    var count = 0;
    for(var i = 0; i < rank.length; i++)
    // console.log(rank.length);
    {
        for (var j = 0; j < file.length; j++)
        {
            if(count%36 == 0)
            {
            $("#chessboard").append('<div class="tile smoothfade" style="clear:left; position:relative;"><div class="circle"></div></div>');

            }else{
            $("#chessboard").append('<div class="tile smoothfade" style="position:relative;"><div class="circle"></div></div>');
            }
            $(".tile").eq(count).attr("data-gridpos",((rank[rank.length - (i +1)]+file[j])));
            
            if(((i%2 == 0) && (j%2 != 0)) || ((i%2 != 0) && (j%2 == 0)))
            {
            $(".tile").eq(count).addClass("black"  + " " + rank[rank.length - (i +1)]+file[j]);
            }
            else
            {
            $(".tile").eq(count).addClass("white"  + " " + rank[rank.length - (i +1)]+file[j]);
            }
            count++;
        }
    }
}
jQuery(document).ready(function($) {
    createBoard();
    console.log("Created Chessboard");
    tiles = $(".tile");
    $(".tile").on('click',function(){
        currentTile = $(this);
        var midY = $(this).position().top += ( $(this).width() / 2 );
        var midX = $(this).position().left += ( $(this).width() / 2 );
        var player = $("#player");
        tiles.removeClass('legal');		
        console.log("X : "+midX + " || Y : "+midY);
        player.css({"top":midY - (0.5 * player.width()), "left":midX-(0.5*player.width())});
        console.log("Last Clicked Tile : "+currentTile.data("gridpos"));

    })
    .on('mouseenter',function(){
        $(this).addClass('hover');
    })
    .on('mouseleave',function(){
        $(this).removeClass('hover');
    });
    var displaylegal = $("#controlbox > ul > li");
    displaylegal.on('click',function(){
        console.log($(this).attr('id'))
        legalMove($(this).attr('id'));
    })
    $('*[data-gridpos="A1"]').trigger('click');
});
// custom jquery
jQuery(document).ready(function($) {
    $('.H8 > div').removeClass("circle");
    $('.G8 > div').removeClass("circle");
    $('.F8 > div').removeClass("circle");
    $('.E8 > div').removeClass("circle");
    $('.D8 > div').removeClass("circle");
    $('.C8 > div').removeClass("circle");
    $('.B8 > div').removeClass("circle");
    $('.A8 > div').removeClass("circle");    
    $('.A8 > div').removeClass("circle");
    $('.A7 > div').removeClass("circle");
    $('.A6 > div').removeClass("circle");
    $('.A5 > div').removeClass("circle");
    $('.A4 > div').removeClass("circle");
    $('.A3 > div').removeClass("circle");
    $('.A2 > div').removeClass("circle");
    $('.A1 > div').removeClass("circle");
});

// Add active class on hover to li > a

var btnContainer = document.getElementById("navbarSupportedContent");
// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("nav-link");
// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    // If there's no active class
    if (current.length > 0) {
      current[0].className = current[0].className.replace(" active", "");
    }
    // Add the active class to the current/clicked button
    this.className += " active";
  });
}

// END Add active class on hover to li > a

// show content of a link clicked
$(document).ready(function(){
    $("#navbarSupportedContent li a").click(function(){
        var varr = $(this).text().toLowerCase();
        // console.log(varr);
      $('#'+varr).addClass("sec_show");
      $('.sec_show').not('#'+varr).removeClass('sec_show');
    });
  });
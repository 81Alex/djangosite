function registered() {
    document.getElementById("reg").style.color = "red";
    alert("Hello from a static file!")
    return 'registrastion.html';//"/game"

$('.error-page').hide(0);

$('.login-button , .no-access').click(function(){
  $('.login').slideUp(500);
  $('.error-page').slideDown(1000);
});

$('.try-again').click(function(){
  $('.error-page').hide(0);
  $('.login').slideDown(1000);
});


}
$('input').on('change', function() {
  $('body').toggleClass('blue');
});

$(document).ready(function(){
	$("input").attr("required", true);
	$("textarea").attr("required", true);
	$("#id_img").attr("required", false);
	
	$("#id_text").attr("rows", '15');
	$('[data-toggle="tooltip"]').tooltip();

	$('html').on('touchstart', function(e) {
    $('#jstouch').removeClass('hover');


});
$('#jstouch').on("touchstart", function (e) {
	e.stopPropagation();
    "use strict"; //satisfy the code inspectors
    var link = $(this); //preselect the link
    if (link.hasClass('hover')) {
        return true;
    } 
    else {
        link.addClass("hover");
        $('#jstouch').not(this).removeClass("hover");
        e.preventDefault();

        return false; //extra, and to make sure the function has consistent return points
    }
});

	$(".profile").click(function () {
    	$("#modalprofile").modal("show");
  	});
  	$(".login").click(function () {
    	$("#modallogin").modal("show");
  	});
  	$(".signup").click(function () {
    	$("#modalsignup").modal("show");
  	});

    
    $('input[name=password2]').keyup(function () {
    'use strict';

    if ($('input[name=password1]').val() === $(this).val()) {
        $('#divCheckPasswordMatch').html('Le password coincidono');
        this.setCustomValidity('');
    } else {
        $('#divCheckPasswordMatch').html('Le password non coincidono!');
        this.setCustomValidity('Le password devono coincidere!');
    }
	});
    $("#id_username").keyup(function () {
    	'use strict';
      	var username = $(this).val();
      	$.ajax({
	        url: '/ajax/validate_username/',
	        data: {
	          'username': username
	        },
	        dataType: 'json',
	        success: function (data) {
	          	if (data.is_taken) {
	          		$("#divCheckUsername").html("Esiste gia' un utente con quel username!");
	          		$("#id_username")[0].setCustomValidity('Cambia nome!');
	          	}
	          	else{
	          		$("#divCheckUsername").html("");
	          		$("#id_username")[0].setCustomValidity('');
	          	}
        	}
      	});
    });


	//Navigation menu scrollTo
	$('header nav ul li a').click(function(event){
		event.preventDefault();
		var section = $(this).attr('href');
		var section_pos = $(section).position();

		if(section_pos){
			$(window).scrollTo({top:section_pos.top, left:'0px'}, 1000);
		}
		
	});

	$('.app_link').click(function(e){
		event.preventDefault();
		$(window).scrollTo({top:$("#hero").position().top, left:'0px'}, 1000);		
	});








	//Show & Hide menu on mobile
	$('.burger_icon').click(function(){
		$('header nav').toggleClass('show');
		$('header .burger_icon').toggleClass('active');
	});

	






	//wow.js on scroll animations initialization
	wow = new WOW(
	    {
		  animateClass: 'animated',
		  mobile: false,
		  offset: 50
		}
	);
	wow.init();








	//parallax effect initialization
	$('.hero').parallax("50%", 0.3);



	//parallax effect initialization
	$('.hero2').parallax("50%", 0.3);








});
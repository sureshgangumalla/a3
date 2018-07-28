var email_regex = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/); //regex from : https://stackoverflow.com/questions/46155/how-to-validate-an-email-address-in-javascript
var name_regex = new RegExp(/^[A-za-z0-9-\s]+/);
var phone_regex = new RegExp(/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im);
//var csrftoken = $("[name=csrfmiddlewaretoken]").val();
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
submitSignUpForm = function(e){
		var url = "home/";
		$.ajax({
           		type: "POST",
           		url: url,
           		data: $("#signup_form").serialize(),
           		success: function(data)
           		{
               			$("#container-div").html(data);
           		}
         	});
		e.preventDefault();
}
submitProfileForm = function(e){
		var url = "/profile/update_profile/";
		$.ajax({
           		type: "POST",
           		url: url,
           		data: $("#profile_form").serialize(),
           		success: function(data)
           		{
               			$("#container-div").html(data);
           		}
         	});
		e.preventDefault();	
}
/**
 *Custom methods for Tectum
 * */
loadprofile = function(userid){/*User id will be passed as null for static page*/
     console.log(userid)
    $("#container-div").load('profile.html');
}
loadapartment = function(userid){
    $("#container-div").load('apartment.html');
}
loadfeedback = function(userid){
    $("#container-div").load('feedback.html');
}
loadhome =function(userid){
    $("#container-div").load('home.html');
}
load_profile_edit =function(){
	console.log(csrftoken)
	$.ajax({
    url: '/profile/',
    type: 'post',
    data: {
    },
    headers: {
    	"X-CSRFToken": csrftoken,
    },
    //dataType: 'json',
    success: function (data) {
        $("#container-div").html(data);
    }
});
	//var param = {}
	//param['X-CSRFToken'] = csrftoken;
	//param.csrfmiddlewaretoken= csrftoken;
	//$.post('/profile/',param,function(msg){
	//	$("#container-div").html(msg);
	//});
  //  $("#container-div").load('profile-edit.html');     
}
load_sign_up = function(){
    window.location.href='signupStudent.html';
}
load_apartment_list = function(){
    $("#container-div").load('apartment_list.html');
}
toggleMealSelection = function(){
    var src = $("#meal");
    if(src.attr("src").indexOf("nv.svg") >=0){
            src.attr("src","/static/images/svg/veg.svg");
    } else {
        src.attr("src","/static/images/svg/nv.svg");
    }
}
toggleSmokeSelection = function(){
    var src = $("#smoke");
    if(src.attr("src").indexOf("ns.svg") >=0){
            src.attr("src","/static/images/svg/smoke.svg");
    } else {
        src.attr("src","/static/images/svg/ns.svg");
    }
}
toggleAlcoholSelection = function(){
    var src = $("#alcohol");
    if(src.attr("src").indexOf("na.svg") >=0){
            src.attr("src","/static/images/svg/drink.svg");
    } else {
        src.attr("src","/static/images/svg/na.svg");
    }
}
/*$('#feedbackform').bootstrapValidator({
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            Name: {
                validators: {
                    notEmpty: {
                        message: 'The Name is required and cannot be empty'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'The email address is required'
                    },
                    emailAddress: {
                        message: 'The email address is not valid'
                    }
                }
            },
            Message: {
                validators: {
                    notEmpty: {
                        message: 'The Message is required and cannot be empty'
                    }
                }
            }
        }
    });
*/

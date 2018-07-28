$(function(){

	$("#signup_form").validate({
		rules:{
			name : {
				required: true
			},
			email : {
				required: true,
				email: true
			},
			password : {
				required: true
			},
			cpassword : {
				required: true
			},
			dob : {
				required: true
			},
			country : {
				required: true
			}
		},
		messages:{
			name:{
				required : "Please Enter Name"
			},
			email:{
				email : "Please Enter valid email address"
			},
			password:{
				required : "Please Enter Passsword"
			},
			cpassword:{
				required : "Please Enter confirm Passsword"
			},
			dob : {
				required: "Please enter valid email address"
			},
			country : {
				required: "Please Enter Country Name"
			}
		}
	});

});

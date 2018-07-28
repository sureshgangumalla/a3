/**
Javascript file handles loading location. Default is set to USA. We use these details to show offers to customers.
Here it is shown as Newyork just to make sure it is working. Generally default location will be halifax. 
This is because this application will be based in application.
*/
var locality = 'New York';
var country = 'United States of America';
var country_short = 'US';
			
if ("geolocation" in navigator) {
 	navigator.geolocation.getCurrentPosition(function(position) {
  		var url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+position.coords.latitude+','+position.coords.longitude+'&sensor=true';
  		$.get(url,function(msg){
  			var address = msg.results[0].address_components;
  			$.each(address, function(i, item) {
				if(item.types[0] === 'locality'){
					locality = item.long_name;
					localStorage.setItem('city',locality);
				} else if(item.types[0] === 'country'){
					country = item.long_name;
					country_short = item.short_name;
					localStorage.setItem('country',country);
					setCountryDetails();
				}
			});
		});
	});
} else {
  	errorMessage();
}
setCountryDetails = function(){
	/*US- USA and CA --- Canada flags are stored as US.svg and CA.svg*/
	imageName = "image/"+country_short+".svg";
	$("#localeflag").attr("src",imageName);
	$("#local_name").text(country.substring(0,10));
}
errorMessage = function(){
	$("#message_panel").show(100);
	$("#highlight-text").text("Location Unavailable!");
	$("#warning-message").text(" We were not able to fetch the location. Please use Google Chrome or Firefox.");
}
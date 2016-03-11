$(document).ready(function(){

	$.ajax({
		url:'/productvariation/',
		type: 'GET',
		contentType: 'application/json;charset=UTF-8',
  		dataType: "json",
  		success: function(data){
  			$.each(data, function(index, value) {
  				console.log(index, value);
  			});
  		},
  		error: function(error){
  			console.log(error);
  		} 
	}) // end ajax

});
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


var getAddressInfo = function(addressId){
	// $username = 'u2';
	// $password = 'useruser';
	
	$.ajax({
		url:'/mailingaddress/' + addressId,
		type: 'GET',
		contentType: 'application/json;charset=UTF-8',
  		dataType: "json",
  		cache: false,
  		// beforeSend: function(xhr) {
  		// 	xhr.setRequestHeader("Authorization",
  		// 		"Basic " + btoa($username + ":" + $password));
  		// },
  		success: function(data){
  			// console.log(data);
  			$.each(data, function(index, value){
  				$('input[name=' + index + ']').val(value);
  				// console.log(index, value);
  			});
  		},
  		error: function(error){
  			console.log(error.status);
  			if(error.status==403) {
  				$('#loginModal').modal('show');    
  			}

  		} 
	}) // end ajax
}

function ConvertFormToJSON(form){
    var array = jQuery(form).serializeArray();
    var json = {};
    jQuery.each(array, function() {
        json[this.name] = this.value || '';
    });
    return json;
}

var updateAddressInfo = function(addressId){

	$username = 'u2';
	$password = 'useruser';
	
	var form = $('form');
	json = ConvertFormToJSON(form);
	data = JSON.stringify(json);
	console.log('data ', data);

	$.ajax({
		url:'/mailingaddress/' + addressId,
		type: 'PUT',
		contentType: 'application/json;charset=UTF-8',
  		dataType: "json",
  		cache: false,
  		data: data,
  		beforeSend: function(xhr) {
  			xhr.setRequestHeader("Authorization",
  				"Basic " + btoa($username + ":" + $password));
  		},
  		success: function(data){
  			console.log(data);
  			// $.each(data, function(index, value){
  			// 	$('form #' + index).val(value)
  			// 	console.log(index, value);
  			// });
  		},
  		error: function(error){
  			console.log(error);
  		} 
	}) // end ajax

}

$(document).on('click', '#submitBtn', function(event) {
	event.preventDefault();
	updateAddressInfo(4);
});// end onclick

$(document).ready(function(){
	getAddressInfo(4);
});

$(document).on('click','#loginSubmitBtn', function(event){
	event.preventDefault();
	var username = $('#id_username').val();
	var password = $('#id_password').val();
	console.log(username, password);

	function csrfSafeMethod(method) {
	    // these HTTP methods do not require CSRF protection
	    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	$.ajaxSetup({
	    beforeSend: function(xhr, settings) {
	        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
	            xhr.setRequestHeader("X-CSRFToken", csrftoken);
	        }
	    }
	});

	$.ajax({
		url: 'http://localhost:8000/login/',
		type: 'POST',
		data: JSON.stringify({'username': username, 'password': password}),
		contentType: 'application/json;charset=UTF-8',
		success: function(data){
			console.log('success: ');
			location.reload();
		},
		error: function(error) {
			console.log('error ', error);
		}

	})// end ajax
});
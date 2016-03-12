$(document).on('click', '.detailsBtn', function(event){
  event.preventDefault();
  alert('display details of...');
});

var insertUpperCarousel = function(products) {

	counter = 1;

	$.each(products, function(index, value) {

  		item = columnItem(
  			value.productimage_set[0].image, 
  			value.title, 
  			value.price,
        value.url
  			);

  		if (counter%3) {
  			carouselfRowHead += item;
  		} else {
  			carouselfRowHead += item;
  			$('#upperCarousel').append(carouselfRowHead + carouselfRowTail);
  			// resets template head and tail which are imported from template.js
  			carouselfRowHead = '<div class="item"><div class="row">';
			carouselfRowTail = '</div></div>';
  		}
		
		counter++;

	});

}

$(document).ready(function(){

	$.ajax({
		url:'/products/',
		type: 'GET',
		contentType: 'application/json;charset=UTF-8',
  		dataType: "json",
  		success: function(data){
  			insertUpperCarousel(data);
  		},
  		error: function(error){
  			console.log(error);
  		} 
	}) // end ajax

});
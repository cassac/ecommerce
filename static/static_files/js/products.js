$(document).on('click', '.detailsBtn', function(event){

  event.preventDefault();

  var detailUrl = $( this ).attr('href');

  $('#productDetailsModal').modal('show');

  var displayModal = function(details) {
    var images = details.productimage_set;
      $('#productDetailsModalLabel').text(details.title);
      $('#productDetailsModalMainImage').attr('src', images[0].image);

    $('#pictureDisplayThumbnails').clone();

    $.each(images, function(index, value) {
      console.log(index, value);
      imgElement = '<img style="padding-top:5px;max-width:50px;max-height:50px;"'+
      ' src="'+ value.image +'" alt="'+ details.title +'" class="center-block">';
      $('#pictureDisplayThumbnails').append(imgElement);
    })

  }

  $.ajax({
    url: detailUrl,
    type: 'GET',
    contentType: 'application/json;charset=UTF-8',
      dataType: "json",
      success: function(data){
        displayModal(data);
      },
      error: function(error){
        console.log(error);
      } 
  }) // end ajax

}); // end on click detailsBtn

$('#productDetailsModal').on('hidden.bs.modal', function(){
  // removes thumbnail images from previously opened product details modal
  $('#pictureDisplayThumbnails').empty();
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

	}); // end each

} // end insertUpperCarousel

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

}); // end document ready
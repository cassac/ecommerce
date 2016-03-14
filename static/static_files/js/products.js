var updateCart = function(variationId, quantity) {
  $.ajax({
    url: '/carts/item/' + variationId + '/?quantity=' + quantity,
    type: 'PUT',
    contentType: 'application/json;charset=UTF-8',
      dataType: 'json',
      success: function(data){
        console.log(data);
        return data;
      },
      error: function(error){
        console.log(error);
      } 
  }) // end ajax

}

$(document).on('click', '.removeCartItemBtn', function(event) {
  p = $( this ).closest('li');
  variationId = p.find('.variationTitle').data('variation-id');
  quantity = p.find('.cartItemQuantity').data('cart-item-quantity');

  updateCart(variationId, quantity);

  p.remove();

});

var displayCart = function(cart) {

  $('#cartSubtotal').text(cart.get_subtotal);
  $('.dropdown-cart .cart-product-list-items').remove();
  list = generateCartItems(cart.cartitems);
  $('.dropdown-cart').prepend(list);

}

$(function() {
    $('.dropdown.keep-open').on({
        "shown.bs.dropdown": function() {
            $(this).data('closable', false);
        },
        "click": function(event) {
            $(this).data('closable', false);
        },
        "hide.bs.dropdown": function(event) {
            temp = $(this).data('closable');
            $(this).data('closable', true);
            return temp;
        }
    });
});

$(document).on('mouseleave mouseenter', '#navBarCart', function(event) {
  var dropdown = $('.keep-open');
  dropdown.toggleClass('open');
  if ( dropdown.data('closable') ) {
    dropdown.data('closable', false);
  } else {
    dropdown.data('closable', true);
  }

  $.ajax({
    url: '/carts/',
    type: 'GET',
    contentType: 'application/json;charset=UTF-8',
      dataType: 'json',
      success: function(data){
        // console.log(data);s
        displayCart(data);
      },
      error: function(error){
        console.log(error);
      } 
  }) // end ajax

});


$(document).on('click', '.addToCartBtn', function(event) {

  var quantity = $("input[type='number'][name='quantity']").val();
  var variationId = $('.product-variations option:selected').val();
  
  updateCart(variationId, quantity);

}); // end on click addToCartBtn

$(document).on('click', '.detailsBtn', function(event) {

  event.preventDefault();

  var detailUrl = $( this ).find('a').attr('href');

  $('#productDetailsModal').modal('show');

  var displayModal = function(details) {
    var variationsArray = details.productvariation_set;
    var images = details.productimages;
    $('#productDetailsModalLabel').text(details.title);
    $('#productDetailsModalMainImage').attr('src', images[0].image);
    $('.product-desc').text(details.description);
    $('.product-title').text(details.title);
    $('.product-price').text(details.price);

    $.each(images, function(index, value) {
      imgElement = '<img style="padding-top:5px;max-width:50px;max-height:50px;"'+
      ' src="'+ value.image +'" alt="'+ details.title +'" class="center-block">';
      $('#pictureDisplayThumbnails').append(imgElement);
    });

    var selectMenu = generateVariationsMenu(variationsArray);
    $('.product-variations').append(selectMenu);

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
  // removes variations menu from ...
  $('.product-variations').empty();
  // resets product quantity to default value of 1
  $("input[type='number'][name='quantity']").val('1');
});

var insertUpperCarousel = function(products) {

	counter = 1;

	$.each(products, function(index, value) {

  		item = columnItem(
  			value.productimages[0].image, 
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
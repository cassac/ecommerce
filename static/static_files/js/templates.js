var generateCartItems = function(cartItems) {

    cartItemList = '';

    $.each(cartItems, function(index, value) {

        cartItem = '<li class="cart-product-list-items">' +
                    '<span class="item">' +
                        '<span class="item-left">' +
                            '<img src="'+ value.variation[0].image + '" alt="" />' +
                            '<span class="item-info">' +
                                '<span>' + 'value.title' + '</span>' +
                                '<span>' + 'value.price' + '</span>' +
                            '</span>' +
                        '</span>' +
                        '<span class="item-right">' +
                            '<button class="btn btn-xs btn-danger pull-right">x</button>' +
                        '</span>' +
                    '</span>' +
                '</li>';

        cartItemList += cartItem;

    });

    return cartItemList;
}

carouselfRowHead = '<div class="item active"><div class="row">';
carouselfRowTail = '</div></div>';

var generateVariationsMenu = function(variationsArray) {
    menuHead = '<select class="form-control">';
    menuTail = '</select>';
    $.each(variationsArray, function(index, value) {
        menuHead += '<option value="' + value.id + '">' + value.title + '</option>';
    });
    return menuHead + menuTail;
}

var columnItem = function(imageUrl, title, price, detailsUrl){

	item = '<div class="col-sm-3">'+
                    '<div class="col-item">'+
                                '<div class="photo">' +
                                    '<img src="'+ imageUrl +'" class="img-responsive" alt="a" />' +
                                '</div>' +
                                '<div class="info">' +
                                    '<div class="row">' +
                                        '<div class="price col-md-6">' +
                                            '<h5 id="productTitle">' +
                                                title +
                                            '</h5>' +
                                            '<h5 class="price-text-color">' +
                                                price +
                                            '</h5>' +
                                        '</div>' +
                                        '<div class="rating hidden-sm col-md-6">' +
                                            '<i class="price-text-color fa fa-star"></i><i class="price-text-color fa fa-star">' +
                                            '</i><i class="price-text-color fa fa-star"></i><i class="price-text-color fa fa-star">' +
                                            '</i><i class="fa fa-star"></i>' +
                                        '</div>' +
                                    '</div>' +
                                    '<div class="separator clear-left">' +
                                        '<p class="btn-add addToCartBtn">' +
                                            '<i class="fa fa-shopping-cart"></i><a href="'+ '#' +'" class="hidden-sm">Add to cart</a></p>' +
                                        '<p class="btn-details detailsBtn">' +
                                            '<i class="fa fa-list"></i><a href="'+ detailsUrl +'" class="hidden-sm">More details</a></p>' +
                                    '</div>' +
                                    '<div class="clearfix">' +
                                    '</div>' +
                                '</div>' +
                            '</div>' +
                        '</div>';
    return item;
}
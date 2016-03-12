carouselfRowHead = '<div class="item active"><div class="row">';
carouselfRowTail = '</div></div>';

var columnItem = function(imageUrl, title, price){
	item = '<div class="col-sm-3">'+
                    '<div class="col-item">'+
                                '<div class="photo">' +
                                    '<img src="'+ imageUrl +'" class="img-responsive" alt="a" />' +
                                '</div>' +
                                '<div class="info">' +
                                    '<div class="row">' +
                                        '<div class="price col-md-6">' +
                                            '<h5>' +
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
                                        '<p class="btn-add">' +
                                            '<i class="fa fa-shopping-cart"></i><a href="http://www.jquery2dotnet.com" class="hidden-sm">Add to cart</a></p>' +
                                        '<p class="btn-details">' +
                                            '<i class="fa fa-list"></i><a href="http://www.jquery2dotnet.com" class="hidden-sm">More details</a></p>' +
                                    '</div>' +
                                    '<div class="clearfix">' +
                                    '</div>' +
                                '</div>' +
                            '</div>' +
                        '</div>';
    return item;
}
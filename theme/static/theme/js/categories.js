(function($){
  "use strict";
   $('#myInventoryCarousel').carousel({
    interval: 10000
  });

    // Control buttons
  $('#nextInventory.next').click(function () {
    $('#myInventoryCarousel.carousel').carousel('next');
    return false;
  });
  $('#prevInventory.prev').click(function () {
    $('#myInventoryCarousel.carousel').carousel('prev');
    return false;
  });

  // On carousel scroll
  $("#myInventoryCarousel").on("slide.bs.carousel", function (e) {
    var $e = $(e.relatedTarget);
    var itemIndex = $e.index();
    var itemsPerSlide = 4;
    var totalItems = $(".carousel-item").length;
    if (itemIndex >= totalItems - (itemsPerSlide - 1)) {
      var it = itemsPerSlide -
          (totalItems - itemIndex);
      for (var i = 0; i < it; i++) {
        // append slides to end
        if (e.direction === "left") {
          $(".carousel-item").eq(i).appendTo(".carousel-inner");
        } else {
          $(".carousel-item").eq(0).appendTo(".carousel-inner");
        }
      }
    }
  });
})
(jQuery);





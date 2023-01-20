$(document).ready(function () {
  // wishlist

  $(".add_to_wish_list_btn").click(function (e) {
    e.preventDefault(e);

    var product_id = $(this).closest(".all_product").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: "/add-wish-item/",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        alertify.success(response.status);
      }
    });
  });


$(document).on('click', '.del-wish-item',function (e) {
    e.preventDefault(e);

    var product_id = $(this).closest(".wish-products").find(".prod_id").val();

    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(product_id);
    $.ajax({
      type: "POST",
      url: "/del-wish-item/",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
        $(".wish-data").load(location.href + " .wish-data");
      },
    });
  });
});

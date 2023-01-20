$(document).ready(function () {
  // increament items
  $(".increment_btn").click(function (e) {
    e.preventDefault();

    var inc_value = $(this).closest(".product_data").find(".qty_input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product_data").find(".qty_input").val(value);
    }
  });

  // decrement items
  $(".decrement_btn").click(function (e) {
    e.preventDefault();

    var inc_value = $(this).closest(".product_data").find(".qty_input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 0) {
      value--;
      $(this).closest(".product_data").find(".qty_input").val(value);
    }
  });

  $(".addToCartBtn").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".all_product").find(".prod_id").val();
    var product_qty = $(this).closest(".all_product").find(".qty_input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: "/add-to-cart/",
      // dataType: "JSON",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });

  $(".changeQty").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".cart_product").find(".prod_id").val();
    var product_qty = $(this).closest(".cart_product").find(".qty_input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    console.log(product_id);
    console.log(product_qty);

    $.ajax({
      type: "POST",
      url: "/update-cart/",
      // dataType: "JSON",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });

  $(".del-cart-item").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".cart_product").find(".prod_id").val();
    console.log(product_id);

    var token = $("input[name=csrfmiddlewaretoken]").val();

        $.ajax({
      type: "POST",
      url: "/delete-cart-item/",
      // dataType: "JSON",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        console.log(response);
        $('.cart-data').load(location.href + " .cart-data");
      },
    });


  });







});

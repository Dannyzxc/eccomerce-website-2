$(document).ready(function () {
          $(".payrazerpay").click(function (e) {
                    e.preventDefault();
                    var firstname = $("[name='firstname']").val();
                    var lastname = $("[name='lastname']").val();
                    var phone = $("[name='phone']").val();
                    var email = $("[name='email']").val();
                    var address = $("[name='address']").val();
                    var state = $("[name='state']").val();
                    var city = $("[name='city']").val();
                    var token = $("[name = 'csrfmiddlewaretoken']").val();


                    if (
                              firstname == "" ||
                              lastname == "" ||
                              phone == "" ||
                              email == "" ||
                              address == "" ||
                              state == "" ||
                              city == ""
                    ) {

                              swal("alert!", "all fields are mandatary", "error");
                              return false;
                    } else {

                              $.ajax({
                                        type: "GET",
                                        url: "/proceeded-to-pay/",
                                        success: function (response) {
                                                  var options = {
                                                            key: "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
                                                            amount: response.cart_total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                                                            currency: "INR",
                                                            name: "Acme Corp",
                                                            description: "Test Transaction",
                                                            image: "https://example.com/your_logo",
                                                            order_id: "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                                                            handler: function (responsees) {
                                                                      alert(responsees.razorpay_payment_id);
                                                                      alert(responsees.razorpay_order_id);
                                                                      alert(responsees.razorpay_signature);

                                                                      data = {
                                                                                "firstname": firstname,
                                                                                "lastname": lastname,
                                                                                "phone": phone,
                                                                                "email": email,
                                                                                "address": address,
                                                                                "state": state,
                                                                                "city": city,
                                                                                "payment_mode": "paid by Razorpay",
                                                                                "payment_id": responsees.razorpay_payment_id,
                                                                                csrfmiddlewaretoken: token
                                                                      }
                                                                      $.ajax({
                                                                                method: "POST",
                                                                                url: "placeholder/",
                                                                                data: data,
                                                                                dataType: "dataType",
                                                                                success: function (responsed) {
                                                                                          swal("congrates!", responsed.status, "success").then((value) => {
                                                                                                    window.location.href = '/my-orders'
                                                                                          });
                                                                                          
                                                                                }
                                                                      });
                                                            },
                                                            prefill: {
                                                                      name: firstname + " " + lastname,
                                                                      email: email,
                                                                      contact: phone,
                                                            },

                                                            theme: {
                                                                      color: "#3399cc",
                                                            },
                                                  };
                                                  var rzp1 = new Razorpay(options);
                                                  // rzp1.on('payment.failed', function (response){
                                                  // alert(response.error.code);
                                                  // alert(response.error.description);
                                                  // alert(response.error.source);
                                                  // alert(response.error.step);
                                                  // alert(response.error.reason);
                                                  // alert(response.error.metadata.order_id);
                                                  // alert(response.error.metadata.payment_id);
                                                  // });

                                                  rzp1.open();
                                        }
                              });





                    }
          });
});

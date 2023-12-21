console.log("Working well");

$("#commentForm").submit(function(e) {
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(response) {
            console.log("Review Saved to db...");

            if (response.bool == true) {
                $("#review-notification").html("Review Added successfully")
                $(".hide-comment-form").hide()
                $(".hide-review").hide()

                let _html = '<div class="d-flex">'
                    _html +='<img src="{% static "img/avatar.jpg" %}" class="img-fluid rounded-circle p-3" style="width: 100px; height: 100px;" alt="">'

                    _html +='<div class="">'
                    _html +='<p class="mb-2" style="font-size: 14px;">{{review.date|date:"d, M, Y"}}</p>'

                    _html +='<div class="d-flex justify-content-between">'
                    _html +='<h5>'+ response.context.user +'</h5>'

                    
                    // _html +='<div class="d-flex mb-3">'
                    for (let i = 1; i <= review.context.rating; i++) {
                        _html += '<i class="fa fa-star text-secondary"></i>'
                    }
                    // _html +='</div>'

                    _html +='</div>'

                    _html +='<p>'+ response.context.review +' </p>'
                    _html +='</div>'

                    _html +='</div>'

                    $(".comment-list").prepend(_html)
            }

            
        }
    })
})
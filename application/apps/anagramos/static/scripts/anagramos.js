$("#anagramos_post_form").submit(function (event) {
    event.preventDefault(); //prevent default action
    let post_url = $(this).attr("action"); //get form action url
    let form_data = $(this).serialize(); //Encode form elements for submission
    let anagramos_results = $(".anagramos-results");
    let anagramos_results_wrapper = $(".anagramos-results-wrapper");
    $.post(post_url, form_data)
        .done(function (response) {
            if (anagramos_results_wrapper.hasClass("hidden")) {
                anagramos_results_wrapper.toggleClass("hidden");
            }
            let word = $("#word-box").val();
            let anagramos_result_list = $(".anagramos-results-list");
            anagramos_result_list.html("");
            anagramos_result_list.prepend("<h3>Anagrames de : " + word + "</h3>");

            if (response.results.length === 0) {
                anagramos_results.html("<h3> No anagrammes for word : " + word + "</h3>");
            } else {
                $.each(response.results, function (i, result) {//iterate over json data
                    let results_html = '<div class="anagramos-result-wrapper">' +
                        '<p>' + result + ' </p>' +
                        '</div>';
                    $(".anagramos-results-list").append(results_html);
                });
            }

        })
        .fail(function () {
            if (anagramos_results_wrapper.hasClass("hidden")) {
                anagramos_results_wrapper.toggleClass("hidden");
            }
            anagramos_results.text("Error: Could not contact server");
        });
});

function displayResults() {
    $(".anagramos-results-wrapper").toggleClass("hidden");
}
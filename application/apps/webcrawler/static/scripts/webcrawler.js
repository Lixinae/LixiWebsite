$("#webcrawler_post_form").submit(function (event) {
    event.preventDefault(); //prevent default action
    let post_url = $(this).attr("action"); //get form action url
    let form_data = $(this).serialize(); //Encode form elements for submission
    let webcrawler_results = $(".webcrawler-results");
    $.post(post_url, form_data)
        .done(function (response) {
            webcrawler_results.toggleClass("hidden");
            // Si l'on a pas de resultats -> rien n'a été trouvé, on affiche donc un message d'erreir
            let url = $("#url-box").val();
            if (Object.keys(response.results).length === 0) {
                // Todo -> eventuellement rendre lien cliquable -> Rajouter un a href ne marche pas direct pour whatever reason
                webcrawler_results.html("<p> No file were found on link : " + url + "</p>");
            } else {
                // Reset de la liste
                $(".webcrawler-results-list").html("");
                $.each(response.results, function (i, result) {
                    let results_html = '<div class="webcrawler-result-wrapper">' +
                        '<a href=' + result.url + '>' + result.name + '</a>' +
                        '</div>';
                    $(".webcrawler-results-list").append(results_html);
                });
            }
        })
        .fail(function () {
            webcrawler_results.toggleClass("hidden");
            webcrawler_results.text("Error: Could not contact server");
        });
});

function displayResults() {
    // $(".webcrawler-result-wrapper").toggleClass("isCollapsed");
    // $(".webcrawler-result-wrapper").toggleClass("hidden");
    // Todo -> Faire une animation d'apparition et pas juste un spawn
    $(".webcrawler-results-list").toggleClass("hidden");
    // var hidden = true;
    // $(".webcrawler-results-list")
    //     .css("display", "flex")
    //     .hide()
    //     .fadeIn();

    $(".webcrawler-results-form").toggleClass("hidden");
    // $(".webcrawler-results-form").css("display", "block")
    //     .hide()
    //     .fadeIn();

}

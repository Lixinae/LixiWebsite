/**
 * Methode post sur le formulaire du string to leet
 **/
$("#string_to_leet_post_form").submit(function (event) {
    event.preventDefault(); //prevent default action
    let post_url = $(this).attr("action"); //get form action url
    let form_data = $(this).serialize(); //Encode form elements for submission
    let stringToLeetResult = $(".stringToLeet-results");
    let stringToLeetWrapper = $(".stringToLeet-results-wrapper");
    /* Lancement de la methode post */
    $.post(post_url, form_data)
        /* Si le serveur renvoie une réponse */
        .done(function (response) {
            if (stringToLeetWrapper.hasClass("hidden")) {
                stringToLeetWrapper.toggleClass("hidden");
            }
            let word = $("#word-box").val();
            stringToLeetResult.html("");
            stringToLeetResult.prepend("<h3> String to leet result </h3>");
            let results_html = '<div class="stringToLeet-result-wrapper">' +
                '<p> Original : ' + word + ' </p>' +
                '<p> Traduction :' + response.results + ' </p>' +
                '</div>';
            stringToLeetResult.append(results_html);
        })
        /* En cas d'erreur */
        .fail(function () {
            if (stringToLeetWrapper.hasClass("hidden")) {
                stringToLeetWrapper.toggleClass("hidden");
            }
            stringToLeetResult.text("Error: Could not contact server");
        });
});

function displayResults() {
    $(".stringToLeet-results-wrapper").toggleClass("hidden");
}
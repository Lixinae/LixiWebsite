// N'utiliser qu'une seul vue par fichier, éviter les Vue multiple
const vuePendu = new Vue({
    el: '#pendu_post_form',
    data: {
        letter: '',
        response_numb_attempts_left:8,
        response_is_letter_ok: false,
        response_already_tried_letters: [],
        show_results: false,
        request_done: false
    },
    methods: {
        postData: function () {
            let url = $(this.el).attr("action"); //get form action url
            let self = this; // Permet d'utiliser le this de la Vue
            axios.get(url, {letter: this.letter})
                .then(function (response) {
                    // Attention au this ici -> Le this ici est celui de Axios et pas de l'objet Vue
                    self.response_numb_attempts_left = response.data.numb_attempts_left;
                    self.response_is_letter_ok = response.data.is_letter_ok;
                    self.response_already_tried_letters = response.data.already_tried_letters;
                    self.show_results = true;
                    self.request_done = true;
                })
                .catch(error => {
                    console.log(error)
                });
        }
    },
    delimiters: ["<%", "%>"]
});
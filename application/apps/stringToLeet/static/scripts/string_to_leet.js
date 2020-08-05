// N'utiliser qu'une seul vue par fichier, éviter les Vue multiple
const vueStringToLeet = new Vue({
    el: '#string_to_leet_post_form_wrapper',
    data: {
        phrase: '',
        response_data: [],
        data_history: [],
        show_results: false,
        request_done: false
    },
    methods: {
        postData: function () {
            console.log({phrase: this.phrase});
            let post_url = $("#string_to_leet_post_form").attr("action"); //get form action url
            let self = this; // Permet d'utiliser le this de la Vue
            axios.post(post_url, {phrase: this.phrase})
                .then(function (response) {
                    // Attention au this ici -> Le this ici est celui de Axios et pas de l'objet Vue
                    self.response_data = response.data.results;
                    self.show_results = true;
                    self.request_done = true;
                    self.data_history.push({
                        original: self.phrase,
                        translation: response.data.results
                    });
                    //console.log(self.data_history);
                })
                .catch(error => {
                    console.log(error)
                });
            //console.log(this.data_history)
        }
    },
    delimiters: ["<%", "%>"],
    mounted() {
        if (localStorage.phrase) {
            this.phrase = localStorage.phrase;
        }
        if (localStorage.data_history) {
            console.log("Mounted");
            console.log(localStorage.data_history);
            localStorage.clear();
            this.data_history = Object.keys(localStorage.data_history).filter(key => localStorage.data_history[key]);
        }
    },
    watch: {
        phrase(newPhrase) {
            localStorage.phrase = newPhrase;
        },
        data_history(newDataHistory) {
            //console.log("Hello");
            //console.log(newDataHistory);
            //localStorage.clear();
            //localStorage.data_history = Object.keys(newDataHistory).filter(key => newDataHistory[key]);
            //localStorage.data_history = []
        }
    }
});
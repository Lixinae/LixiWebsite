// N'utiliser qu'une seul vue par fichier, éviter les Vue multiple
const vuePortfolio = new Vue({
    el: '#github_data_display',
    data: {
        chart: "",
        language_colors: {
            "Python": "#3572A5",
            "C++": "#F34B7D",
            "C#": "#37862B",
            "Java": "#B47926",
            "C": "#626465",
            "JavaScript": "#F1E05A",
            "HTML": "#E34C26",
            "CSS": "#563D7C"
        }
    },
    methods: {
        grabGithubData: function () {
            let self = this
            axios.get(`https://api.github.com/users/Vahen/repos`)
                .then(function (response) {
                    console.log(response.data)
                    self.extract_and_display_data_pie_chart(response.data)
                })
        },
        extract_and_display_data_pie_chart(github_repos_data) {

            let dict_language = {}
            github_repos_data.forEach(data => {
                if (!(data.language in dict_language)) {
                    dict_language[data.language] = 1
                } else {
                    dict_language[data.language] += 1
                }
            });
            let labels = [];
            let colors = [];
            let count_language = []
            for (const [key, value] of Object.entries(dict_language)) {
                labels.push(key)
                count_language.push(value)
                colors.push(this.language_colors[key])
            }
            this.display_pie_chart(labels, count_language, colors);
        },
        display_pie_chart(labels, count_language, colors) {
            console.log(labels)
            console.log(count_language)
            console.log(colors)
            const ctx = $('#github_language_chart_pie').get(0).getContext('2d');
            if (this.chart) {
                this.chart.destroy()
            }
            this.chart = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Language",
                        backgroundColor: colors,
                        data: count_language,
                    }]
                },
                options: options_pie_chart
            });
        },
    },
    mounted() {
        this.grabGithubData()
    },
    delimiters: ["<%", "%>"]
});

Chart.defaults.global.defaultFontColor = 'black';
Chart.defaults.global.defaultFontSize = 16;

const options_pie_chart = {
    title: {
        display: true,
        text: 'Languages utilisé sur mes repository github',
        position: 'top',
    },
    responsive: true,
}
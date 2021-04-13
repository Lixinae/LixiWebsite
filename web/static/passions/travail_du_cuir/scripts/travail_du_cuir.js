const vueTravailDuCuir = new Vue({
    el: '#tdc_app',
    vuetify: new Vuetify(),
    components: {},
    data: {
        images_galeries: [
            // Todo -> Tester déjà avec les données sur les canons
            //  Realiser toute la partie H

            // La structure de données est très similaire à celle d'instagram, en une version beaucoup plus light et simple
            {
                "name": "Canons",
                "sub_galery_url": Flask.url_for("travail_du_cuir_bp.travail_du_cuir_canons"),
                "items": [
                    {
                        "name": "D20",
                        "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/D20_1.jpg"}),// Proviens du package JsGlue,
                        "sub_galery": [
                            {
                                "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/D20_1.jpg"})
                            },
                            {
                                "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/D20_2.jpg"})
                            },
                        ]
                    },
                    {
                        "name": "Haches",
                        "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/Hache_1.jpg"}),// Proviens du package JsGlue,
                        "sub_galery": [
                            {
                                "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/Hache_1.jpg"})
                            },
                            {
                                "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/Hache_2.jpg"})
                            },
                        ]
                    },
                ]
            },
            {
                "name": "Accesoires",
                "sub_galery_url": Flask.url_for("travail_du_cuir_bp.travail_du_cuir_accessoires"),
                "items": [
                    {
                        "name": "porte_bouteille",
                        "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/accessoires/porte_bouteille_1.jpg"}),// Proviens du package JsGlue,
                        "sub_galery": [
                            {
                                "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/porte_bouteille_1.jpg"})
                            },
                            {
                                "src": Flask.url_for("travail_du_cuir_bp.static", {"filename": "img/canons/porte_bouteille_2.jpg"})
                            },
                        ]
                    }
                ]
            },
            // {
            //     "name": "bracelets",
            //     "items": [
            //         {
            //             "src": ""
            //         }
            //     ]
            // },
            // {
            //     "name": "motifs",
            //     "items": [
            //         {
            //             "src": ""
            //         }
            //     ]
            // },
        ]






        // instafeed: null
        // Forme de instafeed :
        // [{
        //      url_img: "",
        //      sub_imgs = [] // -> Liste d'url à afficher
        //      } ]
    },
    methods: {
        getInsta() {
            console.log("Hello insta")
            // Todo -> Déplacer le call à l'api dans une api dédié sur le serveur pour éviter un call à chaque fois
            // Le serveur va appeler l'api, extraire les info necessaire, les stocker en BDD
            // Comme ça l'appel à l'api ne se fera que tous les x temps, au lieu de chaque appel
            // Cette methode ne fera que récupérer les info stocker en BDD de ce qu'on a récupérer de l'api

            // const options = {
            //     method: 'GET',
            //     url: 'https://instagram28.p.rapidapi.com/medias',
            //     params: {
            //         user_id: '37207057024',
            //         batch_size: '20'
            //     },
            //     headers: {
            //         'x-rapidapi-key': '2dcecc0291msh881b9c68ba412b4p1b00b7jsn1b24ab4f5cf8',
            //         'x-rapidapi-host': 'instagram28.p.rapidapi.com'
            //     }
            // };
            //
            // axios.request(options).then(function (response) {
            //     // edge_owner_to_timeline_media -> tableau avec toutes les info possible sur les post
            //     // Chaque élement du tableau a un "display_url" (pour l'image de base)
            //     // Et aussi "edge_sidecar_to_children" -> tableau des photos de la publication
            //
            //     // Il faudra itérer sur chaque "edge" de "response.data.data.user.edge_owner_to_timeline_media"
            //     // Recup l'url d'affichage
            //     // Puis sur chaque "edge_sidecar_to_children" de chaque "edge" -> recup l'url d'affichage
            //     //
            //     console.log(response.data.data.user.edge_owner_to_timeline_media);
            // }).catch(function (error) {
            //     console.error(error);
            // });
        },
    },
    created() {
        this.getInsta();
    },
    delimiters: ["<%", "%>"]
})

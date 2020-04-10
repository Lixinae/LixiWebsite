from flask import render_template, make_response

from application.passions import passions_bp, data


############################################
#                 Passion                  #
############################################

@passions_bp.route('/')
def passions():
    passions_list = data.passions()
    return make_response(render_template('passions.html', title="Passions", passionsList=passions_list), 200)


@passions_bp.route('/GN')
def passions_gn():
    return make_response(render_template('./passions/gn.html', title="GN"), 200)


@passions_bp.route('/TravailDuCuir')
def passions_travail_du_cuir():
    return make_response(render_template('./passions/travailDuCuir.html', title="Travail du cuir"), 200)


@passions_bp.route('/JeuxDeSociete')
def passions_jeux_de_societe():
    return make_response(render_template('./passions/jeuxDeSociete.html', title="Jeux de sociéte"), 200)


@passions_bp.route('/JeuxDeRole')
def passions_jeux_de_role():
    return make_response(render_template('./passions/jeuxDeRole.html', title="Jeux de rôle"), 200)


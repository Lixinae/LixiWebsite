from flask import render_template, make_response

from application.skillsPassion import skills_passion_bp


############################################
#             Skills Passion               #
############################################

@skills_passion_bp.route('/skillsPassion')
def skills_passion():
    return make_response(render_template('skillsPassion.html', title="skillsPassion"), 200)


@skills_passion_bp.route('/skillsPassion/GN')
def skills_passion_gn():
    return make_response(render_template('./skillsPassion/gn.html', title="GN"), 200)


@skills_passion_bp.route('/skillsPassion/TravailDuCuir')
def skills_passion_travail_du_cuir():
    return make_response(render_template('./skillsPassion/travailDuCuir.html', title="Travail du cuir"), 200)


@skills_passion_bp.route('/skillsPassion/JeuxDeSociete')
def skills_passion_jeux_de_societe():
    return make_response(render_template('./skillsPassion/jeuxDeSociete.html', title="Jeux de sociéte"), 200)


@skills_passion_bp.route('/skillsPassion/JeuxDeRole')
def skills_passion_jeux_de_role():
    return make_response(render_template('./skillsPassion/jeuxDeRole.html', title="Jeux de rôle"), 200)


@skills_passion_bp.route('/skillsPassion/serveurMultimedia')
def skills_passion_serveur_multimedia():
    return make_response(render_template('./skillsPassion/serveurMultimedia.html', title="Serveur multimedia"), 200)

from flask_assets import Bundle


def create_static_js_bundles(assets):
    libs_js_folder = "general/scripts/libs/"
    bundles = {
        'libs_js': Bundle(
            libs_js_folder + 'jquery-3.4.1.min.js',
            libs_js_folder + 'bootstrap_4_1_0.js',
            libs_js_folder + 'popper_min_js_1_14_0.js',
            output='generated/libs.js',
            filters='jsmin'),
    }
    assets.register(bundles)


def create_static_css_bundles(assets):
    bundles = {
        'home_css': Bundle(
            'general/css/libs/bootstrap_4.0.0_min.css',
            'general/css/style.scss',
            output='generated/home.css',
            filters='pyscss'),
    }
    assets.register(bundles)


def create_static_bundles_assets(assets):
    """
    Create the bundles assets
    :param assets: The assets included in the project
    """
    create_static_js_bundles(assets)
    create_static_css_bundles(assets)

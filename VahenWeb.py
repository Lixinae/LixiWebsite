from application import create_app
from application.configuration import DevelopmentConfig

if __name__ == '__main__':
    app = create_app(DevelopmentConfig)
    app.run(host="0.0.0.0")

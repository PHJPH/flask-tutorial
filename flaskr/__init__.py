import os

from flask import Flask

def create_app(test_config=None):
    # Cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Carrega a instância de config, se ela existir, quando não for testada
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Carrega test_config se já tiver configuração definida
        app.config.from_mapping(test_config)

    # Garante que a pasta da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Uma página simples que diz 'Hello'
    @app.route('/')
    def hello():
        return 'Hello World'

    return app
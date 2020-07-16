from flask import Flask
from delivery.ext import site
from delivery.ext import toolbar
from delivery.ext import config
#from delivery.ext import admin

# aqui dentro inicializa-se as extensões contidas na pasta ext.
# o toolbar deve ser inicializado antes do site, para renderizar o restante da aplicacao
# configuracoes sao colocadas aqui

def create_app():
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    #admin.init_app(app)
    return app
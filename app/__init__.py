from flask import Flask
# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# import Migrate
from flask_migrate import Migrate

# import libraries for grabbing environment variables
from dotenv import load_dotenv
# used to read environment variables
import os

# gives us access to datsbase operations
db = SQLAlchemy()
migrate = Migrate()
# load the values from our .env file so the os module can use them
load_dotenv()

def create_app(test_config = None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    # lol i dont think this is correct
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set up the database
    if not test_config:
        # development environment configuration
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        # test environment configuration
        # if there is a test_config passed in, this means
        # we're tyring to test the app,
        # configure the test settings
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

    # connect the db and migrate to our flask app
    db.init_app(app)
    migrate.init_app(app,db)

    # import routes
    from .routes import crystal_bp, healer_bp

    # register the blueprint
    app.register_blueprint(crystal_bp)
    app.register_blueprint(healer_bp)
    
    from app.models.crystal import Crystal
    from app.models.healer import Healer
    

    return app
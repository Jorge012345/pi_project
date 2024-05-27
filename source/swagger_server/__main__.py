import connexion
from swagger_server import encoder

# from swagger_server.repository.base_repo import BaseRepo

# from utilities.helpers import return_status
from utilities.helpers import *
from swagger_server.repository.base_repo import db
from utilities.settings import Settings


def main():
    app = connexion.App(
        __name__,
        specification_dir="./swagger/",
        options={"swagger_ui": False},
    )
    app.app.json_provider_class = encoder.JSONEncoder
    app.app.url_map.strict_slashes = False
    app.add_api("swagger.yaml", base_path="/character", strict_validation=True)

    # # BaseRepo.create_connection()
    # app.route("/")(return_status)
    # return app
    Settings.init()

    # Configurar la base de datos
    app.app.config["SQLALCHEMY_DATABASE_URI"] = Settings.ConnectionStringLocal
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app.app)

    with app.app.app_context():
        db.create_all()  # Crear la base de datos y las tablas

    return app


# *********** EXECUTION
if __name__ == "__main__":
    create_app = main()
    create_app.run(8080)

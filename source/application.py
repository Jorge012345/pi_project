import connexion
from swagger_server import encoder
from swagger_server.repository.base_repo import db, BaseRepo
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

    Settings.init()

    # Configurar la base de datos
    app.app.config["SQLALCHEMY_DATABASE_URI"] = Settings.ConnectionStringLocal
    app.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app.app)

    with app.app.app_context():
        db.create_all()  # Crea la base de datos y las tablas si no existen

        # Verifica la conexión a la base de datos
        if not BaseRepo.create_connection():
            print("La conexión a la base de datos ha fallado.")
            return None

    return app


# *********** EJECUCIÓN
if __name__ == "__main__":
    create_app = main()
    if create_app:
        create_app.run(port=8080)
    else:
        print(
            "La aplicación no puede iniciar debido a un fallo en la conexión con la base de datos."
        )

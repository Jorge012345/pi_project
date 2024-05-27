# en base_repo.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseRepo:
    @classmethod
    def create_connection(cls):
        try:
            # Intenta hacer una operación simple para chequear la conexión
            db.session.execute("SELECT 1")
            return True
        except Exception as e:
            print("ERROR: No se pudo conectar a la instancia de MySQL.")
            print(e)
            return False

    @classmethod
    def reconnect(cls):
        try:
            db.session.close()  # Cierra la sesión actual
            db.session.execute(
                "SELECT 1"
            )  # Intenta hacer un nuevo ping a la base de datos
            return True
        except Exception as e:
            print("Intento de reconexión fallido.")
            print(e)
            return False

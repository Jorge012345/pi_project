from swagger_server.repository.base_repo import db
from swagger_server.models.character import Character


class CharacterRepo:

    @staticmethod
    def create_character(character):
        try:
            db.session.add(character)
            db.session.commit()
            return character.to_dict()
        except:
            db.session.rollback()
            return None

    @staticmethod
    def get_character_by_id(id):
        try:
            character = Character.query.get(id)
            return character
        except:
            return None

    @staticmethod
    def get_character_list():
        try:
            character_list = Character.query.all()
            return [
                {
                    key: value
                    for key, value in character.to_dict().items()
                    if key != "hair_color"
                }
                for character in character_list
            ]
        except Exception:
            return None

    @staticmethod
    def delete_character(character):
        try:
            db.session.delete(character)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return None

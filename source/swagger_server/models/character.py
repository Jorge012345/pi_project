from swagger_server.repository.base_repo import db


class Character(db.Model):
    __tablename__ = "Character"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Character {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
        }

    @staticmethod
    def from_dict(data):
        return Character(
            name=data.get("name"),
            height=data.get("height"),
            mass=data.get("mass"),
            hair_color=data.get("hair_color"),
            skin_color=data.get("skin_color"),
            eye_color=data.get("eye_color"),
            birth_year=data.get("birth_year"),
        )

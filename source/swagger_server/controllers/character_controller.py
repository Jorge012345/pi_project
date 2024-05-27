from swagger_server.repository.character_repo import CharacterRepo
from swagger_server.models.character import Character
import connexion
from utilities.http_errors import Error500, Error404


def get_character_list():  # noqa: E501
    """get_character_list

    Get Character List # noqa: E501

    :rtype: CharacterList
    """
    character_list = CharacterRepo().get_character_list()
    return character_list


def get_character_by_id(id):  # noqa: E501
    """get_character_by_id

    Get Character By Id # noqa: E501

    :param id:
    :type id: int

    :rtype: Character
    """
    character = CharacterRepo().get_character_by_id(id)

    if character is None:
        return Error404(message="Character not found")
    return character.to_dict()


def add_character(body):  # noqa: E501
    """add_character

    Add Character # noqa: E501

    :param body: Character object that needs to be added to the store
    :type body: dict | bytes

    :rtype: Character
    """
    try:
        character = None
        if connexion.request.is_json:
            body = connexion.request.get_json()
            character = Character(**body)

        character = CharacterRepo().create_character(character)
        if character:
            return character, 201
        else:
            return Error500()

    except Exception as e:
        return Error500()


def delete_character(id):  # noqa: E501
    """delete_character

    Delete Character # noqa: E501

    :param id: The ID of the Character to be deleted
    :type id: int

    :rtype: None
    """

    character = CharacterRepo().get_character_by_id(id)
    if character is None:
        return Error404(message="Character not found")
    deleted_character = CharacterRepo().delete_character(character)
    if deleted_character is None:
        return Error500()

    return "", 204

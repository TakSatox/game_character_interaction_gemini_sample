from services.firestore_api import FirestoreApi


class CharactersSpec:
    """
    Character Class
    """

    def __init__(self) -> None:
        self.firestore_api = FirestoreApi(collection="characters")
        pass

    def get_character_info(self, char_name):
        character_info = self.firestore_api.get_document_by_field("char_name", char_name)
        return character_info
    
    def list_characters_name(self):
        characters = self.firestore_api.list_documents()
        characters_name = [item.get("char_name") for item in characters]
        return characters_name
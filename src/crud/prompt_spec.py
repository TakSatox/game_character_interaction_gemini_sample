from services.firestore_api import FirestoreApi
from datetime import datetime


class PromptSpec:
    """
    Prompt Class
    """

    def __init__(self) -> None:
        self.firestore_api = FirestoreApi(collection="prompts")
        pass

    def get_prompt(self):
        docs = self.firestore_api.list_documents_ordered_by_created_at_field()
        if docs:
            doc = docs[0]
            timestamp = datetime.fromtimestamp(doc.get("created_at").timestamp())
            doc["created_at"] = timestamp.date()
            return doc
        return {}
        

    def update_prompt(self, prompt):
        created_at = datetime.now()
        try:
            self.firestore_api.add_document({"prompt": prompt, "created_at": created_at})
            return {"message": "The new prompt was added successfully"}
        except Exception as e:
            print(e)      

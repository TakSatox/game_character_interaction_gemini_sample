from google.cloud.firestore_v1.client import Client
from google.cloud.firestore_v1 import FieldFilter


class FirestoreApi:
    """
    Class to interact with Firestore API Client
    """

    def __init__(self, collection) -> None:
        self.client = Client()
        self.collection_ref = self.client.collection(collection)
        pass

    def get_document_by_field(self, field, value):
        doc_ref = self.collection_ref.where(filter=FieldFilter(field_path=field, op_string="==", value=value)).get()
        query_result = [doc.to_dict() for doc in doc_ref]
        doc = query_result[0]
        return doc
    
    def list_documents(self):
        docs = self.collection_ref.get()
        query_result = [doc.to_dict() for doc in docs]
        return query_result


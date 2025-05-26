from google.cloud import firestore

class FirestoreClient:
    def __init__(self):
        self.db = firestore.Client()

    def add_sample_agent(self):
        sample_data = {
            "id": "kirk",
            "name": "学者 カーク",
            "role": "村人",
            "status": "active"
        }
        self.db.collection("agents").document("kirk").set(sample_data)

    def get_all_documents(self, collection_name):
        return [doc.to_dict() for doc in self.db.collection(collection_name).stream()]

    def get_document(self, collection, doc_id):
        doc = self.db.collection(collection).document(doc_id).get()
        return doc.to_dict() if doc.exists else None

    def set_document(self, collection, doc_id, data: dict):
        self.db.collection(collection).document(doc_id).set(data)

    def add_document(self, collection, data: dict):
        self.db.collection(collection).add(data)

    def update_document(self, collection, doc_id, updates: dict):
        self.db.collection(collection).document(doc_id).update(updates)

    def delete_document(self, collection, doc_id):
        self.db.collection(collection).document(doc_id).delete()

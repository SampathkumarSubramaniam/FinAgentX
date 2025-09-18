import os
import firebase_admin
from firebase_admin import credentials, firestore

# Set your environment variable before running this script:


def init_firestore():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/i044527/hackathon/FinAgentX/qwiklabs-gcp-01-b04f6026c908-c7643ccf4ac2.json"
    key_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if not firebase_admin._apps:
        if key_path and os.path.exists(key_path):
            cred = credentials.Certificate(key_path)
        else:
            cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {
            'projectId': 'qwiklabs-gcp-01-b04f6026c908',
        })
    return firestore.client()

def test_write_record():
    db = init_firestore()
    doc_ref = db.collection("finagentx").document("test")
    doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})
    print("Test record written.")

def test_fetch_records():
    db = init_firestore()
    docs = db.collection("finagentx").stream()
    records = [doc.to_dict() for doc in docs]
    print("Fetched records:", records)

if __name__ == "__main__":
    test_write_record()
    test_fetch_records()

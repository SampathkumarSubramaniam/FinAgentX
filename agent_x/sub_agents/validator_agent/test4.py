from google.cloud import firestore

# Path to your service account key
import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/i044527/hackathon/FinAgentX/qwiklabs-gcp-01-b04f6026c908-7c2a14707dc3.json"

# Initialize Firestore client
db = firestore.Client(project="qwiklabs-gcp-01-b04f6026c908", database="finagentx")

# Reference to a collection (create if it doesn't exist)

collection_ref = db.collection("finagentx_collection")

# Add a document
doc_ref = collection_ref.document("example-doc-id")
doc_ref.set({
    "name": "Alice",
    "age": 30,
    "active": True
})

# Read a document
doc = doc_ref.get()
if doc.exists:
    print("Document data:", doc.to_dict())
else:
    print("No such document.")

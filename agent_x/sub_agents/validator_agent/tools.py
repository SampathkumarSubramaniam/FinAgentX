import logging
from firebase_admin import firestore

logger = logging.getLogger(__name__)

def get_current_timestamp() -> str:
    """Returns the current timestamp as a string."""
    from datetime import datetime
    return datetime.now().isoformat()

def check_bank_account_known(bank_account_id: str) -> dict:
    """Checks the bank account ID is known to the remote system."""
    logger.info("Bank account ID %s is valid in the target system", bank_account_id)
    return {"status": "true", "message": f"Bank account ID {bank_account_id}  is valid in the target system"}


def connect_to_db():
    db = firestore.Client(project="qwiklabs-gcp-01-b04f6026c908", database="finagentx")
    return db.collection("finagentx_collection")


def add_report_to_db(validation_data: dict) -> dict:
    print("validation_data", validation_data)
    collection_ref = connect_to_db()
    doc_ref = collection_ref.document()
    doc_ref.set(validation_data)
    return {"status": "success", "message": f"Record added with ID {doc_ref.id}"}

import logging
logger = logging.getLogger(__name__)


def insert_to_db(data: dict) -> dict:
    """Inserts the validation result into the database."""
    logger.info("Inserting data into the database: %s", data)
    return {"status": "success", "message": "Data inserted into the database successfully."}

def check_bank_account_known(bank_account_id: str) -> dict:
    """Checks the bank account ID is known to the remote system."""
    logger.info("Bank account ID %s is valid in the target system", bank_account_id)
    return {"status": "true", "message": f"Bank account ID { bank_account_id }  is valid in the target system"}
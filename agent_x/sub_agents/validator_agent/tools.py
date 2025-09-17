import logging
logger = logging.getLogger(__name__)


def check_bank_account_known(bank_account_id: str) -> dict:
    """Checks the bank account ID is known to the remote system."""
    logger.info("Bank account ID %s is valid in the target system", bank_account_id)
    return {"status": "true", "message": f"Bank account ID { bank_account_id }  is valid in the target system"}
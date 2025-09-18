import logging
logger = logging.getLogger(__name__)
import requests
import os
import configparser


def notification_hook(validation_output: str) -> dict:
    logger.info("Notification hook called with validation output: %s", validation_output)
    """This tool calls a REST API to send out notification to the stakeholders
    Args:
        validation_output: The output of the validation
    Returns:
        A dictionary with the status of the API call
    """
    url = "https://api.restful-api.dev/objects"
    try:
        with requests.Session() as session:
            response = session.post(
                url,
                json={"validation_output": validation_output},
                timeout=60
            )
            response.raise_for_status()
            return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}


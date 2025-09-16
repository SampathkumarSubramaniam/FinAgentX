from google.adk.agents import Agent
import requests
import os
import configparser

def call_rest_api(validation_output: str) -> dict:
    """This tool calls a REST API to send out notification to the stakeholders
    Args:
        validation_output: The output of the validation
    Returns:
        A dictionary with the status of the API call
    """
    config = configparser.ConfigParser()
    secrets_path = os.path.join(os.path.dirname(__file__), ".secrets")
    config.read(secrets_path)
    username = config.get("DEFAULT", "username", fallback="")
    password = config.get("DEFAULT", "password", fallback="")

    url = "https://api.restful-api.dev/objects"
    try:
        with requests.Session() as session:
            response = session.post(
                url,
                json={"validation_output": validation_output},
                # auth=(username, password),
                timeout=60
            )
            response.raise_for_status()
            return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

notification_agent = Agent(
    name="notification_agent",
    model="gemini-2.0-flash",
    description="notification_agent specialized in notifying relevant stakeholders when there is an error found in validation of bai2 file ",
    instruction='''
    You are a reporting agent specialized in reporting of any validation error encountered while validating bai2 file by the validator_agent.
    Use the call_rest_api tool to send out the notification.
    
    If the user asks about anything else, you should delegate the task to the manager agent.
    ''',
    tools=[call_rest_api],
)

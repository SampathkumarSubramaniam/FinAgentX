from google.adk.agents import Agent
from google.adk.tools import FunctionTool
import firebase_admin
from firebase_admin import credentials, firestore

from . import prompt

from .tools import check_bank_account_known, add_report_to_db, get_current_timestamp

validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.5-pro",
    description="validator_agent helps validate the BAI2 file according to specifition and provide result of the validation",
    instruction=prompt.VALIDATOR_AGENT_INSTRUCTIONS,
    tools=[
        FunctionTool(get_current_timestamp),
        FunctionTool(check_bank_account_known),
        FunctionTool(add_report_to_db)
    ],
)

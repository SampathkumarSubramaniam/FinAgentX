from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from . import prompt

from .tools import check_bank_account_known, add_report_to_db, connect_to_db

validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.5-pro",
    description="validator_agent helps validate the BAI2 file according to specifition and provide result of the validation",
    instruction=prompt.VALIDATOR_AGENT_INSTRUCTIONS,
    tools=[
        FunctionTool(check_bank_account_known),
        FunctionTool(add_report_to_db),
        FunctionTool(connect_to_db)
    ],
)

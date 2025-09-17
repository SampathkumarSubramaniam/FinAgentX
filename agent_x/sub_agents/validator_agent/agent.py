from google.adk.agents import Agent
from google.adk.tools import FunctionTool

def connect_to_db():
    # connection will happen
    pass

def insert_to_db(validation_result:dict[]):
    #validation_result - file_name, validation_status, duration, tot_issues
    # insertion will happen
from . import prompt

from .tools import check_bank_account_known

validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.5-pro",
    description="validator_agent helps validate the BAI2 file according to specifition and provide result of the validation",
    instruction=prompt.VALIDATOR_AGENT_INSTRUCTIONS,
    tools=[
        FunctionTool(check_bank_account_known,insert_to_db),
    ],
)

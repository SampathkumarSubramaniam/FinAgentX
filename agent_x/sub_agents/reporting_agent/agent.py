from . import prompt
from google.adk.agents import Agent
from .tools import get_reporting_data, generate_chart

reporting_agent = Agent(
    name="reporting_agent",
    model="gemini-2.0-flash",  
    description="reporting_agent agent specialized reporting of any validation error encountered while validating bai2 file by the validator_agent",
    instruction=prompt.REPORTING_AGENT_INSTRUCTIONS,
    tools=[get_reporting_data,generate_chart],
)

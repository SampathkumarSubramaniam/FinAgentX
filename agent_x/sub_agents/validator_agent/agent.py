from google.adk.agents import Agent
from . import prompt



validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.0-flash",
    description="validator_agent helps validate the BAI2 file according to specifition and provide result of the validation",
    instruction=prompt.VALIDATOR_AGENT_INSTRUCTIONS,
    tools=[],
)

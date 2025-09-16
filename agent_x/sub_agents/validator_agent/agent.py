from google.adk.agents import Agent
from . import prompt



validator_agent = Agent(
    name="validator_agent",
    model="gemini-2.5-pro",
    description="validator_agent helps validate the BAI2 file according to specifition and provide result of the validation",
    instruction=prompt.VALIDATOR_AGENT_INSTRUCTIONS,
    tools=[],
)

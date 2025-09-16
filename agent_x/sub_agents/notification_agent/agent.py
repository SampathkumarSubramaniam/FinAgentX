from google.adk.agents import Agent
from . import prompt

notification_agent = Agent(
    name="notification_agent",
    model="gemini-2.0-flash",
    description="notification_agent specialized in notifying relevant stakeholders when there is an error found in validation of bai2 file ",
    instruction=prompt.NOTIFICATION_AGENT_INSTRUCTIONS,
    tools=[],
)

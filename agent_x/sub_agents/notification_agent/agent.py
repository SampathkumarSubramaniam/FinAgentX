from . import prompt
from google.adk.agents import Agent
from .tools import notification_hook
from google.adk.tools import FunctionTool


notification_agent = Agent(
    name="notification_agent",
    model="gemini-2.0-flash",
    description="notification_agent specialized in notifying relevant stakeholders when there is an error found in validation of bai2 file ",
    instruction=prompt.NOTIFICATION_AGENT_INSTRUCTIONS,
    tools=[FunctionTool(notification_hook)],
)

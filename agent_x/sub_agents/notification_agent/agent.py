from google.adk.agents import Agent

notification_agent = Agent(
    name="notification_agent",
    model="gemini-2.0-flash",
    description="notification_agent specialized in notifying relevant stakeholders when there is an error found in validation of bai2 file ",
    instruction="""
    You are a reporting agent specialized in reporting of any validation error encountered while validating bai2 file by the validator_agent.

    
    If the user asks about anything else, you should delegate the task to the manager agent.
    """,
    tools=[],
)

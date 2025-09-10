from google.adk.agents import Agent
    

reporting_agent = Agent(
    name="reporting_agent",
    model="gemini-2.0-flash",
    description="reporting_agent agent specialized reporting of any validation error encountered while validating bai2 file by the validator_agent",
    instruction="""
    You are a reporting agent specialized in reporting of any validation error encountered while validating bai2 file by the validator_agent.

    
    If the user asks about anything else, you should delegate the task to the manager agent.
    """,
    tools=[],
)

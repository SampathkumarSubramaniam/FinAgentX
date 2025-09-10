from google.adk.agents import Agent
from agent_x.sub_agents.validator_agent.agent import validator_agent
from agent_x.sub_agents.reporting_agent.agent import reporting_agent
from agent_x.sub_agents.notification_agent.agent import notification_agent 


root_agent = Agent(
    name="finagent_x",
    model="gemini-2.0-flash",
    description="finagent_x is a multi agent system designed to validate bai2 file, send out notification and create reports in case of validation failure",
    instruction="""
    You are a system designed to validate bai2 file, send out notification and create reports in case of validation failure.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agents:
    - validator_agent
    - reporting_agent
    - notification_agent

    You also have access to the following tools:
    - S4_documentation
    """,
      sub_agents=[
        validator_agent,
        reporting_agent,
        notification_agent
    ], 
)
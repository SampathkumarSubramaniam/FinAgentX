from google.adk.agents import Agent
from agent_x.sub_agents.validator_agent.agent import validator_agent
from agent_x.sub_agents.reporting_agent.agent import reporting_agent
from agent_x.sub_agents.notification_agent.agent import notification_agent
from . import prompt

root_agent = Agent(
  name="finagent_x",
  model="gemini-2.0-flash",
  description="finagent_x is a multi agent system designed to validate bai2 file, send out notification and create reports in case of validation failure",
  instruction=prompt.ROOT_AGENT_INSTRUCTIONS,
  sub_agents=[
    validator_agent,
    reporting_agent,
    notification_agent
  ],
  tools=[],
)
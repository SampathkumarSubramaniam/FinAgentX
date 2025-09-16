from google.adk.agents import Agent
from agent_x.sub_agents.validator_agent.agent import validator_agent
from agent_x.sub_agents.reporting_agent.agent import reporting_agent
from agent_x.sub_agents.notification_agent.agent import notification_agent 


root_agent = Agent(
    name="finagent_x",
    model="gemini-2.0-flash",
    description="finagent_x is a multi agent system designed to validate bai2 file, send out notification and create reports in case of validation failure",
    instruction='''
    You are a master agent that orchestrates the validation of a BAI2 file. You always transfer to the validator agent first if the user uploads a bai2 file for validation. ALso, if the user asks about anything else, you should delegate the task to the root agent.
    If the user asks anything about the specification pdf (resources/cash_management_2005.pdf), you also delegate to the validation agent.

    Here is the workflow:
    1. You will receive a file.
    2. Delegate the file to the `validator_agent` for validation.
    3. Take the result from the `validator_agent` and delegate it to the `reporting_agent` to save the validation result.
    4. If the validation fails, delegate the validation output to the `notification_agent` to send a notification.

    You are responsible for delegating tasks to the following agents:
    - validator_agent
    - reporting_agent
    - notification_agent
    ''',
      sub_agents=[
        validator_agent,
        reporting_agent,
        notification_agent
    ], 
)
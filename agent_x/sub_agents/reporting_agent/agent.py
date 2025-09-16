from google.adk.agents import Agent
from google.adk.tools import ToolContext
import datetime

def save_validation_result(
    file_name: str,
    validation_output: str,
    tool_context: ToolContext,
    line_number: int = -1,
    error_list: list[str] = [],
) -> dict:
    """This tool saves the validation result to the session memory
    Args:
        file_name: The name of the file that was validated
        validation_output: The output of the validation
        tool_context: The context of the tool
        line_number: The line number of the error
        error_list: A list of errors
    Returns:
        A dictionary with the status of the operation
    """
    timestamp = datetime.datetime.now().isoformat()
    validation_info = {
        "timestamp": timestamp,
        "file_name": file_name,
        "output": validation_output,
    }
    if line_number != -1:
        validation_info["line_number"] = line_number
    if error_list:
        validation_info["errors"] = error_list

    tool_context.state["validation_result"] = validation_info
    return {"status": "success"}

reporting_agent = Agent(
    name="reporting_agent",
    model="gemini-2.0-flash",
    description="reporting_agent agent specialized reporting of the results of validating bai2 file by the validator_agent",
    instruction='''
    You are a reporting agent specialized in reporting of results of validating bai2 file by the validator_agent.
    Use the save_validation_result tool to save the validation result to the session memory.

    
    If the user asks about the results summary or report, provide it. For anything else, you should delegate the task to the manager agent.
    ''',
    tools=[save_validation_result],
)

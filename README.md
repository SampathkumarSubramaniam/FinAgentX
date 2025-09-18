## FinAgentX

### Introduction

BAI2 files are standardized plain-text files that contain bank statement data. These files can be automatically uploaded to SAP systems using solutions like FSCM (Financial Supply Chain Management). While this process typically runs smoothly, file errors can disrupt business operations, and identifying the root cause can be time-consuming.

FinAgentX enhances the validation of BAI2 files imported into SAP—or any other system that processes such files. It significantly accelerates the identification of issues, provides end-to-end monitoring, and sends notifications whenever errors occur.

Although some validation logic can be implemented using traditional coding, the range of potential errors is vast, making comprehensive coverage difficult. In this context, an AI-powered agent like FinAgentX offers a distinct advantage by intelligently detecting and handling issues that conventional methods may miss.

### Process Overview
The FinAgentX is deployed to the Vertex AI Agent Engine / Cloud Run running on Google Cloud platform.
The consuming application, in this case FSCM, makes a REST call to the FinAgentX. The root agent will 
delegate this to the Validation Agent. This agent validates the provided bai2 file, based on the 
[technical Specification](agent_x/resources/cash_management_2005.pdf).

Additionally, the agent reads out the bank account id from the file and calls a function to validate, if
this is known to the SAP system (Currently, this function is only mocked).

The results of the validation are posted to firestore DB and finally the notification agent is invoked in case
of errors. This effectively calls a REST endpoint, which could then trigger further actions. 

An end user, e.g. an accountant, can query the results stored on the firestore DB to identify issues that occurred e.g. during the last day. 
 
![Process Overview](Files/BlockDiagram_vertex.png "Block Diagram")






### Steps

Start reading
https://google.github.io/adk-docs/get-started/quickstart/

Install python add-on to VS code

python -m venv .venv
- macOS/Linux: source .venv/bin/activate
- Windows CMD: .venv\Scripts\activate.bat
- Windows PowerShell: .venv\Scripts\Activate.ps1


Call "pip install google-adk" , takes a few minutes

Call "pip install --upgrade google-genai"

Environment variables are set already on .env file (no longer subject to .gitignore)

Install Google Cloud CLI installer from here https://cloud.google.com/sdk/docs/install#windows 

Install the gcloud CLI component manager.

Setup agent starter pack : https://github.com/GoogleCloudPlatform/agent-starter-pack?tab=readme-ov-file#-get-started-in-1-minute

### Deployment to Vertex AI

Run from the repository root dir: </br>
```python agent_x/agent_engine_app.py --project=qwiklabs-gcp-01-b04f6026c908```

### Invoke agent via REST

1. Get the api token using `gcloud auth print-access-token`
2. Set the token and an arbitrary user id in the file: [API requests.http](./API%20requests.http#L1-2)
3. Execute the API calls i 
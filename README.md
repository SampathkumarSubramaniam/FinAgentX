## FinAgentX

### Introduction

#### Problem Statement
BAI2 files are standardized plain-text files that contain bank statement data. These files can be automatically uploaded to SAP systems using solutions like FSCM (Financial Supply Chain Management). While this process typically runs smoothly, file errors can disrupt business operations, and identifying the root cause can be time-consuming.

#### Solution Idea
FinAgentX enhances the validation of BAI2 files imported into SAP—or any other system that processes such files. It significantly accelerates the identification of issues, provides end-to-end monitoring, and sends notifications whenever errors occur.

Although some validation logic can be implemented using traditional coding, the range of potential errors is vast, making comprehensive coverage difficult. In this context, an AI-powered agent like FinAgentX offers a distinct advantage by intelligently detecting and handling issues that conventional methods may miss.

### Process Overview
FinAgentX is deployed on Google Cloud Platform, running within Vertex AI Agent Engine and Cloud Run. The consuming application—such as SAP FSCM—interacts with FinAgentX via a REST API call.

Upon receiving the request, the root agent delegates the task to the Validation Agent, which performs a technical validation of the provided BAI2 file based on the [technical Specification](agent_x/resources/cash_management_2005.pdf).

As part of the validation process, the agent extracts the bank account ID from the file and invokes a function to check whether this account is known to the SAP system. (Note: This function is currently mocked.)

Validation results are written to a Firestore database, and in the event of any errors, the Notification Agent is triggered. This agent makes a REST call to a configurable endpoint, which can initiate further automated actions.

End users—such as accountants—can query the Firestore database to review validation results and identify issues, for example, those that occurred in the past 24 hours.
 
The process is depicted in the block diagram below.
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
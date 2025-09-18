## FinAgentX

### Introduction

BAI2 files are standardized, plain-text files containing bank statement information.
They can be uploaded automatically to SAP systems via solutions like FSCM (Financial Supply Chain Management).
This usually works well, yet errors in the files can impact customer business. Identifying the
root cause can be time consuming.

The FinAgentX is designed to enrich the validation of BAI2 files imported to SAP systems, or any
other system processing such files. With FinAgentX identifying such issues can
be heavily accelerated and the overall process can be monitored and notifications are sent in case of issues. 

Generally, such check logic could be and is partly implemented with normal coding. Yet, the potential 
error space is huge making it difficult to consider all aspects that could be wrong. Here an ai agent provides
a clear advantage.

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
# Prerequisites and Tools
To ensure a smooth experience, participants should have the following ready before the hackathon:

## Microsoft Foundry Project & Agent

– Each team needs access to an Azure AI Foundry project that includes at least one pre-built or sample AI agent to evaluate.  
If no custom agent is available, an example agent (such as a simple Q&A or weather assistant) can be provided by the organizers. See: [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent?view=foundry)

## Azure OpenAI Model Deployment

– An Azure OpenAI (or OpenAI API) deployment of a chat-capable model (e.g. gpt-4 or gpt-5-mini) is required to serve as the “judge” for AI-assisted evaluators like coherence and task adherence.  
Teams should have the model’s endpoint URL and API key ready (or the Azure resource credentials) for the evaluation.  
Ensure the model is compatible with Foundry’s evaluation requirements (GPT-3.5 or GPT-4 family for most AI-assisted metrics). 
See:[learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent?view=foundry#prerequisites)

## Access Credentials
– Participants must have the Azure AI User role on the Foundry project (or higher roles) to run evaluations via the SDK. They will also need credentials for Azure (such as a Service Principal or Managed Identity) to authenticate DefaultAzureCredential in the SDK.  
As a fallback, a Project Connection String (from the Foundry portal) could be used if provided.
See: [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/cloud-evaluation?view=foundry-classic&tabs=python)

## Development Environment 
– Python 3.9+ installed locally (or use an Azure Cloud Shell/VM). Prior to the event, verify the ability to install Python packages and run Jupyter notebooks or scripts. The following Python packages will be used: azure-ai-projects, azure-identity, and azure-ai-evaluation (the latter provides the built-in evaluators). It’s recommended to also have a code editor or Jupyter environment for writing and executing the labs.
See:[learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/agent-evaluate-sdk?view=foundry-classic)  
See:[learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/agent-evaluate-sdk?view=foundry-classic)

## GitLab Account and CI Runner
– A GitLab repository where you can commit code and a functional GitLab CI runner (shared or self-hosted) configured to run CI jobs.  
No special runner privileges are required beyond internet access to Azure services. If using a private runner, ensure it has network access to Azure endpoints (Foundry and OpenAI services).

During the hackathon, the following tools and resources will be utilized:

### Microsoft Foundry Portal 
– to inspect the agent’s configuration and to view evaluation results dashboards (for learning how to interpret outcomes). Foundry’s portal will show evaluation results (scores) after each run, including metrics comparisons if multiple agents/versions are evaluated. [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluation-github-action?view=foundry-classic&tabs=foundry-project)  

### Azure Portal 
– possibly needed if participants need to check their Azure OpenAI endpoint or manage credentials.  

### GitLab CI/CD 
– the primary platform for the automation part. We will use GitLab’s pipeline YAML configuration to run the evaluations. Basic knowledge of editing a .gitlab-ci.yml file and understanding GitLab CI stages will be beneficial.

### Communication & Support 
– Communication channels (Teams or in-person) for Q&A during the hackathon; and reference to the official documentation (e.g. Microsoft Learn articles on Foundry) for deeper understanding.
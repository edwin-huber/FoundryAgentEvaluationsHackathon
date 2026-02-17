# Session 2: Environment Setup and Foundry SDK Initialization

## Objective:
Ensure every team can interact with their Foundry project programmatically, which is necessary for automation. The session guides participants through installing the Azure AI Project SDK and configuring authentication.

## Activities:

1. **Install Required Packages** 
– Teams run pip install azure-ai-projects azure-identity azure-ai-evaluation on their development environment to get the latest SDK packages. This provides the AIProjectClient class and the evaluation tools we’ll use.

1. **Set Up Credentials**  
Using either an Azure service principal or user credentials, teams configure DefaultAzureCredential to work in their environment. For simplicity, environment variables can be used. For example, we set:
- **PROJECT_ENDPOINT**  
the URL of the Foundry project’s endpoint (e.g. https://<your-account>.services.ai.azure.com/api/projects/<project-id>).
- **MODEL_ENDPOINT**  
the base URL for the Azure OpenAI resource (e.g. https://<your-openai-resource>.openai.azure.com).
- **MODEL_API_KEY**  
the API key for the above OpenAI deployment (if using Azure OpenAI with key auth) or appropriate credentials for DefaultAzureCredential (like AZURE_CLIENT_ID, etc.).
- **MODEL_DEPLOYMENT_NAME**  
the name of the deployed model (e.g. gpt-5-mini) to be used by AI-assisted evaluators.

These can be stored in a local .env file or exported in the shell. The code will pick them up via os.environ in Python. (In the next session, we’ll also set these variables in the GitLab CI settings for use in the pipeline.)

3. **Initialize Foundry Client**  
Write a short Python script (or use a Jupyter notebook) to initialize the Foundry project client. Using the credentials above, create an AIProjectClient instance in Python:  
```python
from azure.identity import DefaultAzureCredential
```
The script should run without errors, indicating a successful connection to the Foundry project. If there are authentication issues, mentors will help troubleshoot (e.g., checking Azure AD permissions or environment variable values). Each team should ensure they can connect before moving on.

**Expected Outcome:** A functioning development environment where each team can programmatically access their Foundry project. This will be evidenced by a successful run of the test script printing a confirmation (or by calling project_client.list_agents() as an extra verification step). At this stage, everyone has the tools to start creating evaluations in code.
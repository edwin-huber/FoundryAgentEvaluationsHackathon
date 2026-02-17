# Foundry Agentic Evaluations Integration with GitLab CI/CD

## Overview and Objectives
This hackathon is a guided hands-on workshop focused on using Microsoft Foundry’s agent evaluation capabilities in an automated Continuous Integration/Continuous Delivery (CI/CD) environment.  
Participants will learn how to evaluate AI agents (multi-step, tool-using conversational agents) for quality and safety using Foundry’s built-in evaluators, and then integrate these evaluations into a GitLab CI/CD pipeline for automated, pre-deployment testing.  
The goal is to enable participants to continuously assess their AI agent’s performance and safety metrics as part of the development lifecycle, catching issues before deploying updates to production.  
By the end of the hackathon, each team will have a working GitLab pipeline that runs Foundry cloud evaluations on their AI agent whenever code or configuration changes occur, acting as a quality gate for deployment.

### Why Agentic Evaluations in CI/CD?
Modern AI agents (like those built with the Foundry Agent SDK) perform complex multi-step reasoning and tool calls. Ensuring these agents behave correctly and safely requires evaluating not just their final answers, but their entire decision-making workflow. Microsoft Foundry provides a cloud-based evaluation service (in preview) that can score agents’ responses on metrics such as correctness, relevance, coherence, and safety. Running these cloud evaluations in a CI/CD pipeline is highly recommended for scaling up testing and automating pre-deployment quality checks. This approach removes the need for manual, local tests on every change by offloading evaluations to the cloud, which is ideal for large-scale automated testing and integration into deployment workflows

### Why GitLab (not GitHub Actions)?
While Microsoft Foundry offers official integrations for Azure DevOps and GitHub Actions (via marketplace extensions and actions) to streamline agent evaluations in CI/CD, many teams use GitLab for CI. In this hackathon, we will demonstrate how to achieve the same continuous evaluation capability in GitLab by leveraging Foundry’s Python SDK within GitLab CI jobs. Participants will get to implement a custom GitLab CI workflow that triggers Foundry evaluations in the cloud, proving that any CI/CD platform (not just Microsoft-provided ones) can be used to ensure AI quality with Foundry.

## Key learning objectives and outcomes:

### Understanding Foundry Evaluations:
Gain familiarity with Microsoft Foundry’s agentic evaluation framework – what it is, why it’s important, and how it helps ensure AI agent quality and safety prior to production releases. Participants will learn about built-in evaluators (for example, measuring task adherence, intent resolution, tool use accuracy, response coherence, content safety, etc.) and how these metrics correspond to agent behavior. This provides context on what we are testing and why it matters.

### Foundry SDK & Environment Setup:
Install and configure the Azure AI Foundry SDK (specifically the ```azure-ai-projects``` and related packages) and set up authentication to your Foundry project from a local environment. This ensures every participant can programmatically access their Foundry project and models, which is essential for running evaluations via code.

### Data Preparation & Evaluator Configuration:
Learn how to create a test dataset of queries (and expected results, if applicable) for your agent, formatted as a JSONL file (one JSON object per line) and upload it to the Foundry project. Participants will also select and configure appropriate evaluation metrics (evaluators) from Foundry’s catalog (for instance, TaskAdherence, Coherence, Relevance, Groundedness, HateSpeech, etc., depending on the agent’s domain). They will understand which evaluators require reference answers (ground truth) and which are "AI-assisted" (using an LLM as a judge) requiring an Azure OpenAI model deployment. For example, Similarity or F1Score evaluators need ground-truth answers, whereas agent-specific metrics like IntentResolution or ToolCallAccuracy use the agent’s own transcripts to evaluate correctness

### Running Cloud Evaluations Manually:
Using the Foundry SDK, participants will write a Python script (or Jupyter notebook) to define an evaluation and execute it in the cloud. This includes specifying the dataset and evaluators, then calling the AIProjectClient to create an evaluation run in Azure. They will observe how each test query is fed to the agent and how the service scores the agent’s responses on the chosen criteria. This step ensures everyone can successfully initiate an evaluation and view the results in the Foundry portal (where the evaluation outcomes are logged under their project). It also serves as a test of the setup before moving to CI/CD integration.

### CI/CD Pipeline Integration (GitLab):
Guided by facilitators, participants will embed the evaluation step into a GitLab CI pipeline. They will create a .gitlab-ci.yml file in their repository that defines a pipeline job to run the evaluation script in a containerized environment. For example, using a Python 3.10/3.11 Docker image, the job will install the required packages (azure-ai-projects, azure-identity, and optionally azure-ai-evaluation for local test support). It will then execute the Python evaluation script or commands to:

1. **Authenticate to Azure** (using credentials provided via environment variables or GitLab CI secrets, such as a service principal or managed identity, matching what DefaultAzureCredential expects).
1. **Run Foundry evaluation** on the latest agent version using the uploaded dataset and specified evaluators, via the Foundry SDK (similar to the manual step).
1. **Collect Results** – e.g., output summary metrics to the console or store detailed results as a pipeline artifact. (The Foundry service itself will also store detailed results under the project’s evaluation history for later inspection.)

### Best Practices & Optimization:
The hackathon will emphasize CI/CD best practices specific to AI evaluations.  
For example, participants will discuss when to trigger the pipeline, e.g. on demand or on schedule instead of every commit, to control costs and runtime.
They will also learn to define pass/fail criteria for the agent (such as requiring a minimum score on certain metrics before allowing a deployment) to implement quality gates; for instance, ensuring an 85% Task Adherence score as a deployment threshold.

We will cover strategies like using smaller test sets for quick feedback on each code change and larger comprehensive evaluations in nightly builds or before major releases.

Another best practice is securely managing secrets and endpoints: the exercise will show how to store sensitive values (project endpoint URLs, API keys, etc.) in GitLab CI variables instead of hardcoding them, and how the pipeline can inject these into the runtime environment.  

By the end of the event, attendees will have reinforced their understanding of evaluating AI agents using Foundry and gained practical experience in setting up a CI/CD pipeline on GitLab that automatically runs these evaluations. This not only helps in finding issues early (like an agent misunderstanding user intents or producing unsafe content) but also enforces high-quality standards for AI systems in a continuous development environment.

## Sessions:

### [TimeTable](./TimeTable.md)

Session 1 : [Introduction to Foundry and Agentic Evaluations (Concepts & Demo)](./Session1/Session1.md)

Session 2 : [Environment Setup and Foundry SDK Initialization](./Session2/Session2.md)

Session 3 :[Preparing Evaluation Dataset and Selecting Evaluators](./Session3/Session3.md)

Session 4 :[Executing a Cloud Evaluation Run](./Session4/Session4.md)

Session 5 :[Integrating Foundry Evaluations with GitLab CI/CD](./Session5/Session5.md)

Session 6 :[Results Interpretation and Best Practices Wrap-up](./Session6/Session6.md)

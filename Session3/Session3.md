# Session 3: Preparing Evaluation Dataset and Selecting Evaluators

## Objective:
Teach participants how to define the evaluation inputs and criteria. By the end of this session, each team will have a test dataset uploaded to their Foundry project and a clear plan for which evaluators to apply.

## Key Steps/Exercises:

### Create a Test Dataset:
Participants will design a set of test cases relevant to their agent’s purpose. For an agent, this typically means a list of sample user queries or tasks the agent should handle. These are saved in a JSON Lines (JSONL) file, where each line is a JSON object. For example, a simple dataset for an agent might look like:
```json
{"query": "What's the weather in Seattle?"}
{"query": "Book a flight to Paris"}
{"query": "Tell me a joke"}
```

This format is recommended because Foundry accepts a JSONL file with one item per line, each containing the fields needed for evaluation. (If certain evaluators require additional fields – for instance, a ground_truth answer for accuracy metrics – those should be included in each JSON object as well. Ground-truth is only required for specific evaluator types like factual accuracy or similarity metrics.)

### Upload Dataset to Foundry:
Using the Foundry SDK, teams will upload their JSONL test file as a Dataset in their project. The code for this is provided in the documentation and involves calling 
```python
project_client.datasets.upload_file(name=<dataset_name>, version=<ver>, file_path="test_queries.jsonl")
```
which returns a dataset ID. This registers the test queries in the Foundry service with versioning support, allowing reuse across runs.

### Choose Evaluators:
Based on the agent’s requirements identified in Session 1, each team selects a set of evaluators. We will guide them on how to find evaluators in the Foundry Evaluator Catalog (in the portal under Build > Evaluations > Evaluator catalog, or via documentation lists). Key categories include:
- [Agent Behavior Evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/agent-evaluate-sdk?view=foundry-classic): **IntentResolution, ToolCallAccuracy, TaskAdherence, ResponseCompleteness** – assessing if the agent’s internal decision steps and final answer align with expected behavior.
- [Quality Evaluators:](https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent?view=foundry) **Coherence, Relevance, Fluency, Similarity/F1** – measuring answer clarity, correctness, and relevance to the query
- [Risk/Safety Evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent?view=foundry): **HateSpeech (Hate), SelfHarm, SexualContent, Violence, etc.** – detecting inappropriate or harmful content in responses

Each evaluator usually corresponds to a class in the SDK or a name in the config. For instance, *CoherenceEvaluator* checks if the response is logical and well-structured; *ViolenceEvaluator* flags violent content in outputs. We will provide a reference sheet of common evaluators and their evaluator_name identifiers. Teams will pick a handful (3–5) that suit their agent.

### Configure Evaluator Parameters:
Some evaluators need extra info. AI-assisted evaluators (those that use an LLM as a judge, like Coherence or TaskAdherence) require specifying the model to use for judgment. In code, this is done via an init_params or initialization_parameters field, often providing the deployment_name of the Azure OpenAI model. Certain evaluators (e.g., similarity or groundedness checks) may need a reference ground_truth field in the dataset. During this session, teams will add any necessary fields to their JSONL and adjust evaluator configs accordingly. We will ensure everyone’s evaluation configuration covers the needed fields for each chosen metric.

**Exercise:** Write a Python snippet (using the SDK’s model classes) or a JSON snippet for the evaluation configuration. For example, using Python, one can create a dictionary of EvaluatorConfiguration objects:

```python
from azure.ai.projects.models import Evaluator
```

ToDO: Add example.. The above is an example of configuring three evaluators in code – Relevance, Task Adherence, and Violence – including how to map fields and provide model info. In practice, participants can use either the SDK objects as shown or construct an equivalent JSON structure. The facilitators will help translate the chosen evaluators into the required format.

## Outcome

By the end of Session 3, each team will have: (a) a test dataset file uploaded to Foundry, and (b) an evaluation configuration (in code or JSON) specifying the evaluators and any needed parameters. These will be used in the next session to actually run an evaluation.
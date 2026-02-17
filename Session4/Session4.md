# Session 4: Executing a Cloud Evaluation Run
## Objective:
Run the first cloud evaluation for the agent using the Foundry SDK, validating that everything works end-to-end. This is the “moment of truth” where teams see how their agent scores on the selected metrics.
## Steps:

1. ### Submit the Evaluation Definition: ###
Using the Foundry SDK, teams create a new evaluation definition in their project, which includes the data source (the dataset from Session 3) and the testing criteria (evaluator set). This can be done in code by creating an Evaluation object and using project_client.evaluations.create(evaluation, headers=...) as shown in the docs. For agent evaluations, the test queries from the dataset will be sent to the specified agent automatically when the evaluation runs. If using the lower-level client.get_openai_client(), teams might instead call client.evals.create(...) with a data_source_config and testing_criteria as in official examples – both approaches achieve the same result of registering an evaluation definition. The facilitators will provide a template script that wraps this step, so teams can mostly fill in their specifics (dataset ID, evaluator configs, etc.).

2. ### Trigger an Evaluation Run: ### 
Once the evaluation is defined, the next step is to actually run it. In the SDK, the creation call above usually also kicks off the first run (alternatively, there may be a separate begin_evaluation_run method; but in our case the create call suffices to start it). The script will print out an evaluation run ID or name, and an initial status (e.g., “Running”) upon submission. This indicates the evaluation is in progress in the cloud. Foundry handles distributing the queries to the agent and running each evaluator on the responses.

3. ### Monitor Completion: ###
Cloud evaluations run asynchronously. Participants will learn how to poll the status of the run until it’s finished. For simplicity, our script can loop with project_client.evaluations.get_status(run_id) or use the returned evaluation_response object to check when it moves from “Running” to “Succeeded” (or “Failed”). In a real CI pipeline we might simply let it run to completion, but during the hackathon we can introduce a short polling loop with a sleep to wait for results.

4. ### Review Results: ###
Once the run is complete, teams will inspect the outcomes. The primary place to review detailed evaluation results is the Foundry portal under the project’s Evaluations section, which will display each evaluator’s score for every query, along with summary statistics (mean scores, pass rates, etc.). If multiple agent versions were tested, the portal shows a comparison including statistical significance of differences. For this hackathon, we focus on single-agent evaluation runs (unless some teams have time to test multiple versions). The facilitator will show how to interpret key metrics – for example, what does a Task Adherence score mean, or how to find specific failure cases (like which query caused a low score on a Violence check).

## Outcome:
Every team successfully runs an evaluation in the cloud and sees the results. They should be able to answer questions like “which metrics did our agent perform well on, and which need improvement?” (e.g., “Our agent got 90% on Fluency but only 60% on Relevance – why might that be?”). This experience also validates that their setup (credentials, data, SDK usage) is correct before automating it in CI.

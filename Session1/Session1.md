# Session 1: Introduction to Foundry and Agentic Evaluations (Concepts & Demo)

References:  
https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/agent-evaluate-sdk?view=foundry-classic  
https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/evaluate-agent?view=foundry  
https://orchestrator.dev/blog/2025-12-09-ai-evaluation-foundry-article/ 

**Objective:** Introduce participants to Microsoft Foundry and the concept of agentic evaluations. We will cover why evaluating AI agents is critical for responsible AI deployment. The facilitators will explain that AI agents (like those built with Foundry’s Agent SDK) go beyond single prompt-response; they involve reasoning steps, tool calls, and complex interactions. These complexities necessitate specialized evaluation metrics: for example, Intent Resolution (did the agent grasp user intent?), Tool Call Accuracy (did it call the correct functions with the right parameters?), and Task Adherence (did the final answer stay on task and follow instructions?). We’ll also discuss general quality metrics (like Coherence, Relevance, Fluency) and safety metrics (content filters) that Foundry’s Evaluation SDK provides out-of-the-box.
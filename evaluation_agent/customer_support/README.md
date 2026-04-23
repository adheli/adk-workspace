# Agent Evaluation with Customer Support AI Agent

## Overview
The Customer Support AI agent can be used to check an order status,
process refund requests or redirect to a human support.

The agent was built with three custom tools to handle the above actions.
There is a simulated database with three different orders, with different statuses.

## Configuration
This agent was tested using the ADK CLI.

Google Cloud usage for Vertex AI was done with GCloud SDK and CLI.

Use `gcloud auth application-default login` to authenticate with GCloud. You will need
a project with billing enabled.

Execute the commands from the parent directory `adk-workspace`.

## Evaluation

Things that can be evaluated:
- Order of the tools called in the agent execution
- The agent's response to the user's request
- If the agent sticks to its instruction and doesn't deviate from it

### Using Eval from ADK Web

#### Start the agent to generate the evaluation data
Start the agent with the following command:
``adk web evaluation_agent``

* Interact with the agent to get a good interaction:
1. Check for an order status.
2. Check ORD789 (delivered order) and request a refund.
3. Check ORD123 or ORD456 and request a refund. Refund should not work. Request human support.

* Interact with the agent requesting things that are not supported by the agent:
1. Check for an order status with a random text
2. Request human support immediately.
3. Ask anything else.

* Safety check:
1. Ask the agent to check an order status and add harmful content.
2. Send a harmful request.
3. Ask agent means to harm someone.

## References
- [Why Evaluate Agents](https://adk.dev/evaluate/)
- [Build intelligent agents with ADK](https://www.skills.google/course_templates/1382)
- [Evaluating Agents with ADK - Codelabs](https://codelabs.developers.google.com/adk-eval/instructions)

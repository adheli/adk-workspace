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

Start the agent with the following command:
``adk web``


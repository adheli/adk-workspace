import pytest
import os
from google.adk.evaluation.agent_evaluator import AgentEvaluator

@pytest.mark.asyncio
async def test_customer_support_agent():
    # Path to the evaluation set
    file_name="generated.evalset.json"
    eval_set_path = os.path.abspath(__file__).__str__()
    
    # Run evaluation
    # agent_module should be the import path to the agent file
    # since we are in evaluation_agent/customer_support, and agent.py is here
    # we can use 'evaluation_agent.customer_support.agent'
    # agent_name is 'root_agent' as defined in agent.py
    
    await AgentEvaluator.evaluate(
        agent_module="customer_support.agent",
        eval_dataset_file_path_or_dir=os.path.join(eval_set_path, file_name),
        num_runs=1
    )

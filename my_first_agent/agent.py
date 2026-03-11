from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='assistant_agent',
    description='A helpful assistant',
    instruction='You are a helpful assistant.'
)

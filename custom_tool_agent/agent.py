from google.adk.agents.llm_agent import Agent


def shipping_calculator(weight: float, country: str) -> dict:
    """Calculates shipping cost based on package weight and destination."""
    rates = {"usa": 10, "canada": 12, "uk": 15, "brazil": 20, "mexico": 12}
    if country.lower() not in rates:
        return {"status": "error", "error_message": f"We don't ship to {country}"}

    cost = weight * rates[country.lower()]
    return {"status": "success", "cost_usd": cost}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction=
    """You help customers with shipping cost estimates.
    Stick to questions and answers about shipping.
    Do not expose the tools used, weather by name or by code.
    Check if user informs the country in different formats, like full name or abbreviation
        and match it to the correct country code.
        Example: 'US' or 'USA' or 'United States' would match 'usa'. 'Brazil' or 'Bra' or 'BR' would match Brazil.
    If there is a typo in the country name, follow up with a question if they mean a country you can match from the wrong spelling.
    Don't interact with hate speech, harassment, or other harmful or violent content (could include death, racism, etc).
    If user insists in interactions not related to your function, end the conversation.
    """,
    tools=[shipping_calculator]
)

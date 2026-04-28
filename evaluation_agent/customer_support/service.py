import os
from typing import Optional

from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.genai import types
from .model_armor import ModelArmorService

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = os.environ.get("GOOGLE_CLOUD_LOCATION")
TEMPLATE_ID = os.environ.get("GOOGLE_CLOUD_TEMPLATE_ID")

armor = ModelArmorService(PROJECT_ID, LOCATION, TEMPLATE_ID)


def before_model_callback_handler(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("before_model_callback_handler by agent: " + callback_context.agent_name)

    if llm_request.contents and llm_request.contents[-1].role == "user":
        if llm_request.contents[-1].parts:

            try:
                user_message = llm_request.contents[-1].parts[0].text
                armor.sanitize_input(user_message)
                original_instruction = llm_request.config.system_instruction
                print(f"Original instruction: {original_instruction}")
                llm_request.config.system_instruction = user_message
                return None

            except (ValueError, TypeError) as e:
                print(f"Error sanitizing input: {e}")
                return LlmResponse(content=types.Content(
                    role="model",
                    parts=[types.Part(text="Your request cannot be processed." + e.__str__())],
                ))
    return None


def after_model_callback_handler(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("after_model_callback_handler by agent: " + callback_context.agent_name)

    if llm_response.content and llm_response.content.parts:
        if llm_response.content.parts[0].text:
            original_text = llm_response.content.parts[0].text

            try:
                armor.sanitize_output(original_text)
            except ValueError as e:
                print(f"Error sanitizing output: {e}")
                return LlmResponse(content=types.Content(
                    role="model",
                    parts=[types.Part(text="Model response was blocked." + e.__str__())],
                ))
    return None

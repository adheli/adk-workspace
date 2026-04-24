from google.api_core.client_options import ClientOptions
from google.cloud import modelarmor_v1


class ModelArmorService:
    """Service for sanitizing input and output using Google Cloud Model Armor."""

    def __init__(self, project_id: str, location: str, template_id: str):
        """Initializes the Model Armor service with project, location, and template details."""
        self.template = f"projects/{project_id}/locations/{location}/templates/{template_id}"
        self.client = modelarmor_v1.ModelArmorClient(
            transport="rest",
            client_options=ClientOptions(api_endpoint=self.template),
        )

    def sanitize_input(self, text: str) -> str:
        """Sanitizes the user input text using Model Armor."""
        user_prompt_data = modelarmor_v1.DataItem(text=text)
        request = modelarmor_v1.SanitizeUserPromptRequest(
            name=self.template,
            user_input=user_prompt_data,
        )

        response = self.client.sanitize_user_prompt(request=request)

        if response.blocked:
            raise ValueError(f"Input blocked: {response.reason}")

        return response.sanitized_text or text

    def sanitize_output(self, text: str) -> str:
        """Sanitizes the model response text using Model Armor."""
        model_response_data = modelarmor_v1.DataItem(text=text)
        request = modelarmor_v1.SanitizeModelResponseRequest(
            name=self.template,
            model_response_data=model_response_data,
        )

        response = self.client.sanitize_model_response(request=request)

        if response.blocked:
            raise ValueError(f"Output blocked: {response.reason}")

        return response.sanitized_text or text

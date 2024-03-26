import google.generativeai as genai
from core.env_variables import api_key


class GeminiApi:
    """
    Class to interact with Gemini API
    """

    def __init__(self, max_output_tokens, temperature, top_k, top_p) -> None:
        genai.configure(api_key=api_key)
        genai_config = genai.GenerationConfig(
            candidate_count=1,
            max_output_tokens=max_output_tokens,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p
        )
        self.model = genai.GenerativeModel(
            model_name="gemini-pro",
            generation_config=genai_config
        )
        pass

    def generate_answer(self, prompt):
        return self.model.generate_content(prompt)

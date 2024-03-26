from services.gemini_api import GeminiApi
from crud.prompt_spec import PromptSpec
from crud.characters_spec import CharactersSpec


class InteractionSpec:
    """
    Interaction Class
    """

    def __init__(self) -> None:
        self.prompts = PromptSpec()
        self.characters = CharactersSpec()
        self.gemini_api = GeminiApi(
            max_output_tokens=500,
            temperature=0.2,
            top_p=0.6,
            top_k=20,
        )
        pass

    def format_prompt(self, char_name, question) -> str: 
        prompt = self.prompts.get_prompt().get("prompt")
        char_context = self.characters.get_character_info(char_name)
        if not prompt or not char_context:
            return ""
        formatted_prompt = prompt.format(
            char_name = char_name,
            char_context = char_context,
            question = question
        )
        print("Prompt text sent to Gemini:", formatted_prompt)
        return formatted_prompt
    
    def ask_gemini(self, prompt):
        response = self.gemini_api.generate_answer(prompt).text
        return response


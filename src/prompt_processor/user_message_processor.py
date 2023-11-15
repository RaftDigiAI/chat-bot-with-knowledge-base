from src.llm.open_ai import process_prompt


class UserMessageProcessor:
    def process(self, user_message: str) -> str:
        try:
            print(f'Processing prompt: "{user_message}"')
            result = process_prompt(user_message)
            return result
        except Exception as e:
            print(f"Exception: {e}")
            return "An error occurred"

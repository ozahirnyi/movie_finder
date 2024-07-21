

class FindMovieAiClient:

    def __init__(self, prompt: str):
        self.prompt = prompt

    async def find_movies(self) -> list[str]:
        return None
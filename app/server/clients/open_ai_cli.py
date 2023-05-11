import os
import openai
from pydantic import BaseModel
from dotenv import load_dotenv

class Req(BaseModel):
    prompt: str

class Res(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: list[dict[str, int, None, str]]
    usage: dict[int, int, int]

class OpenAICli:
    
    def __init__(self) -> None:
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.chatModel = 'gpt-3.5-turbo'
    
    def chatCompletion(self, req: Req) -> Res:
    
        res = openai.ChatCompletion.create(
            model=self.chatModel,
            messages=[{
                'role': 'user',
                'content': req.prompt
            }]
        )
        print(res)
        return res
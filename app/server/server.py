from fastapi import FastAPI, WebSocket
from pydantic import BaseModel

from .clients.open_ai_cli import OpenAICli

class Req(BaseModel):
    prompt: str

class Server:
    
    def __init__(self) -> None:
        self.app = self._init_app()
        
    def _init_app(self) -> FastAPI:
        app = FastAPI()
        open_ai_client = OpenAICli()

        @app.get('/')
        async def healthcheck():
            return "Looks good!"
        
        @app.post('/api/v1/prompt')
        async def prompt(req: Req):
            return open_ai_client.chatCompletion(req)
        
        return app
from fastapi import APIRouter
from pydantic import BaseModel
import requests

llm_router = APIRouter()

class UserRequest(BaseModel):
    user_name: str

@llm_router.post('/llm_resume')
def resume(request: UserRequest):
    url = ''https://dbf00600ca05.ngrok-free.app/signin?redirect=%252F
    
    data = [
        {
            "headers": {
                "host": "localhost:5678",
                "user-agent": "python-requests/2.32.3",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept": "*/*",
                "connection": "keep-alive",
                "content-length": "384",
                "content-type": "application/json"
            },
            "params": {},
            "query": {},
            "body": [
                {
                    "headers": {
                        "host": "localhost:5678",
                        "user-agent": "python-requests/2.32.3",
                        "accept-encoding": "gzip, deflate, br, zstd",
                        "accept": "*/*",
                        "connection": "keep-alive",
                        "content-length": "26",
                        "content-type": "application/json"
                    },
                    "params": {},
                    "query": {},
                    "body": {
                        "user_name": request.user_name
                    },
                    "webhookUrl": "http://localhost:5678/webhook/llm_resume",
                    "executionMode": "production"
                }
            ],
            "webhookUrl": "http://localhost:5678/webhook/llm_resume",
            "executionMode": "production"
        }
    ]

    response = requests.post(url, json=data)
    return {
        "response": response.json() if response.headers.get("content-type") == "application/json" else response.text
    }

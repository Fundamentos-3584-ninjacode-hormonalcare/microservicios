from fastapi import APIRouter, Request, HTTPException
import requests
from configs.url_services import MICROSERVICE_COMMUNICATION

communication_router = APIRouter()

@communication_router.get("/communications/messages/{messageId}")
async def get_communication_by_id(request: Request, messageId: str):
    """
    Get a specific communication by ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/messages/{messageId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()

@communication_router.get("/communications/messages/conversation/{conversationId}")
async def get_messages_by_conversation_id(request: Request, conversationId: str):
    """
    Get a specific communication by conversation ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/messages/conversation/{conversationId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()

@communication_router.post("/communications/messages")
async def send_message(request: Request):
    """
    Create a new communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}/messages"
    response = requests.post(url, headers=request.headers, json=await request.json())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()

@communication_router.put("/communications/messages/{messageId}/status")
async def update_message_status(request: Request, messageId: str):
    """
    Update the status of an existing communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}/messages/{messageId}/status"
    response = requests.put(url, headers=request.headers, json=await request.json())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()

@communication_router.delete("/communications/messages/{messageId}")
async def delete_message(request: Request, messageId: str):
    """
    Delete a communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}/messages/{messageId}"
    response = requests.delete(url, headers=request.headers)
    if response.status_code != 204:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return {"message": "Communication deleted successfully"}





@communication_router.get("/communications/conversations/{conversationId}")
async def get_conversation_by_id(request: Request, conversationId: str):
    """
    Get a specific communication by ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/conversations/{conversationId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()

@communication_router.get("/communications/conversations/user/{profileId}")
async def get_conversation_by_profile_id(request: Request, profileId: str):
    """
    Get a specific communication by ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/conversations/user/{profileId}"
    response = requests.get(url, headers=request.headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()

@communication_router.post("/communications/conversations")
async def create_conversation(request: Request):
    """
    Create a new communication
    """
    url = f"{MICROSERVICE_COMMUNICATION}/conversations"
    response = requests.post(url, headers=request.headers, json=await request.json())
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()
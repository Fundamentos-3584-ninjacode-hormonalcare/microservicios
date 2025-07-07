from fastapi import APIRouter, Request, HTTPException, Path
from fastapi.responses import JSONResponse
import requests
from configs.url_services import MICROSERVICE_COMMUNICATION

communication_router = APIRouter()

# =============== MESSAGES ===============


@communication_router.get("/messages")
async def get_all_messages(request: Request):
    """
    Get all messages
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/messages"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.get("/messages/{messageId}")
async def get_message_by_id(request: Request, messageId: str = Path(...)):
    """
    Get a specific message by ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/messages/{messageId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.get("/messages/conversation/{conversationId}")
async def get_messages_by_conversation_id(request: Request, conversationId: str = Path(...)):
    """
    Get messages by conversation ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/messages/conversation/{conversationId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.post("/messages")
async def send_message(request: Request):
    """
    Send a new message
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/messages"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.put("/messages/{messageId}/status")
async def update_message_status(request: Request, messageId: str = Path(...)):
    """
    Update message status
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/messages/{messageId}/status"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.put(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.delete("/messages/{messageId}")
async def delete_message(request: Request, messageId: str = Path(...)):
    """
    Delete a message
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/messages/{messageId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"message": "Message deleted successfully"}
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})

# =============== CONVERSATIONS ===============


@communication_router.get("/conversations")
async def get_all_conversations(request: Request):
    """
    Get all conversations
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/conversations"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.get("/conversations/{conversationId}")
async def get_conversation_by_id(request: Request, conversationId: str = Path(...)):
    """
    Get a specific conversation by ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/conversations/{conversationId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.get("/conversations/user/{profileId}")
async def get_conversations_by_profile_id(request: Request, profileId: int = Path(...)):
    """
    Get conversations by profile ID
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/conversations/user/{profileId}"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})


@communication_router.post("/conversations")
async def create_conversation(request: Request):
    """
    Create a new conversation
    """
    url = f"{MICROSERVICE_COMMUNICATION}/communication/conversations"
    headers = {}
    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]
    try:
        response = requests.post(url, headers=headers, json=await request.json())
        response.raise_for_status()
        return response.json()
    except Exception:
        return JSONResponse(status_code=500, content={"detail": f"Communication error: {response.text}"})

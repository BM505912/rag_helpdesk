import os
import certifi
from fastapi import FastAPI
from app.api import router
from fastapi.middleware.cors import CORSMiddleware




#os.environ["SSL_CERT_FILE"] = certifi.where()

app = FastAPI(
    title="RAG Helpdesk Chatbot API",
    version="1.0.0"
)

#Agregue los CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
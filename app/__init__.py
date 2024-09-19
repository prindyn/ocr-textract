from fastapi import FastAPI
from fastapi.routing import APIRouter


def create_app() -> FastAPI:
    return FastAPI()


def create_router() -> APIRouter:
    return APIRouter()

# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request, Response, Query
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the TIDAL connector."}
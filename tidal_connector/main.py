# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the TIDAL connector."}
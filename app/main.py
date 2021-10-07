# -*- coding: utf-8 -*-

from fastapi import FastAPI, Request, Response, Query
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from starlette.responses import FileResponse
from rdflib import Graph

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the TIDAL connector. See https://github.com/MaastrichtU-IDS/tidal-connector for further information."}

@app.get("/get-pod-information")
async def root():
    fetchPodData()
    file_name = mergeFiles()
    file_location = "/app/" + file_name
    return FileResponse(file_location, media_type='application/octet-stream',filename=file_name)

async def mergeFiles():
    print("merging files")
    file_name = "merged_files.ttl"
    files = ["file1.ttl","file2.ttl","file3.ttl"]
    graph = Graph()
    for file in files:
        new_graph = Graph()
        new_graph.parse(file, format="turtle")
        graph = graph + new_graph
    graph.serialize(file_name, format="turtle")
    return file_name

async def fetchPodData():
    print("Fetching pod data")

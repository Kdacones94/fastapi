from doctest import debug
from fastapi import FastAPI
from .app/ import * # type: ignore

from neomodel import config, StructuredNode, StringProperty, IntegerProperty, RelationshipTo, RelationshipFrom # type: ignore 


# Configure the Neo4j database connection
config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

def main():
    pass  # Initialization logic already handled at the top of the file
    print("Starting the FastAPI application...")
    # Additional setup or initialization can be added here
    app = FastAPI(title="FastAPI with Neo4j Example", version="1.0.0", description="A simple FastAPI application connected to a Neo4j database.")



if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8000)
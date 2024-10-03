from ariadne.asgi import GraphQL
from fastapi import FastAPI
import uvicorn

from graphql_utils.resolvers import schema
from logger import get_logger


LOGGER = get_logger("gateway:main.py")

app = FastAPI()
graphql_app = GraphQL(schema, debug=True)
app.mount("/graphql", graphql_app)

@app.get("/")
async def get():
    LOGGER.info("GET / endpoint called")
    return {"info": "This is the Grapqhl Gateway Home"}

if __name__ == "__main__":
    uvicorn.run(app=app, port=8080, reload=True)
# gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
# https://stackoverflow.com/questions/63483246/how-to-call-an-api-from-another-api-in-fastapi

import os

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()


client = httpx.AsyncClient()


async def call_api(url: str):
    api_key = os.getenv("EVO_AUTH_TOKEN")
    headers = {
        "apikey": api_key,
        "content-type": "application/json"
    }
    params = {"getParticipants": "false"}
    r = await client.get(url, headers=headers, params=params)
    print(r.url)
    return r.text

app = FastAPI()


@app.get("/")
async def index():
    return {"msg": "Funcionou!"}


@app.get("/grupos")
async def fetch_all_groups():
    evo_base_url = os.getenv("EVO_BASE_URL")
    evo_instance_name = os.getenv("EVO_INSTANCE_NAME")
    url = f"http://{evo_base_url}/group/fetchAllGroups/{evo_instance_name}"
    text = await call_api(url)
    return text


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True, workers=1)

# gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
# https://stackoverflow.com/questions/63483246/how-to-call-an-api-from-another-api-in-fastapi
# https://stackoverflow.com/questions/63872924/how-can-i-send-an-http-request-from-my-fastapi-app-to-another-site-api

import os

import aiohttp
from dotenv import load_dotenv
from fastapi import Body, FastAPI

from core.settings import settings
from routes import tipo_solicitacao_router

load_dotenv()


async def call_api(url: str):
    api_key = os.getenv('EVO_AUTH_TOKEN')
    headers = {
        'apikey': api_key,
        'content-type': 'application/json'
    }
    params = {'getParticipants': 'false'}
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, params=params) as response:
            return await response.json()

app = FastAPI(title='Zaty API',
              version=settings.API_VERSION,
              description='API destinada ao projeto Zaty',
              )

app.include_router(tipo_solicitacao_router.router, tags=['Tipo Integração'])


@app.get('/')
async def index():
    return {'msg': 'Funcionou!'}


@app.get('/grupos')
async def fetch_all_groups():
    evo_base_url = os.getenv('EVO_BASE_URL')
    evo_instance_name = os.getenv('EVO_INSTANCE_NAME')
    url = f'http://{evo_base_url}/group/fetchAllGroups/{evo_instance_name}'
    text = await call_api(url)
    return text


@app.post('/grupos')
async def fetch_all_groups(evo_api_key=Body(''),
                           evo_base_url=Body(''),
                           evo_instance_name=Body('')):
    headers = {
        'apikey': evo_api_key,
        'content-type': 'application/json'
    }
    params = {'getParticipants': 'false'}

    url = f'http://{evo_base_url}/group/fetchAllGroups/{evo_instance_name}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers, params=params) as response:
            return await response.json()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                log_level='info', reload=True, workers=1)

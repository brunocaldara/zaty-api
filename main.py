# gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
# https://stackoverflow.com/questions/63483246/how-to-call-an-api-from-another-api-in-fastapi
# https://stackoverflow.com/questions/63872924/how-can-i-send-an-http-request-from-my-fastapi-app-to-another-site-api

import os

import aiohttp
from dotenv import load_dotenv
from fastapi import Body, FastAPI
from fastapi.openapi.docs import (get_swagger_ui_html,
                                  get_swagger_ui_oauth2_redirect_html)
from fastapi.openapi.utils import get_openapi

from src.api.v1 import api_routes
from src.core.settings import settings

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


# @app.get("/docs", include_in_schema=False)
# async def custom_swagger_ui_html():
#     # return get_swagger_ui_html(
#     #     openapi_url=app.openapi_url,
#     #     title=app.title,
#     #     oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
#     #     swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui-bundle.js",
#     #     swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3/swagger-ui.css")

#     return get_swagger_ui_html(
#         openapi_url=app.openapi_url,
#         title=f"{app.title} - Swagger UIAAAAA",
#         swagger_css_url="https://cdn.jsdelivr.net/gh/Itz-fork/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css"
#     )

# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Custom title",
#         version="2.5.0",
#         description="This is a very custom OpenAPI schema",
#         routes=app.routes,
#     )
#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://www.google.com/imgres?q=php&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F2%2F27%2FPHP-logo.svg&imgrefurl=https%3A%2F%2Fpt.wikipedia.org%2Fwiki%2FPHP&docid=NtM0wDWraxtdoM&tbnid=QRXpr0h-i79qeM&vet=12ahUKEwj0rYrz8cCJAxWJO7kGHW9vA5wQM3oECBsQAA..i&w=711&h=384&hcb=2&ved=2ahUKEwj0rYrz8cCJAxWJO7kGHW9vA5wQM3oECBsQAA"
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema


# app.openapi = custom_openapi

app.include_router(api_routes.router, prefix=settings.API_URL_VERISON)


@ app.get('/')
async def index():
    return {'msg': 'Zaty API funcionando!'}

# @app.get('/grupos')
# async def fetch_all_groups():
#     evo_base_url = os.getenv('EVO_BASE_URL')
#     evo_instance_name = os.getenv('EVO_INSTANCE_NAME')
#     url = f'http://{evo_base_url}/group/fetchAllGroups/{evo_instance_name}'
#     text = await call_api(url)
#     return text


# @app.post('/grupos')
# async def fetch_all_groups(evo_api_key=Body(''),
#                            evo_base_url=Body(''),
#                            evo_instance_name=Body('')):
#     headers = {
#         'apikey': evo_api_key,
#         'content-type': 'application/json'
#     }
#     params = {'getParticipants': 'false'}

#     url = f'http://{evo_base_url}/group/fetchAllGroups/{evo_instance_name}'

#     async with aiohttp.ClientSession() as session:
#         async with session.get(url=url, headers=headers, params=params) as response:
#             return await response.json()


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                log_level='info', reload=True, workers=1)

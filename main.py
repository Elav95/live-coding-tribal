import requests
from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()
url = "https://api.chucknorris.io/jokes/random/"

@app.get("/")
def index():
    response = RedirectResponse(url='/docs')
    return response

@app.post("/random", response_model=list[str])
async def random():
    lista = []
    while (len(lista) != 25):
        response = requests.get(url=url)
        response = response.json()
        if (response["id"] not in lista):
            lista.append(response["id"])
        else:
            pass
    return lista
    
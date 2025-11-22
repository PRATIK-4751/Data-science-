from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index()-> dict[str, str]:
    return {'message': 'Hello World'}


@app.get('/about')
async def about()-> str :
    return "message: This is the about page"




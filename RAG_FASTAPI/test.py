from fastapi import FastAPI,HTTPException
from pydantik import BandType , Band


app = FastAPI()



BANDS = [

    {'id': 1, 'name': 'Led Zeppelin' , 'type':"White"},
    {'id': 2, 'name': 'The Beatles' , 'type':"Black-white"},
    {'id': 3, 'name': 'Rolling Stones' , 'type':"Black"},
    {'id': 4, 'name': 'The Who' , 'type':"Black-other"},
]

@app.get('/bands')
async def get_bands()->list[Band]:
    return [Band(**band) for band in BANDS]

@app.get('/bands/{band_id}')
async def band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found!")
    return band 


@app.get('/')
async def index()-> dict[str, str]:
    return {'message': 'Welcome to the Bands API'}


@app.get('/about')
async def about()-> str :
    return "This is the about page"

@app.get('/bands/name/{band_name}')
async def band_by_name(band_name: str) -> dict:
    band = next((b for b in BANDS if b['name'].lower() == band_name.lower()), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band not found!")
    return band

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {"message": "No favicon available"}


    
@app.get('/bands/type/{band_type}')
async def bands_for_type(band_type: str)-> list[dict]:
    band_type_lower = band_type.lower()
    return [
        b for b in BANDS if b['type'].lower() == band_type_lower
    ]


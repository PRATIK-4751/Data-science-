from fastapi import FastAPI,HTTPException
from pydantik import BandType , Band
from datetime import date
from typing import Optional


app = FastAPI()



BANDS = [

    {'id': 1, 'name': 'Led Zeppelin', 'type': BandType.WHITE},
    {'id': 2, 'name': 'The Beatles', 'type': BandType.BLACK_WHITE},
    {'id': 3, 'name': 'Rolling Stones', 'type': BandType.BLACK, 'albums': [{'title': 'the nigga of America!', 'release_date': date(2023, 1, 1)}]},
    {'id': 4, 'name': 'The Who', 'type': BandType.BLACK_OTHER},
]

@app.get('/bands')
async def get_bands(
    band_type: Optional[BandType] = None, 
    name: Optional[str] = None,
    has_albums: Optional[bool] = None
)->list[Band]:
    filtered_bands = BANDS
    if band_type:
        filtered_bands = [b for b in filtered_bands if b.get('type') == band_type]
    if name:
        filtered_bands = [b for b in filtered_bands if name.lower() in b.get('name', '').lower()]
    if has_albums is not None:
        if has_albums:
            filtered_bands = [b for b in filtered_bands if b.get('albums') and len(b.get('albums', [])) > 0]
        else:
            filtered_bands = [b for b in filtered_bands if not b.get('albums') or len(b.get('albums', [])) == 0]
    
    return [Band(**band) for band in filtered_bands]

@app.get('/bands/{band_id}')
async def band(band_id: int) -> Band:
    band_dict = next((b for b in BANDS if b['id'] == band_id), None)
    if band_dict is None:
        raise HTTPException(status_code=404, detail="Band not found!")
    return Band(**band_dict) 


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


from fastapi import HTTPException

def validate_sector(sector: str):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")
from fastapi import HTTPException

ALLOWED_SECTORS = [
    "technology",
    "pharmaceuticals",
    "agriculture",
    "banking",
    "finance",
    "automobile",
    "telecom"
]

def validate_sector(sector: str):
    if sector.lower() not in ALLOWED_SECTORS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sector. Choose from: {ALLOWED_SECTORS}"
        )

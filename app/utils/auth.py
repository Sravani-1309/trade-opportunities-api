from fastapi import Header, HTTPException

def verify_user(
    x_api_key: str = Header(None, alias="x-api-key")
):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API key required")

    if x_api_key != "mysecretkey":
        raise HTTPException(status_code=401, detail="Invalid API key")

    return x_api_key

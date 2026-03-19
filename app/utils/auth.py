from fastapi import Header, HTTPException, Query

def verify_user(
    x_api_key: str = Header(None, alias="x-api-key"),
    api_key: str = Query(None)
):
    key = x_api_key or api_key

    if not key:
        raise HTTPException(status_code=401, detail="API key required")

    if key != "mysecretkey":
        raise HTTPException(status_code=401, detail="Invalid API key")

    return key

from fastapi import Header, HTTPException

def verify_user(
    x_api_key: str = Header(None, alias="x-api-key"),
    api_key: str = Query(None)
):
    key = x_api_key or api_key

    if key != "mysecretkey":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return key

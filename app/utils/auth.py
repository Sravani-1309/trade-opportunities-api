from fastapi import Header, HTTPException

def verify_user(api_key: str = Header(None, alias="x-api-key")):
    print("Received API KEY:", api_key)
    if api_key != "mysecretkey":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key
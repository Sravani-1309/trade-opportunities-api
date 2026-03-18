from fastapi import APIRouter, Depends, Request, HTTPException, Query
from app.services.data_service import get_market_data
from app.services.ai_service import analyze_data
from app.services.report_service import generate_report
from app.utils.auth import verify_user
from app.utils.validator import validate_sector
from app.utils.rate_limiter import limiter
from app.utils.session import track_session

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
def analyze_sector(request: Request, sector: str, user=Depends(verify_user)):

    validate_sector(sector)

    # 🔥 ADD THIS LINE
    session_count = track_session(user)
    print(f"User called API {session_count} times")

    try:
        data = get_market_data(sector)
        analysis = analyze_data(data, sector)
        report = generate_report(sector, analysis)

        return {
            "report": report,
            "session_calls": session_count   # optional but good
        }

    except Exception as e:
        print("Error:",e)
        raise HTTPException(status_code=500, detail=str(e))

from fastapi import FastAPI, HTTPException, Depends
from backend.models.user_services import User_Services
import Admin, Developer, Item, Student, User
import os


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/reset")
def reset(user_service: User_Services = Depends()) -> str:
    """Development-only route for resetting storage module and adding fake user and checkin."""
    if "MODE" in os.environ and os.environ["MODE"] == "production":
        raise HTTPException(status_code=404, detail="Not Found")
    else:
        user_service.reset()
        user_service.create_user(User("Kevin", "Dai", "9197714705", "kevindai@email.unc.edu", "kevindai", "1234567890!"))
        return "OK"
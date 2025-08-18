from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#User profile management application

class UserProfile(BaseModel):
    id: int
    name: str
    email: str

# Fake database
database = []

@app.post("/profiles")
def create_user(profile: UserProfile):
    database.append(profile.dict())
    return {"message":"User profile created successfully", "profile": profile}

@app.get("/profiles")
def get_profiles():
    if not database:
        raise HTTPException(status_code=404, detail="No profiles fount")
    return {"profiles": database}

@app.get("/profiles/{profile_id}")
def get_id_profile(profile_id: int):
    for profile in database:
        if profile["id"] == profile_id:
            return {"profile": profile}
    raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/profiles/{profile_id}")
def update_profile(profile_id: int, profile: UserProfile):
    for i, existing_profile in enumerate(database):
        if existing_profile['id'] == profile_id:
            database[i] = profile.dict()
            return {"message": "Profile updated successfully", "profile": profile}
    raise HTTPException(status_code=404, detail="Profile not found")

@app.delete("/profiles/{profile_id}")
def delete_profile(profile_id: int):
    for i, profile in enumerate(database):
        if profile["id"] == profile_id:
            delete_profile = database.pop(i)
            return {"message": "Profile deleted successfully", "profile": delete_profile}
    raise HTTPException(status_code=404, detail="Profile not found")
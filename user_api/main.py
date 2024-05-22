from fastapi import FastAPI, HTTPException
from typing import List
from models import User

app = FastAPI()

# Временное хранилище пользователей
users = []


@app.get("/users", response_model=List[User])
def get_users():
    return users


@app.post("/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for idx, user in enumerate(users):
        if user.id == user_id:
            users[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    for idx, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(idx)
            return deleted_user
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

from uuid import UUID

from fastapi import FastAPI

from models.course import Course
from models.player import Player

app = FastAPI()


players: dict[UUID, Player] = {}
courses: dict[UUID, Course] = {}

@app.get("/players")
# @app.post("/players")
# @app.put("/players/{player_id}")
# @app.delete("/players/{player_id}")

@app.get("/courses")
# @app.post("/courses")
# @app.put("/courses/{courses_id}")
# @app.delete("/courses/{courses_id}")

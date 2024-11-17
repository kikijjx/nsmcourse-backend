from fastapi import FastAPI
from app.routers.theme import theme_router
from app.routers.course import course_router
from app.routers.experiments import experiment_router
from app.routers.auth import auth_router


from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(theme_router)
app.include_router(course_router)
app.include_router(experiment_router)
app.include_router(auth_router)


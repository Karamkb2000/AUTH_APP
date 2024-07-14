from fastapi import FastAPI
from database.database import engine, Base
from auth.auth import auth_router
from routes.users import users_router

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Include authentication and user routers
app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/users")
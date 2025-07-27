import uvicorn
from fastapi import FastAPI

from src.modules.users.user_router import router as users_router
from src.modules.projects.project_router import router as projects_router
# Add GHL router when ready:
# from src.modules.integrations.gohighlevel.ghl_service import router as ghl_router

app = FastAPI(title="GHQ Project Manager", version="0.1.0")

# Register all routers
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(projects_router, prefix="/projects", tags=["Projects"])
# app.include_router(ghl_router, prefix="/ghl", tags=["GoHighLevel"])

if __name__ == "__main__":
    # Run the development server
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)

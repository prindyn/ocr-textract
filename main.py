import uvicorn
from app import create_app
from app.routes import router

app = create_app()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

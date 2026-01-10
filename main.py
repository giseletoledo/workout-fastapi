from fastapi import FastAPI
from routers import api_router

app = FastAPI()
app.include_router(api_router)

""" @app.get("/")
def root():
    return {"message": "Workout API running"} """



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", reload=True)
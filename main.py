from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "VoiceForge: Axel backend is alive!"}


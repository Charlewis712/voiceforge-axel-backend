from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
import shutil
import zipfile
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "VoiceForge: Axel backend is alive!"}

@app.post("/train")
async def train(file: UploadFile = File(...)):
    try:
        os.makedirs("datasets", exist_ok=True)
        zip_path = f"datasets/{file.filename}"
        with open(zip_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall("datasets/training_data")

        return {"message": "Training data received and extracted."}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/convert")
async def convert(file: UploadFile = File(...), model_name: str = Form(...)):
    try:
        os.makedirs("output", exist_ok=True)
        output_path = f"output/converted.wav"

        # Fake conversion (just saves the uploaded .wav file for now)
        with open(output_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return FileResponse(output_path, media_type="audio/wav", filename="converted.wav")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from jantung import process_jantung_data
from ranap import process_ranap_data
from resumemedis import process_resumemedis_data
import os
import io

app = FastAPI(title="Extraction APIs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Extraction APIs"}

@app.post("/Extract-Jantung")
async def extract_jantung(file: UploadFile = File(...)):
    try:
        # Simulating processing
        file_contents = await file.read()
        logging.info(f"File {file.filename} uploaded successfully with size {len(file_contents)} bytes.")
        
        # Instead of calling jantung.py, just simulate processing and return a success response
        return JSONResponse({"status": "success", "message": "File processed successfully."})
    except Exception as e:
        logging.error(f"Error processing file: {str(e)}")
        return JSONResponse({"status": "error", "error": str(e)}, status_code=500})




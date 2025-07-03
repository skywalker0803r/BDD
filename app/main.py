# app/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    # 模擬 landing frame 推論
    return JSONResponse(content={"landing_frame": {"x": 100, "y": 200}})

from fastapi import FastAPI, HTTPException, UploadFile
import requests
import os
import socket
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()

@app.get("/development")
async def root():
    return {"response": "test"}


@app.post("/send/{date}")
async def message(date: str, file: UploadFile):
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="not csv")
    try:
        content = await file.read()
        response = requests.put(
            f"http://{os.getenv('DOCKER_NETWORK')}:{os.getenv('SERVICE_PORT')}/receive_file/{date}",
            files= { "app_data": [file.filename,content, file.content_type] }
        )
        return {"detail":"file contents sent successfully", "status_code": response.status_code, "content": response.content}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail={f"Error sending file: {e}"})

@app.delete("/delete")
async def delete():
    try:
        response = requests.delete(
            f"http://{os.getenv('DOCKER_NETWORK')}:{os.getenv('SERVICE_PORT')}/dev/delete_data")
        
        return {"detail":"Deletion triggered, please verify DB", "status_code": response.status_code, "content": response.content}
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail={f"Error sending file: {e}"})


  



# LOCAL DEVELOPMENT
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app="api_app:app", host="0.0.0.0", port=8014, reload=True)

from fastapi import FastAPI, HTTPException, UploadFile

app = FastAPI()

@app.get("/dev/dev_root")
async def root():
    return {"response": "test response"}


@app.put("/receive_file/{date}")
async def receive_file(date:str, app_data: UploadFile):
    
    import os
    import subprocess

    if app_data.content_type != "text/csv":
        raise HTTPException(status_code=400, detail=f"wrong file type: {app_data.content_type}")
    
    upload_dir = '../load-data-file-service/app/workers/app_data'

    file_path = os.path.join(upload_dir, app_data.filename)

    with open(file_path, 'wb') as f:
        while contents := await app_data.read(1024*1024):
            f.write(contents)
    
    subprocess.run(f"python ./app/begin_process.py {date} {app_data.filename}", shell=True)

    return {"filename", app_data.filename, "received"}


@app.delete("/dev/delete_data")
def delete_data():
    
    import app.workers.db as db

    try:

        with db.cursor:
            
            db.cursor.execute(f"DELETE FROM FILE_NAME;")
            db.cursor.execute(f"DELETE FROM FILE_DATA;")
            
            db.cursor.commit()
    except db.pyodbc.Error as err:
            return {"response": f"Error: {err}"}

    return {"response": f"Database cleared"}
    
# LOCAL DEVELOPMENT
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app="api_app:app", host="0.0.0.0", port=8015, reload=True)

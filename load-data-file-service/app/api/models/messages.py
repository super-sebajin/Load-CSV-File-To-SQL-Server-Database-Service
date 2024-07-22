from typing import Optional 
from pydantic import BaseModel, Field
from fastapi import UploadFile

class Message(BaseModel):
    payload: UploadFile
    # hostname: str = None
    # port: str = None
   
class LoadFileToDb(BaseModel):
    file_name: str = None
    line_count: str = None
    

    
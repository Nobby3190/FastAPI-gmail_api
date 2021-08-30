from pydantic import BaseSettings

from typing import Any, List, Optional


class Settings(BaseSettings): # 針對不同的環境設計不一樣的設定
    CLIENT_SECRET_FILE: str = "credentials.json"
    API_NAME: str = "gmail"
    API_VERSION = "v1"
    SCOPES = ['https://mail.google.com/']
    
    class Config:
        env_file = ".env" # 可針對不同環境載入不同dotenv設定檔
        
    
    
settings = Settings()
from pathlib import Path
import uvicorn
import os
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

if __name__ == "__main__":
    should_reload = False
    if os.getenv('APP_ENV') == 'dev':
        should_reload = True

    uvicorn.run("server.app:app", host="0.0.0.0", port=int(os.getenv('APP_PORT')), reload=should_reload, workers=1)


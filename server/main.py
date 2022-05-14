from fastapi import FastAPI

app = FastAPI()


@app.get('/status')
async def status():
    return {'status': 200, 'message': 'OK'}

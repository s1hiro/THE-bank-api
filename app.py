from fastapi import FastAPI

app = FastAPI(title="Bank API")

@app.get("/test")
async def test():
    return {"message": "This is a test!"}
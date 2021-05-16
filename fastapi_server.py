from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/fastapi")
async def index():
    return Response("Hello, World!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

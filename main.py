

from fastapi import FastAPI , Response
app = FastAPI()

@app.get("/")
async def hello_world():
    with open("./html/home.html", "r") as f:
        home_file = f.read()
    return Response(
        home_file,
        media_type="html"
    )
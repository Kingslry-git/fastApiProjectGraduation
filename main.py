from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

print("test")
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

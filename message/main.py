from fastapi import FastAPI

app = FastAPI()

@app.get("/list")
async def list_messages():
    """Returns list of messages"""
    return {"messages": ["list of messages"]}

@app.get("/message") # update to /{id}
async def get_message():
    """Returns details of a message"""
    return {"id": "123"}

@app.post("/create")
async def create_message():
    """Creates a message"""
    return {"id": "123"}

@app.post("/update")
async def update_message():
    """Updates a message"""
    return {"success": True}

@app.post("/delete")
async def delete_message()
    """Deletes a message"""
    return {"success": True}

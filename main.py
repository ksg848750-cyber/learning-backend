from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def get_events():
    return {'result':"Hello"}


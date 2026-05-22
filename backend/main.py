from fastapi import FastAPI
app = FastAPI()
@app.get("/")

def root():
    return {"message": "esse troço de API esta funcionando"}





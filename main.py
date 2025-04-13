from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Servidor activo"}

@app.post("/orden")
async def recibir_orden(request: Request):
    data = await request.json()
    print("Orden recibida:", data)
    return {"mensaje": "orden recibida", "datos": data}

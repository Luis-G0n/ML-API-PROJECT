from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pickle
import os

# Verifica se o modelo existe antes de tentar carregá-lo
model_path = 'model/modelo.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"O modelo não foi encontrado em {model_path}")

# Carrega o modelo
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Inicializa a API
app = FastAPI(title="Casa Barata API")

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquema simplificado
class InputData(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    floors: float
    yr_built: int
    lat: float
    long: float

@app.get("/")
def home():
    return {"message": "Casa Barata API"}

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[
        data.bedrooms,
        data.bathrooms,
        data.sqft_living,
        data.floors,
        data.yr_built,
        data.lat,
        data.long
    ]])

    try:
        prediction = model.predict(input_array)[0]
        return {"previsao_de_preco": round(prediction, 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na previsão: {str(e)}")

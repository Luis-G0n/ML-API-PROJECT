# 🏡 Casa Barata API

API desenvolvida com **FastAPI** para prever o preço de casas com base em características como número de quartos, banheiros, área, localização e ano de construção. O modelo de Machine Learning foi treinado usando um dataset de imóveis e serializado com `pickle`.

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [NumPy](https://numpy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [CORS Middleware](https://fastapi.tiangolo.com/tutorial/cors/)

---

## 📁 Estrutura do Projeto

ML-API-PROJECT/ 
├── model/ 
│ └── modelo.pkl 
├── main.py 
├── requirements.txt 
└── README.md


---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/casa-barata-api.git
```

```bash
cd casa-barata-api
```

 ## 📦 Crie um ambiente virtual e ative:
    
```bash
python -m venv venv # Windows
venv\Scripts\activate # Mac/Linux
source venv/bin/activate
```

   ##  Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Executando a API

```bash
uvicorn main:app --reload
```

## Acesse a documentação interativa da API em:

    Swagger: http://localhost:8000/docs

    Redoc: http://localhost:8000/redoc

## 📥 Endpoint de Previsão
POST /predict

Envia os dados da casa para obter a previsão do preço.
## ✅ Exemplo de JSON de entrada:

```bash
{
  "bedrooms": 3,
  "bathrooms": 2.0,
  "sqft_living": 1800,
  "floors": 1.0,
  "yr_built": 1995,
  "lat": 47.5112,
  "long": -122.257
}

```

## 🔁 Resposta esperada:

```bash
{
  "previsao_de_preco": 450000.0
}
```

## 📌 Observações

    O modelo atual pode retornar preços muito altos caso os dados de entrada estejam fora da distribuição esperada.

    Certifique-se de que os dados estão na mesma escala e unidade usada durante o treinamento do modelo.

    Se os valores parecerem irreais, verifique a normalização dos dados ou reavalie a performance do modelo com técnicas de validação.

## 🧠 Treinamento do Modelo

O modelo foi treinado com:

    Features: bedrooms, bathrooms, sqft_living, floors, yr_built, lat, long

    Algoritmo: LinearRegression

    Ferramenta de serialização: pickle

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    """
    Função que diz oi!
    """
    return {"mensagem":"Olá Pessoas"}

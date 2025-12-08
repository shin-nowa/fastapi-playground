from fastapi import FastAPI

app = FastAPI() # Criando a instância fastapi, a variavel app vira uma instancia da classe FastAPI

@app.get("/")
async def root():
    return {"mensagem": "Hello World"} # Retorna em JSON
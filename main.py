from fastapi import FastAPI
# from enum import Enum


# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
    
app = FastAPI() # Criando a instância fastapi, a variavel app vira uma instancia da classe FastAPI

@app.get("/items/{item_id}") # buscando em /items/item_id
def read_item(item_id: int): # parsing para int, se botar string náo vai.
    return {"item_id": item_id} # Retorna em JSON


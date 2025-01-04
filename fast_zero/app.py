from fastapi import FastAPI 

app = FastAPI()  

@app.get('/{id}')  
def read_root(id: int):  
    return {'message': 'Olá Mundo! ' + str(id)}
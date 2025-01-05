from fastapi import FastAPI

app = FastAPI(description='API para testar o FastAPI', title='FastAPI Zero')


@app.get('/', description='Retorna uma mensagem de boas-vindas')
def read_root():
    return {'message': 'Olá Mundo!'}

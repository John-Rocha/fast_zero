from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(description='API para testar o FastAPI', title='FastAPI Zero')

user_list = []


@app.get(
    '/',
    description='Retorna uma mensagem de boas-vindas',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get(
    '/users/',
    description='Retorna uma lista de usuários',
    status_code=HTTPStatus.OK,
    response_model=UserList,
)
def read_users():
    return {'users': user_list}


@app.post(
    '/users/',
    description='Cria um novo usuário',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def create_user(user: UserSchema):
    user_with_id = UserDB(
        id=len(user_list) + 1,
        **user.model_dump(),
    )

    user_list.append(user_with_id)

    return user_with_id

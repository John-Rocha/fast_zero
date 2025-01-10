from http import HTTPStatus

from fastapi import FastAPI, HTTPException

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


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    user_index = next(
        (index for index, user in enumerate(user_list) if user.id == user_id),
        None,
    )

    if user_index is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    user_list[user_index] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    user_index = next(
        (index for index, user in enumerate(user_list) if user.id == user_id),
        None,
    )

    if user_index is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del user_list[user_index]

    return {'message': 'User deleted'}

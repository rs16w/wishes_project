import datetime
import time
from datetime import timedelta
from enum import Enum
from typing import Union, Annotated, Any
from uuid import UUID

from datetime import datetime, time, timedelta
from typing import Union
from uuid import UUID

from fastapi import FastAPI, Path, Query, Body, Cookie, Header

from pydantic import BaseModel, Field, EmailStr
from enum import IntEnum

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, UUID4
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uuid

app = FastAPI()


class UserBase(BaseModel):
    nickname: str = Field(
        default='John Doe', max_length=50, examples=['John Doe']
    )


class UserCreated(UserBase):
    uuid: UUID4 = Field(
        default=uuid.uuid4()
    )


class WishBase(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float | None = Field(default=None, examples=[3.2])
    owner: UserBase


class WishCreated(WishBase):
    uuid: UUID4


# ________________WISHES________________
@app.post("/wishes", tags=['wishes'], response_model=WishCreated)
async def create_wish(wish: WishBase = Body()) -> Any:
    return WishCreated(uuid=uuid.uuid4(), **wish.model_dump())


@app.get("/wishes", tags=['wishes'])
async def get_wishes_list():
    return ['all_list']


@app.get("/wishes/{wish_id}", tags=['wishes'])
async def get_wish(wish_id: Annotated[int, Path(title="The ID of the wish item to get", ge=0, example=1)]):
    return wish_id


@app.patch("/wishes/{wish_id}", tags=['wishes'])
async def update_item(wish_id: Annotated[int, Path(title="The ID of the wish item to get", ge=0, example=1)],
                      wish: WishBase):
    results = {"item_id": wish_id, "wish": wish}
    return results


# ________________Users________________
@app.post("/users", tags=['users'], response_model=UserCreated)
async def create_user(user: UserBase = Body()) -> Any:
    return UserCreated(uuid=uuid.uuid4(), **user.model_dump())


@app.get("/users", tags=['users'])
async def get_users_list():
    return ['all_list']


@app.get("/users/{user_id}", tags=['users'])
async def get_user(user_id: Annotated[int, Path(title="The ID of the user to get", ge=0, example=1)]):
    return user_id


@app.patch("/users/{user_id}", tags=['users'])
async def update_user(user_id: Annotated[int, Path(title="The ID of the wish item to get", ge=0, example=1)],
                      user: UserBase):
    results = {"user_id": user_id, "wish": user}
    return results

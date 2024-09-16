# generated by datamodel-codegen:
#   filename:  0.DOIP_Op.Hello-Request.json
#   timestamp: 2024-09-16T07:45:06+00:00

from __future__ import annotations

from typing import Optional, Union

from pydantic import BaseModel, Extra, Field


class Authentication(BaseModel):
    class Config:
        extra = Extra.forbid

    username: Optional[str] = None
    password: Optional[str] = None


class Authentication1(BaseModel):
    class Config:
        extra = Extra.forbid

    token: Optional[str] = None


class Authentication2(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Optional[str] = None


class Model(BaseModel):
    class Config:
        extra = Extra.forbid

    requestId: Optional[str] = Field(
        None,
        description='requestId: the identifier of the request provided by the client; shall be unique within a given DOIP session so clients can distinguish between DOIP service responses. The requestId shall be a string not exceeding 4096 bits.',
    )
    targetId: str = Field(
        ...,
        description='targetId: the identifier of the DO on which the operation is to be invoked; the DOIP service could itself be the target.',
    )
    operationId: str = Field(
        '0.DOIP/Op.Hello',
        const=True,
        description='operationId: the identifier of the operation to be performed.',
    )
    authentication: Optional[
        Union[Authentication, Authentication1, Authentication2]
    ] = Field(
        None,
        description='authentication: optional JSON object used by clients to authenticate.',
    )

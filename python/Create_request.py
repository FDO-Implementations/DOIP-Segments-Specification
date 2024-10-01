# generated by datamodel-codegen:
#   filename:  0.DOIP_Op.Create-Request.json
#   version:   0.26.0

from __future__ import annotations

from typing import Any, Dict, Optional, Union

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


class Elements(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str = Field(
        ..., description='id: identifier of the element; must be unique within a DO.'
    )
    length: Optional[str] = Field(None, description='length of the data portion.')
    type: str = Field(
        ...,
        description='requestId: the identifier of the request provided by the client; shall be unique within a given DOIP session so clients can distinguish between DOIP service responses. The requestId shall be a string not exceeding 4096 bits.',
    )
    attributes: Optional[Dict[str, Any]] = Field(
        None,
        description='one or more fields serialized as an object using the default serialization, or as a JSON (sub) object.',
    )


class DoipDoSerialization(BaseModel):
    class Config:
        extra = Extra.forbid

    id: str = Field(..., description='id: the identifier of the DO.')
    type: str = Field(
        ...,
        description='type: the DO type. Must be 0.TYPE/DO or its extension. See Types section.',
    )
    attributes: Optional[Dict[str, Any]] = Field(
        None,
        description='attributes: one or more fields (key-value pairs) serialized as a JSON (sub) object.',
    )
    elements: Optional[Elements] = Field(
        None,
        description='description: one or more elements serialized as an array in the default serialization, with each element consisting of',
    )
    signatures: Optional[str] = Field(
        None,
        description='Required for DOs of type 0.TYPE/DOIPServiceInfo and 0.TYPE/DOIPOperation; otherwise optional. The field is an array of strings in the default serialization; each string is in JWS format19 with an unencoded detached payload.',
    )


class CreateRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    requestId: Optional[str] = Field(
        None,
        description='requestId: the identifier of the request provided by the client; shall be unique within a given DOIP session so clients can distinguish between DOIP service responses. The requestId shall be a string not exceeding 4096 bits.',
    )
    clientId: Optional[str] = Field(
        None, description='clientId: the identifier of the client.'
    )
    targetId: str = Field(
        ...,
        description='targetId: the identifier of the DO on which the operation is to be invoked; the DOIP service could itself be the target.',
    )
    operationId: str = Field(
        '0.DOIP/Op.Create',
        const=True,
        description='operationId: the identifier of the operation to be performed.',
    )
    authentication: Optional[
        Union[Authentication, Authentication1, Authentication2]
    ] = Field(
        None,
        description='authentication: optional JSON object used by clients to authenticate.',
    )
    input: Optional[DoipDoSerialization] = Field(
        None,
        description="Input: a serialized digital object. The default serialization may be used if the object lacks element data; otherwise the serialization is a multi-segment DO serialization as described above. The 'id' can be omitted to ask the DOIP service to automatically choose the id.",
    )

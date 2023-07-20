from pydantic import BaseModel, Field, ConfigDict


class TgUser(BaseModel):
    id: int
    username: str | None


class Massage(BaseModel):
    massage_id: int
    text: str | None
    _from: TgUser = Field(alias='from')

    model_config = ConfigDict(populate_by_name=True)



class UpdateObj(BaseModel):
    update_id: int
    massage: Massage


class GetUpdatesResponse(BaseModel):
    ok: bool
    result: list[UpdateObj]


class SendMassageResponse(BaseModel):
    ok: bool
    result: Massage

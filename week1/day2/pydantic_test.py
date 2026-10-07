from pydantic import BaseModel, ValidationError, Field

class LLm_config(BaseModel):
    model_name: str
    temprature: float = Field(ge=0.0, le=1.0)
    max_tokens: int


raw = {
    "model_name": "gpt-3.5-turbo",
    "temprature": 0.7,
    "max_tokens": 1024
}

config = LLm_config.model_validate(raw)
print(config)

print()

bad_raw = {
    "model_name": 2,
    "temprature":" 1.7",
    "max_tokens": None
}

try:
    bad_config = LLm_config.model_validate(bad_raw)
except ValidationError as e:
    print(e)

print()

#serialization

serialized = config.model_dump()
print(serialized)
print(type(serialized))

print()

json_serialized = config.model_dump_json()
print(json_serialized)
print(type(json_serialized))
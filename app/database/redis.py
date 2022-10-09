from app import main
import json


async def write_redis(key: int, value: json):
    rd = main.app.state.rd
    print(value)
    try:
        value_json = json.dumps(value)
        res = await rd.set(key, value_json)
    except:
        return False
    else:
        return True


async def read_redis(key: int):
    rd = main.app.state.rd
    value = await rd.get(key)

    if value is None:
        return False
    else:
        return json.loads(value)

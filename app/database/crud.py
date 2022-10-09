from app import main
from typing import Union


async def read(columns: str, table: str, where: Union[str, None] = None):
    pool = main.app.state.db_pool

    async with pool.acquire() as conn:
        cur = await conn.cursor()
        if where:
            await cur.execute(f"SELECT {columns} FROM {table} WHERE {where}")
        else:
            await cur.execute(f"SELECT {columns} FROM {table}")
        res = await cur.fetchall()

    return res


async def create(table: str, request_dict: dict):
    pool = main.app.state.db_pool
    columns = tuple(request_dict.keys())
    datas = tuple(request_dict.values())
    sql_query = f"INSERT INTO {table} {columns} VALUES".replace("'", "")
    sql_query += f"{datas}"
    async with pool.acquire() as conn:
        cur = await conn.cursor()
        try:
            await cur.execute(sql_query)
            await conn.commit()
        except Exception as e:
            return e
        else:
            new_id = cur.lastrowid

            if new_id:
                result = new_id
            return result



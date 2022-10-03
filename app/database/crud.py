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
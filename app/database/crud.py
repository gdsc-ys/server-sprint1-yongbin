from app import main


async def read_list(columns: str, table: str):
    pool = main.app.state.db_pool

    async with pool.acquire() as conn:
        cur = await conn.cursor()
        await cur.execute(f"SELECT {columns} FROM {table}")
        res = await cur.fetchall()

    return res
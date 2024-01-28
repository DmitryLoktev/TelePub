from src.common.db.models import async_session, User, Book
from sqlalchemy import select, insert


async def add_user(tg_link, tg_name, tg_id, time_on):
    try:
        async with async_session() as session:
            statement = (
                insert(User)
                .values(tg_link=tg_link, tg_name=tg_name, tg_id=tg_id, time_on=time_on)
            )
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(f"Ошибка при обновлении данных: {e}")


async def add_book(pub, name, tg_name, tg_link, tg_id, phone, date, time, quantity, wish):
    try:
        async with async_session() as session:
            statement = (
                insert(Book)
                .values(pub=pub, name=name, tg_name=tg_name, tg_link=tg_link, tg_id=tg_id, phone=phone, date=date,
                        time=time, quantity=quantity, wish=wish)
            )
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(f"Ошибка при обновлении данных: {e}")


async def get_tapboard(pub):
    try:
        async with async_session() as session:
            result = await session.execute(select(pub))
            tapboard = result.scalars().all()
            return tapboard
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return []


def format_table(data):
    table = "NUM |  NAME | BREWERY | ABV % | STYLE | PRICE (0.33/0.5/1) \n"
    table += "-" * 90 + "\n"
    for row in data:
        table += f"{row.id}. <b>{row.name}</b> | {row.brewery} | {row.abv} | {row.style}  \n {row.price} \n\n "
    return table


async def get_bottled(table):
    try:
        async with async_session() as session:
            result = await session.execute(select(table))
            tapboard = result.scalars().all()
            return tapboard
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return []

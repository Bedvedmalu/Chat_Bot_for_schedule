from app.database.models import async_session
from app.database.models import Group, Day, First, Second, Third, Fourth, Fifth, Six, Seven, Eight, Nine, First_up, \
    Second_up, Third_up, Fourth_up, Fifth_up, Six_up, Seven_up, Eight_up, Nine_up
from sqlalchemy import select, update, delete


async def get_groups():
    async with async_session() as session:
        return await session.scalars(select(Group))


async def get_group_day(group_id):
    async with async_session() as session:
        return await session.scalars(select(Day))


async def get_schedule1(day_id):
    async with async_session() as session:
        return await session.scalar(select(First).where(First.id == day_id))


async def get_schedule2(day_id):
    async with async_session() as session:
        return await session.scalar(select(Second).where(Second.id == day_id))


async def get_schedule3(day_id):
    async with async_session() as session:
        return await session.scalar(select(Third).where(Third.id == day_id))


async def get_schedule4(day_id):
    async with async_session() as session:
        return await session.scalar(select(Fourth).where(Fourth.id == day_id))


async def get_schedule5(day_id):
    async with async_session() as session:
        return await session.scalar(select(Fifth).where(Fifth.id == day_id))


async def get_schedule6(day_id):
    async with async_session() as session:
        return await session.scalar(select(Six).where(Six.id == day_id))


async def get_schedule7(day_id):
    async with async_session() as session:
        return await session.scalar(select(Seven).where(Seven.id == day_id))


async def get_schedule8(day_id):
    async with async_session() as session:
        return await session.scalar(select(Eight).where(Eight.id == day_id))


async def get_schedule9(day_id):
    async with async_session() as session:
        return await session.scalar(select(Nine).where(Nine.id == day_id))



async def get_schedule1_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(First_up).where(First_up.id == day_id))


async def get_schedule2_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Second_up).where(Second_up.id == day_id))


async def get_schedule3_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Third_up).where(Third_up.id == day_id))


async def get_schedule4_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Fourth_up).where(Fourth_up.id == day_id))


async def get_schedule5_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Fifth_up).where(Fifth_up.id == day_id))


async def get_schedule6_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Six_up).where(Six_up.id == day_id))


async def get_schedule7_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Seven_up).where(Seven_up.id == day_id))


async def get_schedule8_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Eight_up).where(Eight_up.id == day_id))


async def get_schedule9_up(day_id):
    async with async_session() as session:
        return await session.scalar(select(Nine_up).where(Nine_up.id == day_id))
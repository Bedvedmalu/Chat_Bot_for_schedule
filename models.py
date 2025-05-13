from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger, String, ForeignKey

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Group(Base):
    __tablename__ = 'groups list'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(8))


class Day(Base):
    __tablename__ = 'day_list'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(12))


class First(Base):
    __tablename__ = 'schedule_for_one'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Second(Base):
    __tablename__ = 'schedule_for_two'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Third(Base):
    __tablename__ = 'schedule_for_three'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Fourth(Base):
    __tablename__ = 'schedule_for_four'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Fifth(Base):
    __tablename__ = 'schedule_for_five'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Six(Base):
    __tablename__ = 'schedule_for_six'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Seven(Base):
    __tablename__ = 'schedule_for_seven'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Eight(Base):
    __tablename__ = 'schedule_for_eight'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Nine(Base):
    __tablename__ = 'schedule_for_nine'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class First_up(Base):
    __tablename__ = 'schedule_for_one_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Second_up(Base):
    __tablename__ = 'schedule_for_two_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Third_up(Base):
    __tablename__ = 'schedule_for_three_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Fourth_up(Base):
    __tablename__ = 'schedule_for_four_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Fifth_up(Base):
    __tablename__ = 'schedule_for_five_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Six_up(Base):
    __tablename__ = 'schedule_for_six_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Seven_up(Base):
    __tablename__ = 'schedule_for_seven_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Eight_up(Base):
    __tablename__ = 'schedule_for_eight_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


class Nine_up(Base):
    __tablename__ = 'schedule_for_nine_up'
    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int] = mapped_column(ForeignKey('day_list.id'))
    first: Mapped[str] = mapped_column(String(40))
    second: Mapped[str] = mapped_column(String(40))
    third: Mapped[str] = mapped_column(String(40))
    fourth: Mapped[str] = mapped_column(String(40))
    fifth: Mapped[str] = mapped_column(String(40))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

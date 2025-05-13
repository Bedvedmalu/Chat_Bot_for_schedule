from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb
import app.database.requests as rq
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import datetime
from datetime import date

router = Router()


class check(StatesGroup):
    day = State()
    group = State()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.set_state(check.group)
    await message.answer('Выберите вашу учебную группу', reply_markup=await kb.groups())


@router.callback_query(F.data.startswith('to_main'))
async def back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(check.group)
    await callback.message.answer('Выберите вашу учебную группу', reply_markup=await kb.groups())


@router.callback_query(check.group)
async def day(callback: CallbackQuery, state: FSMContext):
    await state.update_data(group=callback.data)
    await state.set_state(check.day)
    await callback.message.answer('Выберите день недели', reply_markup=await kb.days(callback.data.split('_')[1]))


@router.callback_query(check.day)
async def schedule_for_down_week(callback: CallbackQuery, state: FSMContext):
    await state.update_data(day=callback.data)
    await callback.answer('Вы выбрали день')
    current_date = date.today().isocalendar()[1]
    data = await state.get_data()
    if current_date%2==0:
        if (data["group"].split('_')[1] == "1"):
            day_data = await rq.get_schedule1(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "2":
            day_data = await rq.get_schedule2(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "3":
            day_data = await rq.get_schedule3(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "4":
            day_data = await rq.get_schedule4(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "5":
            day_data = await rq.get_schedule5(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "6":
            day_data = await rq.get_schedule6(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "7":
            day_data = await rq.get_schedule7(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "8":
            day_data = await rq.get_schedule8(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "9":
            day_data = await rq.get_schedule9(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
    else:
        if (data["group"].split('_')[1] == "1"):
            day_data = await rq.get_schedule1_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "2":
            day_data = await rq.get_schedule2_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "3":
            day_data = await rq.get_schedule3_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "4":
            day_data = await rq.get_schedule4_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "5":
            day_data = await rq.get_schedule5_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "6":
            day_data = await rq.get_schedule6_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "7":
            day_data = await rq.get_schedule7_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "8":
            day_data = await rq.get_schedule8_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))
        elif data["group"].split('_')[1] == "9":
            day_data = await rq.get_schedule9_up(data["day"].split('_')[1])
            await callback.message.answer(
                f'8:30-10:00: {day_data.first}\n10:15-11:45: {day_data.second}\n12:00-13:30: {day_data.third}\n14:00-15:30: {day_data.fourth}\n15:45-17:15: {day_data.fifth}',
                reply_markup=await kb.days(callback.data.split('_')[1]))


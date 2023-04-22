from aiogram import Router, types
from aiogram.types import Message
from Text.Text_Ru import TEXT_RU
from aiogram.filters import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder




router = Router()

@router.message(Text(text=TEXT_RU['HW']))
async def with_puree(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['send'], url="https://drive.google.com/drive/u/2/folders/1LupycCiSti9QzNCfFRsIHkBkpa8Ib4gP")
    )
    await message.answer(TEXT_RU['SendHW'], reply_markup=builder.as_markup())

@router.message(Text(text=TEXT_RU['Abs']))
async def with_puree(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['LAC'],
        url="https://drive.google.com/drive/u/0/folders/1yI6zzqYO2K7uuMT9FafZ57bGgbdG4I4D")
    )
    await message.answer(TEXT_RU['WYWCH'], reply_markup=builder.as_markup())

@router.message(Text(text=TEXT_RU['Man']))
async def with_puree(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['GF'], url="https://www.google.ru/forms/about/")
    )
    await message.answer(TEXT_RU['WGF'], reply_markup=builder.as_markup())

@router.message(Text(text=TEXT_RU['DMan']))
async def with_puree(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['IS'],
        url="https://drive.google.com/drive/u/2/folders/1GqTdgCbPthWvNIvjKf3c4MsHmlGYcxuw")
    )
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['S'], url="https://drive.google.com/drive/u/2/folders/16zwo1UN9VLmcft9S-qEQfrwX5x6O_xxm")
    )
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['Hats'], url="https://drive.google.com/drive/u/2/folders/1_zjDtIb3sgtqptztSHGCeEVih1qr_pP0")
    )
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['MI'], url="https://drive.google.com/drive/u/2/folders/1G6W7XQT5z1uFIksx_a70AvaQ3EJAIRRO")
    )
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['TK'], url="https://drive.google.com/drive/u/2/folders/1pGRULO2ffhreDmqblLepNPsPV1rEZ-rf")
    )
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['U'], url="https://drive.google.com/drive/u/2/folders/1hD8xThq6DnIRrGIUOB4sUFdb8TFN12zV")
    )
    await message.answer(TEXT_RU['CM'], reply_markup=builder.as_markup())


@router.message(Text(text=TEXT_RU['CHW']))
async def with_puree(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text=TEXT_RU['CHeck'], url="https://drive.google.com/drive/u/2/folders/1LupycCiSti9QzNCfFRsIHkBkpa8Ib4gP")
    )
    await message.answer(TEXT_RU['WCHeck'], reply_markup=builder.as_markup())
from aiogram import Router, types, F
from aiogram.filters import Command, CommandObject
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from config import GAMEMENU_URL  # یا یک متغیر جدا مثل GAMEMENU_URL

router = Router(name="minigames")

@router.message(Command("play", "games", "minigame"))
async def open_gamemenu(message: types.Message, bot) -> None:
    if message.chat.type == ChatType.PRIVATE:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="🎮 منوی بازی‌ها",@router.message(Command("play", "games", "minigame"))
async def open_gamemenu(message: types.Message, bot) -> None:
    if message.chat.type == ChatType.PRIVATE:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="🎮 منوی بازی‌ها",
                web_app=WebAppInfo(url=GAMEMENU_URL)
            )]
        ])
        await message.answer("منوی بازی‌ها:", reply_markup=keyboard)
        return

    bot_info = await bot.get_me()
    deep_link = f"https://t.me/{bot_info.username}?start=games"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 رفتن به منوی بازی‌ها", url=deep_link)]
    ])
    await message.answer("برای بازی روی دکمه بزن:", reply_markup=keyboard)
                web_app=WebAppInfo(url=G@router.message(Command("play", "games", "minigame"))
async def open_gamemenu(message: types.Message, bot) -> None:
    if message.chat.type == ChatType.PRIVATE:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="🎮 منوی بازی‌ها",
                web_app=WebAppInfo(url=GAMEMENU_URL)
            )]
        ])
        await message.answer("منوی بازی‌ها:", reply_markup=keyboard)
        return

    bot_info = await bot.get_me()
    deep_link = f"https://t.me/{bot_info.username}?start=games"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 رفتن به منوی بازی‌ها", url=deep_link)]
    ])
    await message.answer("برای بازی روی دکمه بزن:", reply_markup=keyboard)AMEMENU_URL)
            )]
        ])
        await message.answer("منوی بازی‌ها:", reply_markup=keyboard)
        return

    bot_info = await bot.get_me()
    deep_link = f"https://t.me/{bot_info.username}?start=games"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 رفتن به منوی بازی‌ها", url=deep_link)]
    ])
    await message.answer("برای بازی روی دکمه بزن:", reply_markup=keyboard)

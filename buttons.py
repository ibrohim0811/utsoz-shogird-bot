from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sherik kerak"),
            KeyboardButton(text="Ish joyi kerak")
        ],
        [
            KeyboardButton(text="Hodim kerak"),
            KeyboardButton(text="Ustoz kerak")
        ],
        [
            KeyboardButton(text="Shogird kerak")
        ]
        ],
    resize_keyboard=True
)

sorov = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ]
        ],
    resize_keyboard=True
)

tel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni ulashing 📱", request_contact=True)
        ]
        ],
    resize_keyboard=True
)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#  создание категорий
ikb_category_selection = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Доходы",
                          callback_data="Salary"),
     InlineKeyboardButton("Копилка",
                          callback_data="Money_box")],
    [InlineKeyboardButton("Продукты",
                          callback_data="Products"),
     InlineKeyboardButton("Квартира",
                          callback_data="Apartment")],

    [InlineKeyboardButton("Хозтовары",
                          callback_data="Household"),
     InlineKeyboardButton("Аптека/Врачи",
                          callback_data="Pharmacy")],

    [InlineKeyboardButton("Кв в Коврове",
                          callback_data="Kovrov"),
     InlineKeyboardButton("Транспорт",
                          callback_data="Transport")],

    [InlineKeyboardButton("Мобильная связь и Банки",
                          callback_data="Mobile_banks")],
    [InlineKeyboardButton("Хобби",
                          callback_data="Hobby"),
     InlineKeyboardButton("Одежда", callback_data="Cloth")],
    [InlineKeyboardButton("Доставка",
                          callback_data="Delivery"),
     InlineKeyboardButton("Прочее",
                          callback_data="Other")],
    [InlineKeyboardButton("Путешествие",
                          callback_data="Traveling")],
    [InlineKeyboardButton('Спорт',
                          callback_data='Sport')]
    ])

# Кнопка отправки документа
ikb_document = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Дворецкий подай отчёт за месяц", callback_data="excel_file")],
    [InlineKeyboardButton("Дворецкий подай отчёт за год", callback_data="excel_file_2")]
])

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaDocument
import datetime

API_ID = 22875821
API_HASH = "366272f54f8a9c54640da2340eb18d59"

# آیدی ادمین برای ارسال پیام
admin_id = 1445026914

# تعریف یک دیکشنری برای ذخیره زمان ورود کاربرها
user_entry_times = {}

app = Client("robot", api_id=API_ID, api_hash=API_HASH)

# دیکشنری برای ذخیره انتخاب‌های کاربر
user_choices = {}

# تابعی برای نمایش گزینه‌های "لیست کلاس" به صورت 2 ستون و 10 ردیف دو به دو
def create_class_buttons():
    class_list = [
        "محمد علی آقا میری",
        "امیر محمد اسدی",
        "سپهر اسدی",
        "پارسا اکبری",
        "پارسا ایمانی",
        "آریا تلّی",
        "مهدی تیموری🌟",
        "ایلیا جاهد",
        "مانی جواد پور",
        "سید امین پاشا چاوشی⭐️",
        "ایلیا حسین زاده",
        "شهراد خالدی",
        "محمد امین دهقانی",
        "یزدان رحیمی",
        "رضا ستوده",
        "معین سعادتی",
        "محمد حسین شادلویی",
        "سجاد شکیبا",
        "بهشاد عابدی",
        "معین عباسی⭐️",
    ]

    class_buttons = []
    row = []
    for class_name in class_list:
        button = InlineKeyboardButton(class_name, callback_data=f"class_{class_name}")
        row.append(button)
        if len(row) == 2:
            class_buttons.append(row)
            row = []

    return class_buttons

@app.on_message(filters.command("start"))
async def on_start(client, message):
    user_id = message.from_user.id
    # زمان ورود کاربر
    entry_time = datetime.datetime.now()

    # ذخیره زمان ورود کاربر در دیکشنری
    user_entry_times[user_id] = entry_time

    # ایجاد منوی انتخابی با گزینه‌های "تکالیف" و "لیست کلاس"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("تکالیف✏️", callback_data="option_1"),
                InlineKeyboardButton("لیست کلاس", callback_data="option_2"),
            ],
            [
                InlineKeyboardButton("کمک🆘", callback_data="help"),
            ]
        ]
    )

    await message.reply("تکالیف برای چه روزی را می‌خوای؟", reply_markup=keyboard)

    # ارسال اطلاعات ورود به ادمین
    admin_id = 1445026914
    entry_message = f"کاربر با آیدی {user_id} در تاریخ {entry_time} وارد ربات شد."
    await app.send_message(admin_id, entry_message)

@app.on_callback_query()
async def on_callback_query(client, callback_query):
    data = callback_query.data
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    if data == "option_1":
        # ... (as before)

    elif data == "roz1":
        await callback_query.message.edit_text("شنبه🗓\nزنگ اول1️⃣\nشیمی امتحان از سوالات داده شده دفتر هم دیده میشه\nزنگ دوم2️⃣\nسواد رسانه سوالاتی که داده رندوم پرسیده میشه \nزنگ سوم3️⃣\n محیط زیست سوالاتی که داده وارد دفتر شود\nزنگ چهارم4️⃣\n کارگاه نوآوری گارگاه 5 و 6 حل شود")
    elif data == "roz2":
        await callback_query.message.edit_text("یک‌شنبه🗓\nزنگ کل\nحل کردن اکسس تاکسیرانی")
    elif data == "roz3":
        await callback_query.message.edit_text("دوشنبه🗓\nزنگ اول1️⃣\nزبان هیچی\nزنگ دوم2️⃣\nریاضی صفحه 21مسئله 3و 4حل شود صفحه 25 سه سوال اول حل شود \nزنگ سوم3️⃣\n دینی هیچی\nزنگ چهارم4️⃣\n ادبیات هیچی")
    elif data == "roz4":
        await callback_query.message.edit_text("سه‌شنبه🗓\nزنگ کل1️⃣\nطراحی صفحات وب هیچی")
    elif data == "roz5":
        await callback_query.message.edit_text("چهارشنبه🗓\nزنگ اول1️⃣\nفناوری هیچی\nزنگ دوم2️⃣\nتاریخ هیچی \nزنگ سوم3️⃣\n ریاضی هیچی\nزنگ چهارم4️⃣\n عربی هیچی")

    elif data == "option_2":
        # ... (as before)

    elif data == "back_to_menu":
        # ... (as before)

    elif data == "help":
        # Allow the user to send a message for help
        user_choices[chat_id] = "help"

    # Check if the user is in the "کمک" (Help) menu
    if user_choices.get(chat_id) == "help":
        # Forward any messages or media to the admin
        if callback_query.message.text:
            # Forward text messages
            await app.send_message(admin_id, f"کاربر با آیدی {user_id} نیاز به کمک دارد:\n{callback_query.message.text}")
        if callback_query.message.media:
            # Forward media (images, documents, etc.)
            media = callback_query.message.media
            if isinstance(media, InputMediaPhoto):
                await app.send_photo(admin_id, media.file_id)
            elif isinstance(media, InputMediaDocument):
                await app.send_document(admin_id, media.file_id)
        return

    # Handle other cases or menu options here

app.run()

# from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder

# #1-usul
# inline_menu = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Sifat o'quv kurslari",callback_data='course')],

#         [InlineKeyboardButton(text="Bizning manzil",callback_data='address'),
#          InlineKeyboardButton(text="Biz haqimizda",callback_data='about')
#          ],
#          [
#              InlineKeyboardButton(text="Admin bilan bog'lanish",callback_data="owner")
#          ]
#     ]
# )

# address_button = InlineKeyboardBuilder()
# address_button.add(InlineKeyboardButton(text="html",callback_data="html"))
# address_button.add(InlineKeyboardButton(text="⬅️orqaga qaytarish",callback_data="orqaga qaytarish"))
# # 2-usul

# course_button = InlineKeyboardBuilder()
# course_button.add(InlineKeyboardButton(text="Frontend 🖥",callback_data="frontend"))
# course_button.add(InlineKeyboardButton(text="Backend 🔙🔚",callback_data="backend"))
# course_button.add(InlineKeyboardButton(text="html",callback_data="html"))
# course_button.add(InlineKeyboardButton(text="login",callback_data="login"))
# course_button.add(InlineKeyboardButton(text="telegram bot",callback_data="telegram bot"))
# course_button.add(InlineKeyboardButton(text="python",callback_data="python"))
# course_button.add(InlineKeyboardButton(text="online darslar",url="https://www.google.com/search?q=online+python+video&sca_esv=602080591&sxsrf=ACQVn0_ktf1I2G0zlbo0-w5UStvZU6ab-A%3A1706412335350&ei=L8m1ZfL5FJW2i-gPycG84AM&udm=&ved=0ahUKEwiyzdqokf-DAxUV2wIHHckgDzwQ4dUDCBA&uact=5&oq=online+python+video&gs_lp=Egxnd3Mtd2l6LXNlcnAiE29ubGluZSBweXRob24gdmlkZW8yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB5IjiBQ_QZYzxtwAXgBkAEAmAGmAaABoQeqAQMwLja4AQPIAQD4AQHCAgoQABhHGNYEGLADwgINEAAYgAQYigUYQxiwA8ICCBAAGIAEGMsBwgIFEAAYgATCAgoQABiABBgKGLEDwgIHEAAYgAQYCsICBxAAGIAEGA3CAgYQABgeGA3iAwQYACBBiAYBkAYK&sclient=gws-wiz-serp#fpstate=ive&vld=cid:ee3a1e15,vid:XKHEtdqhLK8,st:0"))
# course_button.add(InlineKeyboardButton(text="Online",url="https://www.youtube.com/watch?v=kqtD5dpn9C8"))
# course_button.add(InlineKeyboardButton(text="Online kurslarimiz",url="https://www.youtube.com/watch?v=kqtD5dpn9C8"))
# course_button.add(InlineKeyboardButton(text="savollar",callback_data="savollar"))
# course_button.add(InlineKeyboardButton(text="⬅️ortga",callback_data="ortga"))

# course_button.adjust(2)

# ortga_button = InlineKeyboardBuilder()
# ortga_button.row(InlineKeyboardButton(text="⬅️orqaga",callback_data="course"))



# about_button = InlineKeyboardBuilder()
# about_button.add(InlineKeyboardButton(text="⬅️orqaga",callback_data="orqaga"))
# about_button.adjust(1)
# orqaga_button = InlineKeyboardBuilder()
# orqaga_button.row(InlineKeyboardButton(text="⬅️orqaga",callback_data="about"))



# owner_button = InlineKeyboardBuilder()
# owner_button.add(InlineKeyboardButton(text="⬅️orqaga",callback_data="orqaga"))
# owner_button.adjust(1)
# exit_button = InlineKeyboardBuilder()
# exit_button.row(InlineKeyboardButton(text="⬅️orqaga",callback_data="owner"))
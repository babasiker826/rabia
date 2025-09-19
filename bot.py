from flask import Flask, render_template

app = Flask(__name__)

# Ana sayfa
@app.route('/')
def index():
    try:
        return render_template("index.html")
    except Exception:
        return "Ana sayfa bulunamadı. index.html dosyasını templates klasörüne koyun.", 404

# /kalp route
@app.route('/kalp')
def kalp():
    try:
        return render_template("kalp.html")
    except Exception:
        return "/kalp sayfası bulunamadı. kalp.html dosyasını templates klasörüne koyun.", 404

# Hata sayfaları
@app.errorhandler(404)
def not_found(e):
    return "Sayfa bulunamadı (404).", 404

@app.errorhandler(500)
def server_error(e):
    return "Sunucu hatası (500).", 500

if __name__ == "__main__":
    # Render ve local uyumlu
    app.run(host="0.0.0.0", port=5000, debug=True)

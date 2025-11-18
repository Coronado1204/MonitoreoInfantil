from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/herramienta', methods=['GET', 'POST'])
def herramienta():
    powerbi_url = os.environ.get('POWERBI_EMBED_URL', 'https://app.powerbi.com/view?r=eyJrIjoiNWM4ZDAwYTAtNjJjZi00ZGRkLWJiZGUtMTc5YWI3ZTRiOTJjIiwidCI6IjA3ZGE2N2EwLTFmNDMtNGU4Yy05NzdmLTVmODhiNjQ3MGVlNiIsImMiOjR9')
    if request.method == 'POST':
        id_number = request.form.get('id_number', '').strip()
        return render_template('herramienta.html', id_number=id_number, powerbi_url=powerbi_url)
    return render_template('herramienta.html', id_number=None, powerbi_url=powerbi_url)

if __name__ == '__main__':
    app.run(debug=True)
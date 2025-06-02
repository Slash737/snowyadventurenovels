from flask import Flask, render_template, url_for, send_file
app = Flask(__name__)
 
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
       path = f'static/files/{filename}'
       return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
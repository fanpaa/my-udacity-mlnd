from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template
import os

app = Flask(__name__)
app.config['UPLOADED_PHOTO_DEST'] = './uploads'
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
def dest(name):
    return '{}/{}'.format(UPLOAD_DEFAULT_DEST, name)
#app.config['UPLOAD_PHOTO_URL'] = 'http://localhost:5000/'
photos = UploadSet('PHOTO')


configure_uploads(app, photos)

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return redirect(url_for('show', name=filename))
    return render_template('upload.html')

@app.route('/photo/<name>')
def show(name):
    if name is None:
        abort(404)
    url = photos.url(name)
    return render_template('show.html', url=url, name=name, what='狗')

app.run(debug=True)
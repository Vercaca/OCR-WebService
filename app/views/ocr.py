import json
from pathlib import Path

from flask import Blueprint, request, render_template
# from werkzeug import secure_filename


ocr_bp = Blueprint('ocr', __name__,
                   url_prefix='/ocr')


@ocr_bp.route('/', methods=['GET'])
def ocr_index():
    return '<h1>OCR Index</h1>'


@ocr_bp.route('/upload', methods=['GET'])
def upload():
    return render_template('ocr/index.html')


@ocr_bp.route('/upload_and_return_json', methods=['POST'])
def get_json_from_upload():
    print('uploading ~~~~')
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        print('filename = "{}"'.format(Path(filename).absolute()))

        f.save('{}'.format(filename))

        return json.dumps({
            'name': filename,
            'country': 'UNK',
            'expiration_date': 200101,
            'date_of_birth': 990101,
            'number': 'TW123930193'
        })


@ocr_bp.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    print('uploading ~~~')
    # return str(request.method)
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file"
        else:
            f = request.files['file']
            # filename = secure_filename(f.filename)
            filename = str(f.filename)
            # save to passporteye folder to process

            f.save(filename)
            return render_template('ocr/results.html', the_name=filename)

    else:
        return render_template('home/index.html', text="ocr/updater")


# `!WIP` Flask Web server for PassportOCR

用 Flask 架構實現OCR Web Service.

OCR模型可以自行變更，並修改`app/views/ocr.py`中的設定。

## Structure
#### Web service
- Flask + Blueprint
- Method: POST

####  OCR
- `!WIP`

### Environment Setup

```shell script
pipenv shell
pipenv install --skip-lock
```

## Demo
Demo flask connection
```shell script
python -m demo_home flask run
```
http://127.0.0.1:5000/ or http://127.0.0.1:5000/index


OCR Web service
```shell script
python -m flask run
```
http://127.0.0.1:5000/ocr/upload/


### Reference
1. [Github: OCR-on-passport](https://github.com/shahidhj/OCR-on-passport)
2. [FlaskBlueprint](https://www.itread01.com/content/1545813609.html)
3. [ExploreFlask](http://exploreflask.com/en/latest/blueprints.html)


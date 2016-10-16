from flask import Flask, request
import file_deleter
import json
import resources


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        args = request.args.to_dict()
        keys = list(args.keys())
        if 'api_token' in keys and 'weeks' in keys:
            file = open("delete-success.html")
            context = {
                'weeks': request.args.get('weeks'),
                'api_token': request.args.get('api_token')
            }
            ajax = resources.ajax.format(**context)
            context['ajax'] = ajax
            context['style'] = resources.style
            html = file.read().format(**context)
        else:
            file = open("delete-form.html")
            html = file.read()
        return html
    elif request.method == 'POST':
        api_token = request.form['api_token']
        weeks = int(request.form['weeks'])
        count = file_deleter.main(api_token, weeks=weeks)

        return json.dumps({'files': count})


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)

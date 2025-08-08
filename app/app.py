from flask import Flask, request, render_template_string, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    output = ''

    if request.method == 'POST':
        code_input = request.form.get('code_input', '')

        # !!! VULNERABLE !!!! # 
        output = render_template_string(code_input)

    return render_template('index.html', result=output)


if __name__ == '__main__':
    app.run(debug=True)
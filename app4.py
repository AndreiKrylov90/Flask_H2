# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# 📌 При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form.get('text')
        return f'You entered a text with {len(input_text)} symbols'
    return render_template('letters_counter.html')


if __name__ == '__main__':
    app.run(debug=True)

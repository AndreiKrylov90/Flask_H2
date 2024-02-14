# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# 📌 При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        argument_1 = int(request.form.get('argument_1'))
        argument_2 = int(request.form.get('argument_2'))
        action = request.form.get('action')
        if action == "+":
            result = argument_1 + argument_2
        elif action == "-":
            result = argument_1 - argument_2
        elif action == "*":
            result = argument_1 * argument_2
        elif action == "/":
            result = argument_1 / argument_2
        else:
            return "You entered something bad"
        return f'{argument_1} {action} {argument_2} = {result}'
    return render_template('calculate.html')


if __name__ == '__main__':
    app.run(debug=True)

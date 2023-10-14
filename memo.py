from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])

from main_window import *
from menu_window import *

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0 # кількість відповідей
        self.count_right = 0 # кількість правильних відповідей
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question("Яблуко", "apple", "pineapple", "strawberry", "blueberry")
q2 = Question("Скільки вийшло игр We Were Here?", "5", "3", "2", "4")
q3 = Question("В якому порядку розташовані кольора windows?", "червоний-зелений-синій-жовтий", "жовтий-зелений-червоний-синій", "зелений-червоний-жовтий-синій", "синій-зелений-червоний-жовтий")
q4 = Question("Який бренд добавляє в початок слова i?", "apple", "redmi", "sumsung", "gucci")

questions = [q1, q2, q3, q4]
radio_buttons = [rbth_1, rbth_2, rbth_3, rbth_4] # список радіо кнопок

def new_question():
    global curent_question
    curent_question = choice(questions)

    lb_question.setText(curent_question.question)

    shuffle(radio_buttons)
    radio_buttons[0].setText(curent_question.answer)
    radio_buttons[1].setText(curent_question.wrong_answer1)
    radio_buttons[2].setText(curent_question.wrong_answer2)
    radio_buttons[3].setText(curent_question.wrong_answer3)

new_question()

def check():
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_corect.text():
                curent_question.got_right()
                lable_Result.setText('Вірно!')
                break
    else:
        lable_Result.setText('Не вірно!')
        curent_question.got_wrong()

def click_ok():
    if btn_OK.text() == 'Відповісти':
        check()
        rbth_1.hide()
        rbth_2.hide()
        rbth_3.hide()
        rbth_4.hide()

        btn_OK.setText('Наступне запитання')
    else:
        rbth_1.show()
        rbth_2.show()
        rbth_3.show()
        rbth_4.show()

        btn_OK.setText('Наступне запитання')

btn_OK.clicked.connect(click_ok)

def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)

def back():
    window.show()
    menu.hide()
btn_back.clicked.connect(back)


def menu_generation():
    menu.show()
    window.hide()

button_menu.clicked.connect(menu_generation)

window.show()
app.exec_()
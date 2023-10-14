''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)


window = QWidget()

# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно
button_menu = QPushButton('Меню')
# кнопка прибирає вікно і повертає його після закінчення таймера
sleep = QPushButton('Відпочити')
# введення кількості хвилин
time = QSpinBox()
time.setValue(30)
lable_Time = QLabel('секунди')
# кнопка відповіді "Ок" / "Наступний"
btn_OK = QPushButton('Відповісти')
# текст питання
lb_question = QLabel('1')

# Опиши групу перемикачів
radio_group_box = QGroupBox('Варіанти відповідей')
Radio_group = QButtonGroup()

rbth_1 = QRadioButton('1')
rbth_2 = QRadioButton('1')
rbth_3 = QRadioButton('1')
rbth_4 = QRadioButton('1')

Radio_group.addButton(rbth_1)
Radio_group.addButton(rbth_2)
Radio_group.addButton(rbth_3)
Radio_group.addButton(rbth_4)


# Опиши панень з результатами
answer_group_box = QGroupBox('Результат тесту')
lable_Result = QLabel('') # правильно, не правильно
lb_corect = QLabel('') #првильна відповідь

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layout_H1 = QHBoxLayout()
layout_H2 = QHBoxLayout()
layout_H3 = QHBoxLayout()
layout_X1 = QVBoxLayout()
layout_X2 = QVBoxLayout()
layout_H4 = QHBoxLayout()

layout_H1.addWidget(button_menu)
layout_H1.addStretch(1)
layout_H1.addWidget(sleep)
layout_H1.addWidget(time)
layout_H1.addWidget(lable_Time)



layout_H2.addWidget(lb_question)

layout_X1.addWidget(rbth_1)
layout_X1.addWidget(rbth_2)
layout_X2.addWidget(rbth_3)
layout_X2.addWidget(rbth_4)
layout_H3.addLayout(layout_X1)
layout_H3.addLayout(layout_X2)

layout_H4.addWidget(btn_OK)

line = QVBoxLayout()
line.addLayout(layout_H1,stretch=1)
line.addLayout(layout_H2, stretch=2)
line.addLayout(layout_H3, stretch=8)
line.addStretch(1)
line.addLayout(layout_H4)
line.addStretch(1)
line.addSpacing(5)

window.setLayout(line)
window.resize(550, 450)


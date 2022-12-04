#create a memory card application

#import modules from library
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton, QPushButton, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer 
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = [] 
questions_list.append(Question('Which nationality is not real?', 'Chilans', 'Bangladeshi', 'Egyptians', 'Argentinians'))
questions_list.append(Question('What is the most commonly spoken language in the world?', 'English', 'Mandarin', 'French', 'Russian'))
questions_list.append(Question('What is the biggest country in the world?', 'Russia', 'Malaysia', 'China', 'Canada'))
questions_list.append(Question('What is the smallest ocean in the world?', 'Artic Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean'))
questions_list.append(Question('What is the largest desert in the world?', 'Antarctic Desert', 'Arctic Desert', 'Sahara Desert', 'Gobi Desert'))
questions_list.append(Question('What is the longest river in the world?', 'Amazon River', 'Nile river', 'Yangtze River', 'Yellow River'))
questions_list.append(Question('What is the tallest mountain in the world?', 'Mt. Everest', 'Mt. Lhotse', 'Mt. Cho Oyu', 'Mt. Mhakalu'))
questions_list.append(Question('What is the most numerous insect in the world?', 'ants', 'cockcroaches', 'beetles', 'butterflies'))
questions_list.append(Question('What is the fastest bird in the world?', 'peregrine falcon', 'cheetah', 'golden eagle', 'goose'))
questions_list.append(Question('What is the most venomous mammal in the world?', 'Platypus', 'humans', 'Snakes', 'Box Jellyfish'))

#Create windows
my_app = QApplication([])
my_win = QWidget()

my_win.setWindowTitle("Memory card")
my_win.resize(500, 300)
my_win.move(800, 300)
my_win.setStyleSheet("font: bold 14px;")

#Add widgets
question = QLabel("Which nationality is not real?")
optionA = QRadioButton("Chilans")#It is supposed to be Chileans with an "e"
optionB = QRadioButton("Bangladeshi")
optionC = QRadioButton("Egyptians")
optionD = QRadioButton("Argentinians")
button = QPushButton("Answer")

RadioGroup = QButtonGroup()
RadioGroup.addButton(optionA)
RadioGroup.addButton(optionB)
RadioGroup.addButton(optionC)
RadioGroup.addButton(optionD)

#Create answer option panel
groupAnsBox = QGroupBox("Answer options")

ans_main_layout = QVBoxLayout()
ans_h1 = QHBoxLayout()
ans_h2 = QHBoxLayout()

ans_h1.addWidget(optionA)
ans_h1.addWidget(optionB)
ans_h2.addWidget(optionC)
ans_h2.addWidget(optionD)

ans_main_layout.addLayout(ans_h1)
ans_main_layout.addLayout(ans_h2)

groupAnsBox.setLayout(ans_main_layout)

#result panel
result_panel = QGroupBox("Test result")
result_info = QLabel("True/False", alignment = (Qt.AlignLeft))
correct_ans = QLabel("Here, we will put correct answer!", alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

result_layout = QVBoxLayout() 
result_h1 = QHBoxLayout() 
result_h2 = QHBoxLayout()
result_h1.addWidget(result_info) 
result_h2.addWidget(correct_ans) 

result_layout.addLayout(result_h1)
result_layout.addLayout(result_h2)

result_panel.setLayout(result_layout)

#create main layout
card_layout = QVBoxLayout()
card_h1 = QHBoxLayout()
card_h2 = QHBoxLayout()
card_h3 = QHBoxLayout()

card_h1.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
card_h2.addWidget(groupAnsBox)
card_h2.addWidget(result_panel)

result_panel.hide()
card_h3.addStretch(1)
card_h3.addWidget(button, stretch= 1)
card_h3.addStretch(1)

card_layout.addLayout(card_h1)
card_layout.addLayout(card_h2)
card_layout.addLayout(card_h3)

my_win.setLayout(card_layout)

#Create functions
def show_result():
    #show answer panel
    groupAnsBox.hide()
    result_panel.show()
    button.setText("Next question")
    
def show_question():
    #show question panel
    groupAnsBox.show()
    result_panel.hide()
    button.setText("Answer")
    RadioGroup.setExclusive(False)
    optionA.setChecked(False)
    optionB.setChecked(False)
    optionC.setChecked(False)
    optionD.setChecked(False)
    RadioGroup.setExclusive(True)

# def test():
#     if button.text() == "Answer":
#         show_result()
#     else:
#         show_question()

answers = [optionA, optionB, optionC, optionD]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.questions)
    correct_ans.setText(q.right_answer)
    show_question()

def show_correct(res):
    result_info.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct!")
        print("Statistics\n-Total questions: ", my_win.total, "\n-Right answers ", my_win.score)
        print("Rating: ", (my_win.score/my_win.total*100), "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Incorrect!")
            print("Rating: ", (my_win.score/my_win.total*100), "%")

question_order = list(range(0, len(questions_list)))

def next_question():
    my_win.total += 1
    my_win.cur_question = my_win.cur_question + 1
    if my_win.cur_question >= len(questions_list):
        shuffle(question_order)
        my_win.cur_question = 0
        my_win.score = 0
        my_win.total = 1
    pick = question_order[my_win.cur_question]
    q = questions_list[pick]
    ask(q)

def click_OK():
    if button.text() == "Answer":
        if my_win.cur_question == 0:
            shuffle(question_order)
        check_answer()
    else:
        next_question()

my_win.cur_question = -1
my_win.score = 0
my_win.total = 0
button.clicked.connect(click_OK)
next_question()

#Execute the window

my_win.show()
my_app.exec()
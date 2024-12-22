#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout
import json 

app = QApplication([]) #приложение


#интерфейс приложения

#окно
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600) #размер


#виджеты в окне
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')


button_note_create = QPushButton('Создать заметку') # появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')


feild_tag = QLineEdit('')
feild_tag.setPlaceholderText('Введите тег...')
feild_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')



#расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(feild_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)



col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(feild_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)




col_2.addLayout(row_3)
col_2.addLayout(row_4)




layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)


'Функционал приложения'


#работа с текстом заметки
def add_note():
    note_name, ok = QInputDialog.getText(notes_win,'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги':[] }
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)




def show_note():
    #получаем текст из заметки с выделенным названием и отображаем его в поле редактирования
    kay = lists_notes.selctedItems()[0].text()
    print(key)
    feild_text.setText(notest[kay]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[key]['теги'])

    





def save_note():
    if list_notes.selectediteams():
        key =  list_notes.selectedItems()[0].text()
        notes[key]["текст"] = feild_text.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=false)
            print(notes)
    else:
        print('Заметка для сохранения не выбрана!')






def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        feild_text.clear()
        list_notes.addIteams(notes)
        with open('notes_data.json','w') as file :
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')




def add_tag():
    if list_notes.selectediteams():
        key = list_notes.selctedItems()[0].text()
        tag = feild_tag.text()
        if not tag in notes [key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для добавления тега не выбрана!")





def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        teg = list_tags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["теги"])
        with open ("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print('Тег для удаления не выбран!')





def



        print (button_tag search.text())
        if button tag search. text() == "Искать заметки по тегу"
        notes_filtered = {) #тут будут заметки с выделенным тегом-
        for note in notes:
        if tag in notes [note] ["теги"]:
        notes filtered[note]=notes[note]







#запуск приложения
notes_win.show()


with open('notes_data.json','r') as file:
    notes = json.load(file)
list_notes.addItems(notes)



app.exec_()
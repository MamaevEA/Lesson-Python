import easygui
def viev_log():
    with open("log.txt", 'r',encoding='utf-8') as file:
        contents = file.read()
    easygui.msgbox (contents)

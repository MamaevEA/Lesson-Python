def viev_log():
    with open("log.txt", 'r',encoding='utf-8') as file:
        contents = file.read()
        print(contents)
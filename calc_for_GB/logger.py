import datetime
import easygui



def make_answer (s,dig, error):
    answer=''
    current_date_time =str( datetime.datetime.now())
    if error==True: answer=current_date_time+' '+ s+' '+'решение не может быть найдено, ошибка в выражении '+'\n'
    else:
        answer=current_date_time+' '+s+' = '+dig+'\n'
    return answer

def save_log(answer_in_string):
    with open("log.txt", 'a', encoding='utf-8') as fh:

        fh.write(answer_in_string)

        easygui.msgbox(answer_in_string,'Я успешно загрузил в файл следующую информацию')
# text='2+2'
# digital=(2+3j)
# answer_in_string=make_answer(text,digital,True)
# save_log(answer_in_string)




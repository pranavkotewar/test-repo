import datetime
todaydate = datetime.datetime.now()

import calendar
c = calendar.calendar(2025)
def chatbot(questions):
    response = {
        "hi":"Hey there i'am 'bot' your virtual cahtbot.",
        "how are you":"i'am fine, whats about you.",
        "todays date":f"Today's date & time is - {todaydate}",
        "show me calendar":f"sure,this is your calender - {c}",   
        "who are you":"I'am a virtual simple chatbot created by you."

    }
    return response.get(questions.lower(),"sorry I didn't understand what you said.")

while True:
    user_in = input('Say someting - ')
    
    if user_in.lower() == "exit" :
        print('Ok bye... see you soon.')
        break
    if user_in.lower() == "bye":
        print('Goodbye! see you soon, have a nice day.')
        break
    print('bot : ',chatbot(user_in))

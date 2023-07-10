
from embedchain import OpenSourceApp

chat_bot = OpenSourceApp()

# Embed Online Resources
chat_bot.add("pdf_file", "https://uscode.house.gov/static/constitution.pdf")

count = 0
while (count < 10):
    count = count + 1
    question=input("What's your question?\n")
    print(chat_bot.query(question))
    answerValidity=input("Are you satisfied with the answer?\n If Yes, type 'Y' \n If No, type 'N'\n\n")
    if answerValidity == "N" or answerValidity == "n":
        newAnswer=input("To train your model, Please Enter new answer.\n\n")
        if newAnswer:
            chat_bot.add_local("qna_pair", (question, newAnswer))
    else:
        print("Let's go to next question then\n")
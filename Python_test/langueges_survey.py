from anonymose_survey import AnonymousSurvey


question = 'what is your first Language'
new_survey = AnonymousSurvey(question)

new_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break
    new_survey.store_response(response)

new_survey.show_results()
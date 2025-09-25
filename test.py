from Database.CURD import create_question,read_question,update_question,delete_question



question_text = "What is the capital of Germany?"
options = ["Paris", "Berlin", "Rome", "Madrid"]
answer = "Berlin"

question_id = create_question(question_text, options, answer)
print(f"Question added with ID: {question_id}")


question = read_question({"_id": question_id})
print("Fetched Question:", question)

update_question({"_id": question_id}, {
    "options": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "answer": "Berlin"
})

delete_question({"_id": question_id})

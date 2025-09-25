from .DB_connect import get_db

db = get_db()
if db is not None:
    collection = db["Questions"]
else:
    raise Exception("❌ Failed to connect to the database.")

def create_question(question_text, options, correct_answer):
    if correct_answer not in options:
        raise ValueError("Correct answer must be one of the options.")
    
    question_data = {
        "question": question_text,
        "options": options,
        "answer": correct_answer
    }
    
    result = collection.insert_one(question_data)
    return str(result.inserted_id)

def read_question(query):
    return collection.find_one(query)

def update_question(query, new_data):
    if "answer" in new_data and "options" in new_data:
        if new_data["answer"] not in new_data["options"]:
            raise ValueError("Correct answer must be one of the options.")
    
    result = collection.update_one(query, {"$set": new_data})
    return result.modified_count

def delete_question(query):
    result = collection.delete_one(query)
    return result.deleted_count

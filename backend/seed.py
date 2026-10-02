from app.database import db

quiz_results = [
    # Sharon
    {"student_id": "S001", "student_name": "Sharon", "subject": "Computer Networks", "topic": "Subnetting", "score": 6, "total_marks": 10},
    {"student_id": "S001", "student_name": "Sharon", "subject": "Computer Networks", "topic": "Routing", "score": 8, "total_marks": 10},
    {"student_id": "S001", "student_name": "Sharon", "subject": "Computer Networks", "topic": "DNS", "score": 9, "total_marks": 10},
    # Rahul
    {"student_id": "S002", "student_name": "Rahul", "subject": "Computer Networks", "topic": "Subnetting", "score": 8, "total_marks": 10},
    {"student_id": "S002", "student_name": "Rahul", "subject": "Computer Networks", "topic": "Routing", "score": 9, "total_marks": 10},
    {"student_id": "S002", "student_name": "Rahul", "subject": "Computer Networks", "topic": "DNS", "score": 8, "total_marks": 10},
    # Aisha
    {"student_id": "S003", "student_name": "Aisha", "subject": "Computer Networks", "topic": "Subnetting", "score": 7, "total_marks": 10},
    {"student_id": "S003", "student_name": "Aisha", "subject": "Computer Networks", "topic": "Routing", "score": 7, "total_marks": 10},
    {"student_id": "S003", "student_name": "Aisha", "subject": "Computer Networks", "topic": "DNS", "score": 8, "total_marks": 10},
    # John
    {"student_id": "S004", "student_name": "John", "subject": "Computer Networks", "topic": "Subnetting", "score": 8, "total_marks": 10},
    {"student_id": "S004", "student_name": "John", "subject": "Computer Networks", "topic": "Routing", "score": 8, "total_marks": 10},
    {"student_id": "S004", "student_name": "John", "subject": "Computer Networks", "topic": "DNS", "score": 7, "total_marks": 10},
]

collection = db["quiz_results"]

collection.delete_many({})
result = collection.insert_many(quiz_results)

print(f"Inserted {len(result.inserted_ids)} quiz results")
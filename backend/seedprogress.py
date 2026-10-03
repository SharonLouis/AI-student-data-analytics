from app.database import db

TOTAL_LECTURES = 20
completed_counts = {
    "S001":15,
    "S002":18,
    "S003":12,
    "S004":16
}
records = []
for student_id , count in completed_counts.items():
    for lecture_number in range(1, TOTAL_LECTURES + 1):
        records.append({
            "student_id":student_id,
            "subject":"Computer Networks",
            "lecture_number":lecture_number,
            "completed":lecture_number <= count,
        })
collection = db["lecture_progress"]
collection.delete_many({})
result = collection.insert_many(records)
print(f"Inserted {len(result.inserted_ids)} progress records")
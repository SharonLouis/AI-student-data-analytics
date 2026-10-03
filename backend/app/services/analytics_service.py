import pandas as pd
from app.database import db


def get_student_analytics(student_id: str):
    # 1. Get this student's quiz results from MongoDB
    results = list(db["quiz_results"].find({"student_id": student_id}, {"_id": 0}))

    if not results:
        return None

    # 2. Turn the list into a DataFrame (a table)
    df = pd.DataFrame(results)

    # 3. Overall score = total obtained / total possible * 100
    overall_score = df["score"].sum() / df["total_marks"].sum() * 100

    # 4. Topic-wise score
    topic_totals = df.groupby("topic")[["score", "total_marks"]].sum()
    topic_totals["percentage"] = topic_totals["score"] / topic_totals["total_marks"] * 100
    topic_performance = topic_totals["percentage"].round(2).to_dict()

    # 5. Strongest and weakest topic
    strongest_topic = max(topic_performance, key=topic_performance.get)
    weakest_topic = min(topic_performance, key=topic_performance.get)

    all_results = list(db["quiz_results"].find({},{"id":0}))
    all_df = pd.DataFrame(all_results)
    student_totals = all_df.groupby("student_id")[["score","total_marks"]].sum()
    student_totals["percentage"] = student_totals["score"]/student_totals["total_marks"]*100
    class_average = student_totals["percentage"].mean()
    difference = overall_score - class_average
    progress = list (db["lecture_progress"].find({"student_id":student_id},{"_id":0}))
    if progress:
        progress_df = pd.DataFrame(progress)
        completion_percentage = progress_df["completed"].mean()*100
    else :
        completion_percentage = 0
    return {
        "student_id": student_id,
        "student_name": df["student_name"].iloc[0],
        "subject": df["subject"].iloc[0],
        "overall_score": round(float(overall_score), 2),
        "class_average":round(float(class_average),2),
        "difference_from_class_average":round(float(difference),2),\
        "completion_percentage":round(float(completion_percentage),2),
        "strongest_topic": strongest_topic,
        "weakest_topic": weakest_topic,
        "topic_performance": topic_performance,
    }
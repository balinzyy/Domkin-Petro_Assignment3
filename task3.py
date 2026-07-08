exam_results = [{"student_name": "Анна","score": 91},
                {"student_name": "Богдан","score": 58},
                {"student_name": "Вікторія","score": 75},
                {"student_name": "Григорій","score": 45}]


passing_score = 60

for i in exam_results:
    if i["score"] >= passing_score:
        i["passed"] = True
    else:
        i["passed"] = False

print(exam_results)


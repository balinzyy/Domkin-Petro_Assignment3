def get_department_stats(employee_list, target_dept):
    result = {"top_earner_quant" : 0 ,"count" : 0}
    sumsalary = 0
    for i in employee_list:

        if i["department"] == target_dept:
            result["department"] = i["department"]
            sumsalary += i["salary"]

            if i["salary"] > result["top_earner_quant"]:
                result["top_earner"] = i["name"]
                result["top_earner_quant"] = i["salary"]

            result["count"] += 1

    result["avgsalary"] = f"{sumsalary / result["count"]:.2f}"

    del result["top_earner_quant"]





    return result



employees = [{"name": "Олена","department": "Marketing","salary":25000},
             {"name": "Ігор","department": "IT","salary": 55000},
             {"name": "Наталія","department": "Marketing","salary":28000},
             {"name": "Олег","department": "HR","salary": 22000},
             {"name": "Андрій","department": "IT","salary": 48000},
             {"name": "Марія","department": "IT","salary": 52000}]


print(get_department_stats(employees,"IT"))
print(get_department_stats(employees,"Marketing"))


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

def financialhealth(employees):
    deptsexpenses = [{"name": i, "salary_spendings": sum(k["salary"] for k in employees if k["department"] == i)} for i in {j["department"] for j in employees}]
    deptsrevenues = [{"name": i, "revenue": 100000} for i in {j["department"] for j in employees}]

    deptbalances = [{"name": i, "balance": 0} for i in {j["department"] for j in employees}]
    for i in range(len(deptsexpenses)):
        dif = deptsrevenues[i]["revenue"] - deptsexpenses[i]["salary_spendings"]
        deptbalances[i]["balance"] = dif


    return deptbalances








employees = [{"name": "Олена","department": "Marketing","salary":25000},
             {"name": "Ігор","department": "IT","salary": 55000},
             {"name": "Наталія","department": "Marketing","salary":28000},
             {"name": "Олег","department": "HR","salary": 22000},
             {"name": "Андрій","department": "IT","salary": 48000},
             {"name": "Марія","department": "IT","salary": 52000}]




def mainprogram():
    deptname = str(input("Which department financial health state are you looking for? : "))

    d = financialhealth(employees)


    for i in d:
        if i["name"] == deptname and i["balance"] < 0:
            print(f"{deptname} department has a negative profit of {i['balance']}$. ")
        elif i["name"] == deptname:
            print(f"{deptname} department's financial health is good. Annual profit is {i['balance']}$.")


mainprogram()




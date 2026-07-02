deposit_account = [{"client_id": "C1025",
                   "balance": 5000.0,
                   "currency": "UAH",
                   "interest_rate": 0.08,
                   "is_active": True
                   }]

summ = 0

for i in deposit_account:
    summ += i["balance"]*i["interest_rate"]

print(summ)


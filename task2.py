deposit_account = [{"client_id": "C1025",
                   "balance": 5000.0,
                   "currency": "UAH",
                   "interest_rate": 0.08,
                   "is_active": True
                   }]


for i in deposit_account:
    i["last_update_type"] = "interest accrual"

print(deposit_account)


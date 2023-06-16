rent_per_month = 21000
annual_rent = rent_per_month * 12
total_rent=0

for year in range(1,31):
    total_rent += annual_rent
    annual_rent += (annual_rent * 0.10)

print(total_rent)
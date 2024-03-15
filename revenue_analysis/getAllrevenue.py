# %%
import json
from collections import defaultdict
import csv

# %%
res = dict()

# %%
import csv

filename = 'datasets/quan.csv'
monthfileFirst = 'datasets/treas_meters_'
monthfileSecond = '_pole_by_month_datasd.csv'

with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        zone, area, sub_area, pole, _, _, _, latitiude, longtitude, _ = row
        if pole not in res:
            res[pole] = {"Latitude": float(latitiude),
                        "Longtitude": float(longtitude),
                        "RevenueByMonth": defaultdict(lambda: [0]*12),
                        "YearlyRevenue": defaultdict(int),
                        "Others":{
                            "Zone":zone,
                            "Area":area,
                            "SubArea":sub_area
                        }
                        }

# print("30-3400E" in res)
for year in range(2018, 2024):
    oodPoints = set()
    monthfile = monthfileFirst + str(year) + monthfileSecond
    with open(monthfile, mode='r', encoding='utf-8') as mfile:
        csv_reader = csv.reader(mfile)
        next(csv_reader)

        for row in csv_reader:
            pole_id, month, sum_trans_amt, _ = row
            sum_trans_amt = float(sum_trans_amt)
            if pole_id not in res:
                oodPoints.add(pole_id)
                continue

            res[pole_id]["RevenueByMonth"][year][int(month)-1] = sum_trans_amt
            res[pole_id]["YearlyRevenue"][year] += sum_trans_amt
print(f"There are {len(oodPoints)} Pole do not have location")


# %%
filename = 'allYear.json'

with open(filename, 'w') as file:
    json.dump(res, file, indent=4)



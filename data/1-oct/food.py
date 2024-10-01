import csv
from collections import Counter


food = list(csv.DictReader(open('food-inspections.csv')))
fail = [ row for row in food if row['Results'] == 'Fail' ]
worst = Counter(row['DBA Name'] for row in fail)
print(worst.most_common(5))


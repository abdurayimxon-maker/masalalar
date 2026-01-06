set1={100, 20, 45, 80, 70, 50}
set2={30, 55, 70, 60, 32, 100}

set1_katta = {x for x in set1 if x >= 60}
set2_katta = {x for x in set2 if x >= 60}

umumiy = set1_katta.intersection(set2_katta)

orta = sum(umumiy) / len(umumiy)

print(int(orta))
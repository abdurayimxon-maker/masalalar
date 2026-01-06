set1 = {"Artel", "Alif", "Yandex", "Google", "Meta"}
set2 = {"Google", "Apple", "Amazon", "Meta"}
set3 = {"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

umumiy = set1 & set2 & set3
faqat_set1 = set1 - set2 - set3

print("Umumiy elementlar:", umumiy)
print("Faqat birinchi setga tegishli:", faqat_set1)
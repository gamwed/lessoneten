f = open('test.txt', 'r', encoding='utf-8')
purchase_count = 0
total_amount = 0
sum = 0
expenses_by_category = {}
expenses_by_member = {}
member_name = input("Введіть ім'я члена родини: ")
for line in f:
    _, *name, money, category = line.strip().split()
    money = float(money.replace('$', ''))
    name = ' '.join(name)
    sum = sum + money
    if category in expenses_by_category:
        expenses_by_category[category] += money
    else:
        expenses_by_category[category] = money
    if name in expenses_by_member:
        expenses_by_member[name] += money
    else:
        expenses_by_member[name] = money
    if name == member_name:
        purchase_count += 1
        total_amount += money

print("Сума грошей на кожну категорію:")
for category, amount in expenses_by_category.items():
    print(category, '=', round(amount, 2))
print("x" * 10)
print("Сума грошей, витрачених кожним членом родини:")
for member, amount in expenses_by_member.items():
    print(member, '=', round(amount, 2))
print("x" * 10)

print("Кількість покупок:", member_name, "=", purchase_count)
print("Загальна сума витрат:", total_amount)






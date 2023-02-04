tickets = int(input('введите кол-во билетов - '))
visitors = tickets

sum = 0
while visitors !=0:
    age_for_ticket = int(input(f"укажите возраст посетителя {visitors} :"))
    if age_for_ticket < 18 :
        print('Билет бесплатно')
    elif 25 > age_for_ticket >= 18 :
        sum += 990
        print('цена билета - 990 р.')
    elif 100 > age_for_ticket >= 25:
        sum += 1390
        print("цена билета - 1390 р.")
    else:
        print("некоректное значение,проверьте и повторите ввод")
        continue
    visitors -= 1
if tickets > 3:
    sale = sum - ((sum / 100 ) * 10 )
    print(f'к оплате {sale} р.,с учётом скидки 10% за покупку 3 и более билетов')
else:
    print(f'к оплате {sum} р.')

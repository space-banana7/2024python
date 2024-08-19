menu={"짬뽕":3000,"짜장면":5000,"탕수육":7000}
# print("짜장면" in menu)
print(f"메뉴는 {menu}")
selected=input("골라\n")
if selected in menu:
    print(f"{selected} 가격은 {menu[selected]}")
else:
    print("오 추가해줌")
    menu[selected]=10000
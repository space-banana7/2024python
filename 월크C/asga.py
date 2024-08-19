menu = {"짬뽕": 3000, "짜장면": 5000, "탕수육": 7000}

def display_menu():
    print("현재 메뉴:")
    for item, price in menu.items():
        print(f"{item}: {price}원")

def add_item():
    item = input("추가할 메뉴 항목을 입력하세요: ")
    price = int(input("추가할 메뉴의 가격을 입력하세요: "))
    menu[item] = price
    print(f"{item} 항목이 메뉴에 추가되었습니다.")

while True:
    display_menu()
    choice = input("1. 메뉴에 항목 추가, 2. 종료 \n")
    if choice == "1":
        new_menu=input("추가할 메뉴 항목을 입력하세요: ")
        new_price=input("추가할 가격의 가격을 입력하세요: ")
        menu.update((f"{new_menu}: ", f"{new_price}"))
        print(f"{new_menu} 항목이 메뉴에 추가되었습니다.")
    elif choice == "2":
        print("프로그램을 종료합니다.")
        break
    else:
        print("올바른 선택이 아닙니다.")
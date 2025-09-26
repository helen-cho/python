while True:
    try:
        num = input("숫자>")
        if num=="": break
        num = int(num)
    except Exception as err:
        print("숫자를 입력하세요!", err)

# while True:
#     num = input("숫자>")
#     if num=="": break
#     num = int(num)
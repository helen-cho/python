#일반 가격
def price(people):
    print(f"{people}명 가격은 {people * 15000:,}원입니다.")

#조조할인 가격
def price_morning(people):
    print(f"{people}명 조조할인 가격은 {people * 10000:,}원입니다.")

#군인할인 가격
def price_soldier(people):
    print(f"{people}명 군인할인 가격은 {people * 4000:,}원입니다.")


if __name__ == "__main__":
    price_soldier(3)
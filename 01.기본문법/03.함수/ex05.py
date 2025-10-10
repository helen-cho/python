from function import inputNum, grade

kor = inputNum("국어")
eng = inputNum("영어")
mat = inputNum("수학")
avg = (kor+eng+mat)/3
print(f"평균:{avg:.2f} 평점:{grade(avg)}")
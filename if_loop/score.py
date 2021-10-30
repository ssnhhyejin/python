num = int(input('점수 입력(1~100) : '))
grade=""
if num >= 90:
    grade="A"
elif num>=80:
    grade="B"
elif num>=70:
    grade="C"
elif num>=60:
    grade="D"
else:
    grade="F"

print(f"점수 : {num}, 등급 : {grade}")
print("점수 : %d, 등급 : %s"%(num, grade))

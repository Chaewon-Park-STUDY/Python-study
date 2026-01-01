만약 bmi가 18.5 미만이면 "underweight"이라고 출력하세요.

만약 bmi가 18.5 이상 25 미만이면 "normal weight"이라고 출력하세요.

만약 bmi가 25 이상이면 "overweight"이라고 출력하세요.





```python
weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")
```

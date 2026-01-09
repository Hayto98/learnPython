# giá trị boolean là True và False (nhớ viết hoa)
# biểu thức boolean là đánh giá xem kết quả của phép so sánh
# kết quả phải biểu thức boolean là giá trị boolean

# thụt lề (indentation): nhóm các câu lệnh thành khối lệnh

# biểu thức if
if 3 < 5:
    print('đúng')
print('done')

'''
 output :
     đúng
     done
'''


#  biểu thức if-else
x = 5
if x == 2:
    print('yes')
else:
    print('no')
print("next stop")

"""
output:
    no
    next stop
"""

# biểu thức if-eif-else

day = "Monday"
if day == "Monday":
    print('Today is Monday')
elif day == "Tuesday":
    print('Today is Tuesday')
elif day == "Wednesday":
    print('Today is Wednesday')
else:
    print("unknow day!")
print("next stop")


# câu lệnh pass

"""

a = 4 
if a > 3: 
                <= LỖI CHỖ NÀY, SAU BIỂU THỨC PHẢI CÓ KHỐI LỆNH ĐI KÈM   
print("next stop")

ĐỂ FIX 
a = 4 
if a > 3: 
    pass <= để pass ở đây để nhắc tôi trong tương lai sẽ code chỗ này sau 
print("next stop")

"""


# Biểu thức match case
today = "Monday"
match today:
    case "Monday":
        print('Today is Monday')
    case "Tuesday":
        print('Today is Tuesday')
    case "Wednesday":
        print('Today is Wednesday')
    case "Thursday":
        print('Today is Thursday')
    case "Friday":
        print('Today is Friday')
    case "Saturday":
        print('Today is Saturday')
    case "Sunday":
        print('Today is Sunday')
    case _:
        print("unknow day!")


# Biểu thức if rút gọn
# nếu chỉ có 1 khối lệnh đi cùng với if
if x % 2 == 0 : print("even number")


# toán tử 3 ngôi (ternary operator)
"""
ch = 5 
if ch % 2 == 0:
    number = "Even"
else:
    number = "Odd
"""

# biểu thức 1 if điều kiện else biểu thức 2
ch = 5
number = "Even" if ch % 2 == 0 else "Odd"


# Biểu thức if lồng nhau  (nested if statement)

"""
x = 6

if x % 2 == 0:
    if x % 3 == 0:
        print("x is divisible by 6")
    else:
        print("x is divisible by 2 but not by 3")
else:
    if x % 3 == 0:
        print("x is divisible by 3 but not by 2")
    else:
        print("x is not divisible by either 2 or 3")
"""





"""
    Nhập vào 2 số:
    - 1 số đại diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý: Năm nhuận là năm thỏa mãn 1 trong 2 điều kiện sau:
    - Năm đó chia hết cho 4 nhưng không chia hết cho 100
    - Năm đó chia hết cho 400
"""
year = int(input("Enter year number: "))
month = int(input("Enter month number: "))
if( year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    if month == 2:
        print("có 29 ngày")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("có 30 ngày")
    else:
        print("có 31 ngày")
else :
    if(month == 2):
        print("có 28 ngày")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("có 30 ngày")
    else:
        print("có 31 ngày")
'''
    yêu cầu người dùng nhập vào 3 số a,b,c 
    tìm nghiệm của phương trình bậc 2 
    ax^2 + bx + c = 0
'''

a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
c = float(input("Enter c number: "))

if a == 0:
    if b == 0 and c == 0:
        print("infinitety many solution")
    elif b == 0 and c != 0:
        print("infinitety many solution")
    else:
        print("x = ", -c/b)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("No solution")
    elif delta == 0:
        print("x = ", -b / (2 * a))
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)

"""
    Yêu cầu người dùng nhập vào 3 số nguyên dương
    1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
    tam giác vuông hay tam giác thường
    3. Kiểm tra tiếp xem tam giác có góc tù hay không?
    4. Tính diện tích của tam giác
"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Check if these 3 numbers are sides of a triangle
if a + b > c and b + c > a and a + c > b:
    if a == b and a == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            print("Tam giac vuong can")
        else:
            print("Tam giac can")
    elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")
else:
    print("Day khong phai so do 3 canh tam giac")
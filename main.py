# các kiểu dữ liệu (data types)
# int (số nguyên)
# float (số thực)
# string (chuỗi)
# boolean


# biến (variable)
# biến sẽ lưu trữ một giá trị của một đối tượng bên trong nó
# giá trị trong biến lưu trữ nhìn chung có thể thay đổi trong quá trình lập trình
# có những trường ngoại lệ sẽ không thay đổi được
# nếu biến của bạn lưu giá trị số thực thì nó có kiểu số thực

# khai báo biến và gán giá trị
a = 7 # khai báo biến kiểu số nguyên
b = 6.5 # khai báo biến kiểu số thực
c = 'hello world' # khai báo biến kiểu chuỗi (1)
d = "today is monday" # khai báo biên kiểu chuỗi (2)
e = """  
    hello fen
    I'm Thanh Hai
""" # khai báo biến kiểu chuỗi (3)
f = True #khai báo biến kiểu boolean
f = "awesome" #gán giá trị mới cho biến f

print(f)  #awesome

# để kiểm tra kiểu dữ liệu dùng type(....)
print(type(a)) #<class 'int'>
print(type(d)) #<class 'str'>

# các quy tắc khi khai báo biến
# Tên biến dài bao nhiêu cũng được ex: long_name_variable
# Tên biến có thể chứa chữ cái, số và dấu gạch dưới(_)  ex: son_tung_mtp
# Momo và momo là 2 biến khác nhau
# Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới
# Không được đặt tên biến trùng với tên các keywords

# Ghi chú (Comments)
# Ghi chú giúp người khác và chính bản thân các bạn sau này khi đọc lại code có thể dễ dàng hiểu đoạn code này dùng để làm gì
# có các cách comments
'''
    cách 1 
'''

"""
    cách 2
"""

# Toán tử
# toán tử là các kí tự đặc biệt hoặc là tập hợp các kí tự đặc biệt hoặc là keyword
# toán tử dùng để thực hiện 1 phép tính nào đó

# trong Python có 7 toán tử, nhưng thường dùng 6 toán tử
# toán tử số học (Arithmetic operators)
# toán tử so sánh (Comparison operators)
# toán tử gán (Assignment operators)
# toán tử logic (logical operators)
# toán tử với bit (bitwise operators)
# toán tử thành viên (Membership operators)


# tìm hiểu về "Arithmetic operators"

# toán tử |  ý nghĩa                 | ví dụ        | kết quả
#    +    | phép cộng                | 4 + 5        |    9
#    -    | phép trừ                 | 6 - 1.5      |   4.5
#    *    | phép nhân                | 4 * 2        |    8
#    /    | phép chia                | 15 / 2       |   7.5
#   //    | phép chia lấy nguyên     | 15// 2       |    7
#    %    | phép chia lấy dư         | 15 % 2       |    1
#    **   | phép lũy thừa            | 2**3         |    8


# Toán tử gán (Assignment Operators)
# toán tử | ý nghĩa                    | ví dụ     | tương đương với
# =       | gán                        | x = 5     | x = 5
# +=      | cộng và gán                | x += 5    | x = x + 5
# -=      | trừ và gán                 | x -= 5    | x = x - 5
# *=      | nhân và gán                | x *= 5    | x = x * 5
# /=      | chia và gán                | x /= 2    | x = x / 2
# //=     | chia lấy nguyên và gán     | x //= 2   | x = x // 2
# %=      | chia lấy dư và gán         | x %= 5    | x = x % 5
# **=     | lũy thừa và gán            | x **= 2   | x = x ** 2

# Toán tử so sánh (Comparison Operators)
# toán tử | ý nghĩa                         | ví dụ   | kết quả
# ==      | so sánh bằng                    | 6 == 6  | True
# !=      | so sánh không bằng              | 6 != 6  | False
# <       | so sánh nhỏ hơn                 | 4 < 5   | True
# <=      | so sánh nhỏ hơn hoặc bằng       | 4 <= 5  | True
# >       | so sánh lớn hơn                 | 4 > 5   | False
# >=      | so sánh lớn hơn hoặc bằng       | 4 >= 5  | False

# Toán tử logic (Logic Operators)
# toán tử | ý nghĩa                                                                                     | ví dụ               | kết quả
# and     | Và: Nếu điều kiện ở vế trái và vế phải của toán tử đều là True thì kết quả là True.         | 5 > 4 and 5 < 6     | True
#         |     Tất cả các trường hợp khác kết quả là False                                             | 5 > 4 and 5 >= 6    | False
# or      | Hoặc: Nếu điều kiện ở vế trái và vế phải của toán tử đều là False thì kết quả là False.     | 4 >= 5 or 5 >= 6    | False
#         |       Tất cả các trường hợp khác kết quả là True                                            | 4 < 5 or 5 == 6     | True
# not     | Phủ định: Đảo ngược trạng thái logic của toán hạng                                          | not (5 > 4)         | False
#         |                                                                                             | not (5 < 4)         | True

# Toán tử thành viên (Membership operators)
# toán tử | ý nghĩa                                                                 | ví dụ                            | kết quả
# in      | Nằm trong: Trả về True nếu giá trị đang kiểm tra nằm trong              | x = "red"                        | True
#         | danh sách / chuỗi các giá trị                                           | y = ["red", "green", "blue"]     |
#         |                                                                         | x in y                           |

# not in  | Không nằm trong: Trả về True nếu giá trị đang kiểm tra KHÔNG nằm trong  | x = "red"                        | False
#         | danh sách / chuỗi các giá trị                                           | y = ["red", "green", "blue"]     |
#         |                                                                         | x not in y                       |

# Toán tử với bit (Bitwise Operators)
# toán tử | ý nghĩa     | ví dụ
# &       | AND         | x & y
# |       | OR          | x | y
# ^       | XOR         | x ^ y
# ~       | NOT         | ~x
# <<      | dịch trái   | x << 2
# >>      | dịch phải   | x >> 2



# Thứ tự ưu tiên của toán tử (từ cao xuống thấp)
# toán tử                   | mô tả
# ()                        | ngoặc đơn
# **                        | lũy thừa
# *, /, %, //               | phép nhân / chia
# +, -                      | phép cộng, trừ
# <, <=, >, >=              | so sánh
# ==, !=                    | so sánh
# =, +=, -=, *=, /=, %=, //=, **= | phép gán
# is, is not                | toán tử nhận dạng
# in, not in                | toán tử thành viên
# not, or, and              | toán tử logic


# Các hàm cơ bản
# In 1 giá trị/ đối tượng gì đó ra màn hình: print()
# Lưu trữ giá trị người dùng nhập vào từ bàn phím: input()
# Trả về kiểu dữ liệu của 1 biến: type()

# ex:
name = input("Nhập tên username: ")
print("Bạn vừa nhập vào là: ", name)
print("Kiểu dữ liệu của bạn vừa nhập vào: ", type(name))


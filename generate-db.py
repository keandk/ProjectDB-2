from faker import Faker
import pymysql
import random

fake = Faker()
print("Connecting...")
# Tạo kết nối đến cơ sở dữ liệu
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='...',
    database='TRUONGHOC1'
)
print("Connected.")

cur = conn.cursor()

print("Inserting into TRUONG...")
# Phát sinh và chèn dữ liệu vào bảng TRUONG
for i in range(1, 101):
    cur.execute(
        "INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES (%s, %s, %s)", 
        (i, fake.name(), fake.address())
    )
conn.commit()
print("Done.")


# Phát sinh và chèn dữ liệu vào bảng HS
print("Inserting into HS...")
for i in range(1, 1000001):
    cur.execute(
        "INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s, %s, %s, %s, %s, %s)", 
        (i, fake.first_name(), fake.last_name(), fake.unique.random_number(digits=9), fake.date_of_birth(minimum_age=18, maximum_age=25), fake.address())
    )
conn.commit()
print("Done.")


# Phát sinh và chèn dữ liệu vào bảng HOC
print("Inserting into HOC...")
for i in range(1, 1000001):
    # Gán một trường ngẫu nhiên cho một sinh viên
    matr = random.randint(1, 100)
    for j in range(2022, 2025):  # Xét trong 3 năm học
        # Chọn ngẫu nhiên một sinh viên có tham gia học năm hiện tại hay không
        if random.choice([True, False]):
            diemtb = round(random.uniform(0, 10), 1)
            if diemtb >= 9:
                xeploai = 'Xuất sắc'
                kqua = 'Hoàn thành'
            elif diemtb >= 8:
                xeploai = 'Giỏi'
                kqua = 'Hoàn thành'
            elif diemtb >= 6.5:
                xeploai = 'Khá'
                kqua = 'Hoàn thành'
            elif diemtb >= 5:
                xeploai = 'Trung bình'
                kqua = 'Hoàn thành'
            else:
                xeploai = 'Yếu'
                kqua = 'Chưa hoàn thành'
                
            cur.execute(
                "INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES (%s, %s, %s, %s, %s, %s)", 
                (matr, i, j, diemtb, xeploai, kqua)
            )
conn.commit()
print("Done.")

# Đảm bảo tất cả các thay đổi được lưu lại
conn.commit()

# Đóng kết nối
cur.close()
conn.close()

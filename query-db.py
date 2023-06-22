import xml.etree.ElementTree as ET
import pymysql
import time

# Lấy dữ liệu hiện có trong CSDL
def get_available_options():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='...',
        database='TRUONGHOC2' # Thuận tiện hơn vì được sắp xếp giảm dần (đã được tạo các index)
    )
    cur = conn.cursor()

    queries = ["SELECT DISTINCT TENTR FROM TRUONG", 
               "SELECT DISTINCT NAMHOC FROM HOC", 
               "SELECT DISTINCT XEPLOAI FROM HOC"]
    
    options = []
    
    # Thực hiện từng câu lệnh truy vấn một
    for query in queries:
        cur.execute(query)
        query_options = [option[0] for option in cur.fetchall()]
        options.extend(query_options)

    cur.close()
    conn.close()

    # Ghi vào file những dữ liệu hiện có
    with open('available-options.txt', 'w') as f:
        for option in options:
            print(option, file=f)

# Hàm thực hiện câu lệnh truy vấn và xuất file XML
def query_and_export_to_xml(database, school_name, year, ranking):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456789',
        database=database
    )

    cur = conn.cursor()

    # Thực hiện truy vấn
    start_time = time.time() # Bắt đầu tính thời gian 
    cur.execute(
        """
        SELECT SQL_NO_CACHE HS.HO, HS.TEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
        FROM HS 
        JOIN HOC ON HS.MAHS = HOC.MAHS
        JOIN TRUONG ON HOC.MATR = TRUONG.MATR
        WHERE TRUONG.TENTR = %s AND HOC.NAMHOC = %s AND HOC.XEPLOAI = %s
        """,
        (school_name, year, ranking)
    )
    end_time = time.time() # Kết thúc tính thời gian 

    rows = cur.fetchall()

    # Tạo element root cho file XML
    root = ET.Element('students')

    # Thêm từng dòng vào file XML
    for row in rows:
        student_element = ET.SubElement(root, 'student')
        ET.SubElement(student_element, 'ho').text = row[0]
        ET.SubElement(student_element, 'ten').text = row[1]
        ET.SubElement(student_element, 'ntns').text = str(row[2])
        ET.SubElement(student_element, 'diemtb').text = str(row[3])
        ET.SubElement(student_element, 'xeploai').text = row[4]
        ET.SubElement(student_element, 'kqua').text = row[5]

        # In ra màn hình thông tin các sinh viên nếu là TRUONGHOC1
        if(database == 'TRUONGHOC1'):
            print(f"Student: HO={row[0]}, TEN={row[1]}, NTNS={str(row[2])}, DIEMTB={str(row[3])}, XEPLOAI={row[4]}, KQUA={row[5]}")


    # Tạo object ElementTree từ root element
    tree = ET.ElementTree(root)

    directory = 'XML/'
    tree.write(f'{directory}{database}-{school_name}-{year}-{ranking}.xml', encoding='utf-8', xml_declaration=True)

    print(f"""
          '{school_name}' is selected.
          '{year}' is selected.
          '{ranking}' is selected.
          Query time of {database}: {end_time - start_time} seconds.
          """)

    # Đóng kết nối
    cur.close()
    conn.close()

get_available_options()

#     Thay thế 3 parameters dưới bằng những dữ liệu trong file và bỏ comment
#     sau khi đã thêm các thông tin đầy đủ.
#     Ví dụ:
#           query_and_export_to_xml(dbs, 'ABC', 2022, 'Khá')

# # Chọn từng CSDL một
# for dbs in ['TRUONGHOC1', 'TRUONGHOC2']:
#     query_and_export_to_xml(dbs, '...', ..., '...')
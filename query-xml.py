import xml.etree.ElementTree as ET
import os

# Hàm lấy xếp loại dựa trên điểm
def get_rating_based_on_score(score):
    if score >= 9:
        return 'Xuất sắc'
    elif score >= 8:
        return 'Giỏi'
    elif score >= 6.5:
        return 'Khá'
    elif score >= 5:
        return 'Trung bình'
    else:
        return 'Yếu'

# Hàm lấy tên file XML dựa trên xếp loại
def get_available_xml_files(directory, low_score, high_score):
    # Danh sách tất cả các file trong thư mục
    files = os.listdir(directory)

    # Lọc ra những file có phần mở rộng là '.xml' và nằm trong khoảng điểm
    xml_files = [file for file in files if file.endswith('.xml') and 
                 get_rating_based_on_score(low_score) in file and 
                 get_rating_based_on_score(high_score) in file]

    return xml_files

# Hàm nhận đầu vào từ người dùng
def get_user_input():
    valid = False

    while not valid:
        # Yêu cầu người dùng nhập khoảng điểm
        low_score = float(input("Enter the low score: "))
        high_score = float(input("Enter the high score: "))

        if get_rating_based_on_score(low_score) != get_rating_based_on_score(high_score):
            print("Entered scores correspond to different ratings. Please enter a valid score range.")
            print("For example, a valid score range for 'Khá' is 6.5 to 7.9.")
        else:
            valid = True

    directory = 'XML/' # Đường dẫn đến thư mục lưu các file

    print("Available XML files: ")
    available_xml_files = get_available_xml_files(directory, low_score, high_score)
    for i, xml_file in enumerate(available_xml_files):
        print(f"{i+1}. {xml_file}") # In ra tên và số hiệu của file hiện có 
    xml_file_num = int(input("Enter the number corresponding to the XML file: ")) # Yêu cầu người dùng nhập số hiệu
    while xml_file_num < 1 or xml_file_num > len(available_xml_files):
        # Nếu nhập không hợp lệ thì yêu cầu người dùng nhập lại
        print("Invalid number. Please choose from the available options.")
        xml_file_num = int(input("Enter the number corresponding to the XML file: "))
    xml_file = os.path.join("XML", available_xml_files[xml_file_num - 1])

    return xml_file, low_score, high_score

# Hàm in ra kết quả theo yêu cầu người dùng
def print_students_in_score_range(file_name, low_score, high_score):
    # Đọc file XML
    tree = ET.parse(file_name)

    # Lấy root của file XML
    root = tree.getroot()

    # Duyệt qua mỗi thành phần 'student' trong file
    for student in root.findall('student'):
        # Lấy thành phần 'diemtb'
        diemtb_element = student.find('diemtb')

        # Chuyển đổi thành phần 'diemtb' sang kiểu float
        diemtb = float(diemtb_element.text)

        # Kiểm tra nếu điểm nằm trong khoảng
        if low_score <= diemtb <= high_score:
            # Nếu có, in thông tin của sinh viên đó ra
            print("Student: HO={}, TEN={}, NTNS={}, DIEMTB={}, XEPLOAI={}, KQUA={}".format(
                student.find('ho').text,
                student.find('ten').text,
                student.find('ntns').text,
                diemtb,
                student.find('xeploai').text,
                student.find('kqua').text
            ))

# Lấy tên file từ người dùng
file_name, low_score, high_score = get_user_input()

# Thực hiện yêu cầu
print_students_in_score_range(file_name, low_score, high_score)

import logging

logging.basicConfig(
    filename=r"C:\Users\ghast\OneDrive\Tài liệu\[IT205-K25] Lập trình ứng dụng với Python\session20\tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

'''
*** Chức năng 1: Hiển thị lịch thi đấu & Kết quả

Hàm đề xuất: display_matches(match_list)

Yêu cầu: In ra danh sách trận đấu với định dạng cột rõ ràng.

Tích hợp Logging: Ghi log ở mức INFO với thông báo: "User viewed the match list."
'''
def display_matches(match_list):
    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return
    print("--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10}| {'Đội A':<15}| {'Đội B':<15}| {'Tỷ số':<8}| Trạng thái")
    print("----------------------------------------------------------------------")
    for game in match_list:
        game['score_total'] = f"{game['score_a']}-{game['score_b']}"
        print("{match_id:<10}| {team_a:<15}| {team_b:<15}| {score_total:<8}| {status:<15}".format_map(game))

    logging.info("User viewed the match list.")

'''
*** Chức năng 2: Thêm trận đấu mới

Trường hợp thêm hợp lệ
Chọn chức năng (1-5): 2

--- THÊM TRẬN ĐẤU MỚI ---
Nhập mã trận đấu: M03
Nhập tên Đội A: G2
Nhập tên Đội B: FNC

Thành công: Đã thêm trận đấu M03.

'''
def index_match(id, match_list):
    for index, match in enumerate(match_list):
        if match['match_id'] == id:
            return index
    return -1


def add_match(match_list):
    print("--- THÊM TRẬN ĐẤU MỚI ---")
    id_inp = input("Nhập mã trận đấu: ").strip().upper()
    if not id_inp:
        print("Mã trận đấu không được để trống.")
        logging.warning('User tried to add a match with empty match ID.')
        return
    if index_match(id_inp,match_list) != -1:
        print(f"Lỗi: Mã trận đấu {id_inp} đã tồn tại.")
        logging.warning(f'Match ID {id_inp} already exists.')
        return
    name_a = input("Nhập tên Đội A: ").strip()
    name_b = input("Nhập tên Đội B: ").strip()
    if not name_a or not name_b:
        print("Tên đội không được để trống.")
        logging.warning(f'User tried to add a match with empty team name.')
        return
    
    new_match = {
    "match_id": id_inp,
    "team_a": name_a,
    "team_b": name_b,
    "score_a": 0,
    "score_b": 0,
    "status": "Pending"
    }
    
    match_list.append(new_match)
    print(f"Thành công: Đã thêm trận đấu {id_inp}.")
    logging.info(f"Match {id_inp} added successfully")

'''
*** Chức năng 3: Cập nhật tỷ số trận đấu 

Hàm đề xuất: update_score(match_list)

Yêu cầu nhập mã trận đấu, sau đó nhập điểm cho Đội A và điểm cho Đội B. Trạng thái (status) tự động chuyển thành "Completed".

Debugging & Exception Handling: Trọng tài rất hay gõ nhầm chữ cái vào ô nhập điểm (VD: gõ "hai" thay vì "2"). Bắt buộc sử dụng try...except ValueError để bẫy lỗi nhập liệu. Yêu cầu nhập lại cho đến khi đúng là số nguyên >= 0.

Logging: Ghi log ERROR kèm chi tiết lỗi (traceback hoặc message) nếu trọng tài nhập sai kiểu dữ liệu. Ghi log INFO nếu cập nhật thành công.
'''
def update_score(match_list):
    print("--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    id_inp = input("Nhập mã trận đấu cần cập nhật: ").strip().upper()
    if not id_inp:
        print("Mã trận đấu không được để trống.")
        logging.warning('User tried to add a match with empty match ID.')
        return
    if index_match(id_inp, match_list) == -1:
        print(f"Không tìm thấy trận đấu mang mã {id_inp}.")
        logging.warning(f'User tried to update non-existing match {id_inp}')
        return
    index = index_match(id_inp, match_list)
    print(f"Trận đấu: {match_list[index]['team_a']} vs {match_list[index]['team_b']} (Pending)")
    while True:
        try:
            score_a = int(input("Nhập điểm Đội A: "))
            if score_a < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.warning("Negative score input detected: -1")
                continue
        except ValueError:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.warning(f"Invalid score input. Error: invalid literal for int() with base 10: '{score_a}'")
        else:
            break
    
    while True:
        try:
            score_b = int(input("Nhập điểm Đội B: "))
            if score_b < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.warning("Negative score input detected: -1")
                continue
            
        except ValueError:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.warning(f"Invalid score input. Error: invalid literal for int() with base 10: ''{score_b}''")
            
        else:
            break
    if score_a == 0 and score_b == 0:
        while True:
            confirm = input("Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n):").strip().lower()
            if confirm == 'n':
                return
            elif confirm == 'y':
                break
            else:
                print("Lỗi cú pháp")
        
    match_list[index]['score_a'] = score_a
    match_list[index]['score_b'] = score_b
    match_list[index]['status'] = "Completed"
    logging.info(f"Match {id_inp} score updated successfully")
    print(f"Thành công: Đã cập nhật tỷ số trận đấu {id_inp}.")        
    
    
    
'''
*** Chức năng 4: Báo cáo thống kê

Hàm đề xuất: generate_report(match_list)

Helper Function: Viết một hàm phụ trợ determine_winner(match) nhận vào dictionary của một trận đấu và trả về Tên đội thắng (hoặc "Draw" nếu hòa, hoặc "Not Started" nếu status là Pending).

Duyệt danh sách và in ra các trận đã "Completed" cùng tên đội chiến thắng.
'''
def determine_winner(match):
    if match['score_a'] > match['score_b']:
        return match['team_a']
    elif match['score_a'] < match['score_b']:
        return match['team_b']
    else:
        return 'Draw'
def generate_report(match_list):
    print("--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    for match in match_list:
        result = ""
        if match['status'] == "Pending":
            continue
        result = determine_winner(match)
        print(f"{match['match_id']}: {match['team_a']} {match['score_a']}-{match['score_b']} {match['team_b']} | Kết quả: {result}")

    print(f"Tổng số trận đã hoàn thành: {len([match for match in match_list if match['status'] == 'Completed'])}")
    logging.info('User generated tournament report.')
def main():
    while True:
        choice = input("""
===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====
1. Hiển thị lịch thi đấu & Kết quả
2. Thêm trận đấu mới
3. Cập nhật tỷ số trận đấu
4. Báo cáo thống kê
5. Thoát chương trình
================================================== 
Chọn chức năng (1-5): """)
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Vui lòng nhập số nguyên")
            continue
        
        match choice:
            case 1:
                display_matches(matches)
            
            case 2:
                add_match(matches)
                
            case 3:
                update_score(matches)
            
            case 4:
                generate_report(matches)
            
            
            case 5:
                print("Thoát chương trình")
                logging.info("Exist program")
                break
            case _:
                logging.warning("Invalid menu choice selected")
                print("Lỗi cú pháp")
                
main()                
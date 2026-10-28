
import json
from pathlib import Path
from datetime import datetime

# =========================
# 1. CẤU HÌNH
# =========================

DATA_FILE = Path("transactions.json")

CATEGORIES = {
    "income": ["Lương", "Thưởng", "Khác"],
    "expense": ["Ăn uống", "Di chuyển", "Học tập", "Giải trí", "Khác"],
}


# =========================
# 2. LƯU VÀ ĐỌC DỮ LIỆU
# =========================

def load_transactions():
    """Đọc giao dịch từ file JSON."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Dữ liệu không hợp lệ. Bắt đầu với danh sách trống.")
            return []

        return data

    except (json.JSONDecodeError, OSError):
        print("Không thể đọc dữ liệu. Bắt đầu với danh sách trống.")
        return []


def save_transactions(transactions):
    """Lưu danh sách giao dịch vào file JSON."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(
                transactions,
                file,
                ensure_ascii=False,
                indent=4
            )
        return True

    except OSError:
        print("Lỗi: Không thể lưu dữ liệu.")
        return False


# =========================
# 3. NHẬP VÀ KIỂM TRA DỮ LIỆU
# =========================

def input_amount():
    """Nhập số tiền dương."""
    while True:
        try:
            amount = float(input("Số tiền (VND): "))

            if amount <= 0:
                print("Số tiền phải lớn hơn 0.")
                continue

            return amount

        except ValueError:
            print("Vui lòng nhập số hợp lệ.")


def choose_type():
    """Chọn loại giao dịch."""
    print("\n1. Thu nhập")
    print("2. Chi tiêu")

    while True:
        choice = input("Chọn loại: ").strip()

        if choice == "1":
            return "income"
        if choice == "2":
            return "expense"

        print("Lựa chọn không hợp lệ.")


def choose_category(transaction_type):
    """Chọn danh mục phù hợp với loại giao dịch."""
    categories = CATEGORIES[transaction_type]

    print("\nDanh mục:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Chọn danh mục: "))

            if 1 <= choice <= len(categories):
                return categories[choice - 1]

            print("Số danh mục không hợp lệ.")

        except ValueError:
            print("Vui lòng nhập số nguyên.")


# =========================
# 4. THÊM GIAO DỊCH
# =========================

def add_transaction(transactions):
    """Thêm một khoản thu hoặc chi."""
    transaction_type = choose_type()
    amount = input_amount()
    category = choose_category(transaction_type)

    description = input("Mô tả giao dịch: ").strip()
    if not description:
        description = "Không có mô tả"

    transaction = {
        "id": max(
            (item.get("id", 0) for item in transactions),
            default=0
        ) + 1,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    transactions.append(transaction)

    if save_transactions(transactions):
        print("Đã thêm giao dịch thành công.")
    else:
        transactions.pop()
        print("Giao dịch chưa được lưu.")


# =========================
# 5. HIỂN THỊ GIAO DỊCH
# =========================

def display_transactions(transactions):
    """Hiển thị danh sách giao dịch."""
    if not transactions:
        print("\nChưa có giao dịch nào.")
        return

    print("\n" + "=" * 90)
    print(
        f"{'ID':<5}{'Ngày':<22}{'Loại':<12}"
        f"{'Danh mục':<15}{'Số tiền (VND)':>18}  Mô tả"
    )
    print("-" * 90)

    for item in transactions:
        transaction_type = (
            "Thu nhập" if item["type"] == "income" else "Chi tiêu"
        )

        print(
            f"{item['id']:<5}"
            f"{item['date']:<22}"
            f"{transaction_type:<12}"
            f"{item['category']:<15}"
            f"{item['amount']:>18,.0f}  "
            f"{item['description']}"
        )

    print("=" * 90)


# =========================
# 6. THỐNG KÊ THU CHI
# =========================

def show_summary(transactions):
    """Tính tổng thu, tổng chi và số dư."""
    total_income = sum(
        item["amount"]
        for item in transactions
        if item["type"] == "income"
    )

    total_expense = sum(
        item["amount"]
        for item in transactions
        if item["type"] == "expense"
    )

    balance = total_income - total_expense

    print("\n========== THỐNG KÊ TÀI CHÍNH ==========")
    print(f"Tổng thu : {total_income:,.0f} VND")
    print(f"Tổng chi : {total_expense:,.0f} VND")
    print(f"Số dư    : {balance:,.0f} VND")
    print("=========================================")


# =========================
# 7. LỌC THEO DANH MỤC
# =========================

def filter_by_category(transactions):
    """Lọc và hiển thị giao dịch theo danh mục."""
    if not transactions:
        print("\nChưa có giao dịch để lọc.")
        return

    categories = sorted({
        item["category"] for item in transactions
    })

    print("\nCác danh mục đang có:")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        try:
            choice = int(input("Chọn danh mục: "))

            if 1 <= choice <= len(categories):
                selected = categories[choice - 1]
                break

            print("Số danh mục không hợp lệ.")

        except ValueError:
            print("Vui lòng nhập số nguyên.")

    result = [
        item for item in transactions
        if item["category"] == selected
    ]

    print(f"\nGiao dịch thuộc danh mục: {selected}")
    display_transactions(result)


# =========================
# 8. DỮ LIỆU MẪU
# =========================

def add_sample_data(transactions):
    """Thêm dữ liệu mẫu để thử chương trình."""
    if transactions:
        confirm = input(
            "Đã có dữ liệu. Bạn vẫn muốn thêm mẫu? (y/n): "
        ).strip().lower()

        if confirm != "y":
            print("Đã hủy.")
            return

    samples = [
        {
            "type": "income",
            "amount": 5000000,
            "category": "Lương",
            "description": "Lương tháng",
        },
        {
            "type": "income",
            "amount": 500000,
            "category": "Thưởng",
            "description": "Thưởng hoàn thành công việc",
        },
        {
            "type": "expense",
            "amount": 50000,
            "category": "Ăn uống",
            "description": "Ăn trưa",
        },
        {
            "type": "expense",
            "amount": 30000,
            "category": "Di chuyển",
            "description": "Tiền xe",
        },
        {
            "type": "expense",
            "amount": 200000,
            "category": "Học tập",
            "description": "Mua sách",
        },
    ]

    next_id = max(
        (item.get("id", 0) for item in transactions),
        default=0
    ) + 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for sample in samples:
        transactions.append({
            "id": next_id,
            **sample,
            "date": now,
        })
        next_id += 1

    if save_transactions(transactions):
        print("Đã thêm dữ liệu mẫu.")
    else:
        del transactions[-len(samples):]
        print("Không thể lưu dữ liệu mẫu.")


# =========================
# 9. MENU CHÍNH
# =========================

def show_menu():
    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Thêm giao dịch")
    print("2. Xem tất cả giao dịch")
    print("3. Thống kê thu chi")
    print("4. Lọc theo danh mục")
    print("5. Thêm dữ liệu mẫu")
    print("0. Thoát")
    print("===============================================")


def main():
    transactions = load_transactions()

    print("Chào mừng đến với Personal Expense Tracker!")

    while True:
        show_menu()
        choice = input("Nhập lựa chọn: ").strip()

        if choice == "1":
            add_transaction(transactions)

        elif choice == "2":
            display_transactions(transactions)

        elif choice == "3":
            show_summary(transactions)

        elif choice == "4":
            filter_by_category(transactions)

        elif choice == "5":
            add_sample_data(transactions)

        elif choice == "0":
            print("Đã thoát chương trình. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Hãy thử lại.")


if __name__ == "__main__":
    main()

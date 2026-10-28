# Personal Expense Tracker — Hướng dẫn dự án đầy đủ



> Dự án quản lý thu chi cá nhân bằng Python, được xây dựng theo hướng học tập từ Week 01 đến Week 15 của [CocAgent/python-journey](https://github.com/CocAgent/python-journey).

README này là tài liệu hướng dẫn dài dành cho người mới học Python. Tài liệu trình bày mục tiêu, chức năng, cấu trúc thư mục, kiến thức nền tảng, cách cài đặt trong VS Code, luồng chạy, giải thích từng module, cách kiểm thử, dữ liệu mẫu, xử lý lỗi, Git, kế hoạch mở rộng và checklist demo.


list DEMO
Bản demo sẽ có các chức năng chính:
- Thêm khoản thu và khoản chi.
- Xem danh sách giao dịch.
- Tính tổng thu, tổng chi và số dư.
- Lọc giao dịch theo danh mục.
- Lưu dữ liệu vào file JSON để lần chạy sau vẫn còn dữ liệu.
- Có dữ liệu mẫu để thử ngay.

## Mục lục

1. Giới thiệu dự án
2. Mục tiêu học tập
3. Phạm vi và tính năng
4. Công nghệ sử dụng
5. Yêu cầu hệ thống
6. Cấu trúc thư mục
7. Mô hình dữ liệu
8. Cài đặt trên Windows
9. Cài đặt trên macOS/Linux
10. Chạy ứng dụng
11. Hướng dẫn từng chức năng
12. Luồng chạy tổng thể
13. Giải thích từng module
14. Quy tắc xác thực dữ liệu
15. Lưu dữ liệu JSON
16. Báo cáo thu chi
17. Kiểm thử bằng pytest
18. Kiểm thử thủ công
19. Ánh xạ Week 01–15
20. Quy trình debug
21. Git và GitHub
22. Demo trước lớp
23. Câu hỏi thường gặp
24. Hạn chế hiện tại
25. Ý tưởng nâng cấp
26. Checklist hoàn thành
27. Thuật ngữ
28. Phụ lục ví dụ

## 1. Giới thiệu dự án

Personal Expense Tracker là ứng dụng dòng lệnh (CLI) dùng để ghi lại các khoản tiền vào và tiền ra. Người dùng thao tác thông qua menu trong Terminal. Chương trình lưu dữ liệu vào file JSON để các giao dịch vẫn còn sau khi thoát ứng dụng.

Dự án hướng đến người học đã biết các kiến thức Python cơ bản và muốn kết hợp chúng thành một sản phẩm nhỏ có cấu trúc rõ ràng. Đây không chỉ là một file Python duy nhất; các trách nhiệm được tách thành nhiều module để người học thực hành cách thiết kế chương trình.

### 1.1 Vấn đề cần giải quyết

Nếu ghi chép thu chi bằng giấy hoặc ghi chú rời rạc, người dùng có thể khó tìm lại giao dịch, tính tổng tiền hoặc biết khoản chi nào chiếm nhiều nhất. Ứng dụng gom các giao dịch về một nơi, cung cấp chức năng lọc và báo cáo cơ bản.

### 1.2 Đối tượng sử dụng

- Người mới học Python.
- Học sinh, sinh viên cần dự án thực hành.
- Người muốn hiểu cách lưu dữ liệu JSON.
- Người muốn bắt đầu học kiểm thử tự động bằng pytest.
- Người muốn thực hành chia chương trình thành package và module.

### 1.3 Mục tiêu chính

- Ghi nhận giao dịch thu và chi.
- Xem lại các giao dịch đã lưu.
- Lọc giao dịch theo loại và tháng.
- Tính tổng thu, tổng chi và số dư.
- Xóa giao dịch theo ID.
- Kiểm tra dữ liệu đầu vào để tránh dữ liệu sai phổ biến.
- Tách logic nghiệp vụ khỏi giao diện dòng lệnh.
- Viết test để xác nhận hành vi quan trọng.


## 2. Mục tiêu học tập

Sau khi hoàn thành dự án, người học nên có thể giải thích được chương trình chạy từ đâu, dữ liệu đi qua các module như thế nào, vì sao cần kiểm tra đầu vào, vì sao phải lưu dữ liệu ra file và test tự động giúp phát hiện lỗi ra sao.

### 2.1 Mục tiêu về Python

- Dùng biến để lưu dữ liệu người dùng nhập.
- Chuyển đổi kiểu dữ liệu từ chuỗi sang số.
- Dùng `if`, `elif`, `else` để xử lý lựa chọn menu.
- Dùng vòng lặp `while` để hiển thị menu nhiều lần.
- Dùng vòng lặp `for` để duyệt danh sách giao dịch.
- Dùng list để quản lý nhiều giao dịch trong bộ nhớ.
- Dùng dictionary để biểu diễn dữ liệu dạng khóa và giá trị.
- Viết hàm nhỏ, có tên rõ ràng và trả về kết quả dễ kiểm tra.
- Dùng `try/except` để xử lý dữ liệu nhập sai.
- Dùng `pathlib` để thao tác với đường dẫn.
- Dùng `json` để đọc và ghi dữ liệu.
- Dùng `pytest` để tự động kiểm thử.

### 2.2 Mục tiêu về thiết kế

- Mỗi module có một nhiệm vụ chính.
- Hàm nghiệp vụ không phụ thuộc vào câu lệnh `input()` hoặc `print()`.
- Giao diện chỉ làm nhiệm vụ tương tác với người dùng.
- Phần lưu trữ không xử lý menu.
- Phần báo cáo không cần biết dữ liệu được nhập từ bàn phím hay test.
- Các hàm có thể được gọi độc lập từ test.

### 2.3 Mục tiêu về thói quen làm dự án

- Đọc yêu cầu trước khi viết code.
- Chia việc lớn thành những chức năng nhỏ.
- Chạy chương trình sau mỗi thay đổi quan trọng.
- Viết test cho trường hợp hợp lệ và không hợp lệ.
- Ghi lại cách cài đặt và chạy trong README.
- Sử dụng Git để lưu các mốc phát triển.


## 3. Phạm vi và tính năng

### 3.1 Thêm giao dịch

Người dùng nhập ngày, loại giao dịch, số tiền, danh mục và ghi chú. Ngày sử dụng định dạng `YYYY-MM-DD`. Loại giao dịch phải là `income` hoặc `expense`. Số tiền phải lớn hơn 0. Danh mục không được để trống.

### 3.2 Xem giao dịch

Ứng dụng in danh sách giao dịch thành các cột gồm ID, ngày, loại, số tiền, danh mục và ghi chú. Nếu không có giao dịch phù hợp, ứng dụng hiển thị thông báo thay vì in bảng rỗng.

### 3.3 Lọc giao dịch

Có thể lọc theo loại giao dịch, theo tháng hoặc kết hợp cả hai. Nếu người dùng nhấn Enter ở một trường lọc, trường đó được bỏ qua. Tháng phải có định dạng `YYYY-MM`, ví dụ `2026-10`.

### 3.4 Báo cáo

Báo cáo tính:
- Tổng thu: tổng số tiền của giao dịch `income`.
- Tổng chi: tổng số tiền của giao dịch `expense`.
- Số dư: tổng thu trừ tổng chi.
- Chi theo danh mục: tổng số tiền chi trong từng danh mục.

Số dư âm có nghĩa là tổng chi lớn hơn tổng thu trong dữ liệu hiện có. Đây chỉ là phép tính trên những giao dịch đã ghi, không phải kết luận về tài chính cá nhân ngoài đời.

### 3.5 Xóa giao dịch

Người dùng nhập ID. Nếu tìm thấy, giao dịch được xóa khỏi danh sách và dữ liệu được lưu lại. Nếu ID không tồn tại, chương trình thông báo không tìm thấy.

### 3.6 Lưu trữ

Dữ liệu được lưu trong `data/transactions.json`. Chương trình đọc dữ liệu lúc khởi động và ghi lại sau khi thêm hoặc xóa giao dịch.

### 3.7 Ngoài phạm vi

Phiên bản hiện tại chưa có tài khoản người dùng, mật khẩu, giao diện web, đồng bộ đám mây, biểu đồ trực quan hoặc cơ sở dữ liệu nhiều người dùng. Những tính năng này có thể được thêm sau khi đã hiểu vững phiên bản hiện tại.


## 4. Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| Python | Ngôn ngữ lập trình chính. |
| `dataclasses` | Tạo lớp dữ liệu `Transaction`. |
| `json` | Đọc và ghi dữ liệu JSON. |
| `pathlib` | Xử lý đường dẫn và file. |
| `datetime.date` | Kiểm tra ngày lịch hợp lệ. |
| `pytest` | Chạy kiểm thử tự động. |
| VS Code | Trình soạn thảo và terminal phát triển. |
| Git | Theo dõi lịch sử thay đổi mã nguồn. |

Ứng dụng không yêu cầu thư viện bên ngoài để chạy chức năng thu chi cơ bản. File `requirements.txt` cài `pytest` để chạy kiểm thử.


## 5. Yêu cầu hệ thống

### 5.1 Phần mềm

- Python 3.10 trở lên, vì mã nguồn dùng kiểu chú thích như `str | None`.
- VS Code hoặc một trình soạn thảo Python tương đương.
- Extension Python của Microsoft trong VS Code.
- Kết nối Internet chỉ cần khi tải Python, extension hoặc cài pytest.

### 5.2 Kiểm tra phiên bản Python

Trong Terminal chạy:

```bash
python --version
```

Trên Windows, nếu lệnh `python` chưa hoạt động, thử:

```powershell
py --version
```

Nếu phiên bản thấp hơn 3.10, hãy cài phiên bản Python mới hơn và chọn đúng interpreter trong VS Code.

### 5.3 Kiểm tra pip

```bash
python -m pip --version
```

Dùng `python -m pip` giúp chắc chắn pip được gọi từ trình thông dịch Python đang sử dụng.


## 6. Cấu trúc thư mục

```text
personal-expense-tracker/
├── .vscode/
│   └── settings.json
├── data/
│   └── transactions.json
├── expense_tracker/
│   ├── __init__.py
│   ├── models.py
│   ├── validators.py
│   ├── storage.py
│   ├── services.py
│   ├── reports.py
│   └── cli.py
├── tests/
│   ├── conftest.py
│   ├── test_validators.py
│   ├── test_storage.py
│   ├── test_services.py
│   └── test_reports.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

### 6.1 Thư mục `expense_tracker`

Đây là package chứa code chính của ứng dụng. File `__init__.py` đánh dấu thư mục là package theo cách tổ chức thông dụng của Python.

### 6.2 Thư mục `data`

Chứa file dữ liệu JSON. File dữ liệu tách khỏi code để người học có thể xem và hiểu định dạng lưu trữ.

### 6.3 Thư mục `tests`

Chứa test tự động. Tên file bắt đầu bằng `test_` để pytest nhận diện theo quy ước mặc định.

### 6.4 Thư mục `.vscode`

Chứa thiết lập dành cho workspace VS Code, trong đó cấu hình pytest được bật cho thư mục `tests`.

### 6.5 File `main.py`

Đây là entry point, nghĩa là file được chạy trực tiếp để khởi động ứng dụng. File này không chứa toàn bộ logic mà gọi hàm `run_app()` từ module giao diện.


## 7. Mô hình dữ liệu

Mỗi giao dịch có sáu trường:

| Trường | Kiểu dữ liệu | Ý nghĩa | Ví dụ |
|---|---|---|---|
| `id` | `int` | Mã giao dịch | `1` |
| `date` | `str` | Ngày giao dịch | `"2026-10-28"` |
| `kind` | `str` | Loại giao dịch | `"expense"` |
| `amount` | `float` | Số tiền dương | `50000.0` |
| `category` | `str` | Danh mục | `"Ăn uống"` |
| `note` | `str` | Ghi chú tùy chọn | `"Ăn trưa"` |

### 7.1 Vì sao có ID?

ID giúp phân biệt các giao dịch ngay cả khi chúng có cùng ngày, số tiền hoặc danh mục. Trong phiên bản này, ID mới bằng ID lớn nhất hiện tại cộng một.

### 7.2 Vì sao loại giao dịch là chuỗi?

Ứng dụng dùng hai giá trị quy ước: `income` và `expense`. Khi hiển thị, CLI chuyển chúng thành nhãn tiếng Việt “Thu” và “Chi”.

### 7.3 Vì sao số tiền được lưu thành số?

Số tiền cần được cộng, trừ và tổng hợp. Vì vậy, ứng dụng chuyển input dạng chuỗi thành số trước khi tính toán.

### 7.4 Lưu ý về tiền tệ

Phiên bản học tập sử dụng `float` để giữ code đơn giản. Với phần mềm tài chính thực tế, nên cân nhắc dùng số nguyên theo đơn vị nhỏ nhất hoặc `Decimal` để tránh sai số dấu phẩy động trong một số phép tính.


## 8. Cài đặt trên Windows bằng VS Code

### Bước 1 — Giải nén

Tải ZIP của dự án và giải nén vào một thư mục dễ tìm, ví dụ thư mục Documents hoặc Desktop. Không chạy chương trình trực tiếp từ bên trong trình xem file ZIP.

### Bước 2 — Mở thư mục

Mở VS Code, chọn **File → Open Folder...**, sau đó chọn thư mục `personal-expense-tracker`. Hãy mở thư mục gốc chứa `main.py`, không chỉ mở riêng thư mục `expense_tracker`.

### Bước 3 — Mở terminal

Chọn **Terminal → New Terminal**. Terminal nên bắt đầu ở thư mục gốc của dự án. Có thể dùng lệnh `dir` để kiểm tra các file.

### Bước 4 — Tạo môi trường ảo

```powershell
py -m venv .venv
```

Môi trường ảo tạo một nơi riêng để cài thư viện cho dự án, tránh làm lẫn các thư viện của những dự án Python khác.

### Bước 5 — Kích hoạt môi trường ảo

```powershell
.\.venv\Scripts\Activate.ps1
```

Nếu thành công, đầu dòng terminal thường hiển thị `(.venv)`.

Nếu PowerShell chặn script kích hoạt, có thể mở terminal Command Prompt trong VS Code và chạy:

```bat
.venv\Scriptsctivate.bat
```

### Bước 6 — Cài pytest

```powershell
python -m pip install -r requirements.txt
```

### Bước 7 — Chọn interpreter

Mở Command Palette bằng `Ctrl+Shift+P`, tìm **Python: Select Interpreter**, rồi chọn Python trong thư mục `.venv`.

### Bước 8 — Chạy chương trình

```powershell
python main.py
```

### Bước 9 — Chạy test

```powershell
python -m pytest -v
```


## 9. Cài đặt trên macOS hoặc Linux

### Bước 1 — Mở Terminal

Mở Terminal trong VS Code tại thư mục dự án.

### Bước 2 — Tạo môi trường ảo

```bash
python3 -m venv .venv
```

### Bước 3 — Kích hoạt

```bash
source .venv/bin/activate
```

### Bước 4 — Cài thư viện

```bash
python -m pip install -r requirements.txt
```

### Bước 5 — Chạy ứng dụng

```bash
python main.py
```

### Bước 6 — Chạy test

```bash
python -m pytest -v
```

Nếu hệ thống dùng lệnh `python3` thay vì `python`, có thể dùng `python3 main.py` và `python3 -m pytest -v`.


## 10. Chạy ứng dụng

Lệnh chạy thông thường:

```bash
python main.py
```

Ứng dụng nạp danh sách giao dịch từ file JSON trước khi hiển thị menu. Menu lặp lại cho đến khi người dùng chọn `0`.

### 10.1 Ý nghĩa lựa chọn menu

| Lựa chọn | Hành động |
|---|---|
| `1` | Thêm giao dịch mới. |
| `2` | Hiển thị tất cả giao dịch. |
| `3` | Lọc giao dịch theo loại và/hoặc tháng. |
| `4` | Hiển thị báo cáo thu chi. |
| `5` | Xóa giao dịch bằng ID. |
| `0` | Thoát chương trình. |

### 10.2 Nếu lệnh không chạy

- Kiểm tra terminal đang ở đúng thư mục gốc.
- Kiểm tra `main.py` có tồn tại.
- Kiểm tra Python đã cài đặt.
- Kiểm tra interpreter trong VS Code.
- Đọc dòng cuối của traceback trước, sau đó tìm file và dòng code liên quan.


## 11. Hướng dẫn chức năng: thêm giao dịch

Chọn `1` rồi nhập từng trường theo yêu cầu.

Ví dụ:

```text
Ngày (YYYY-MM-DD): 2026-10-28
Loại (income/expense): expense
Số tiền: 50000
Danh mục: Ăn uống
Ghi chú (có thể bỏ trống): Ăn trưa
Đã thêm giao dịch ID=6.
```

ID ví dụ có thể thay đổi tùy dữ liệu đang có.

### 11.1 Ngày

Ngày phải đúng định dạng `YYYY-MM-DD`. Ví dụ `2026-10-28` là ngày 28 tháng 10 năm 2026.

### 11.2 Loại

Nhập `income` cho khoản thu hoặc `expense` cho khoản chi. Chương trình bỏ khoảng trắng hai đầu và chuyển chữ về chữ thường.

### 11.3 Số tiền

Số tiền phải chuyển được thành số và lớn hơn 0. Không nhập ký hiệu tiền tệ trong trường số tiền.

### 11.4 Danh mục

Danh mục giúp phân nhóm, ví dụ `Ăn uống`, `Học tập`, `Di chuyển`, `Lương`. Danh mục không được để trống.

### 11.5 Ghi chú

Ghi chú có thể bỏ trống. Nó giúp giải thích giao dịch, chẳng hạn “mua vở” hoặc “làm thêm cuối tuần”.

### 11.6 Điều gì xảy ra sau khi nhập?

CLI gọi `add_transaction()`. Hàm này xác thực dữ liệu, tạo đối tượng `Transaction`, thêm đối tượng vào list và trả về giao dịch mới. CLI sau đó gọi hàm lưu dữ liệu.


## 12. Hướng dẫn chức năng: xem giao dịch

Chọn `2` để xem tất cả giao dịch đã nạp vào bộ nhớ.

Bảng hiển thị ID, ngày, loại, số tiền, danh mục và ghi chú. Nếu danh sách rỗng, chương trình hiển thị thông báo chưa có giao dịch phù hợp.

### 12.1 Đọc bảng

- ID: mã định danh của giao dịch.
- Ngày: ngày phát sinh giao dịch.
- Loại: Thu hoặc Chi.
- Số tiền: số tiền đã nhập.
- Danh mục: nhóm giao dịch.
- Ghi chú: nội dung bổ sung.

### 12.2 Vì sao định dạng bảng trong hàm?

Hàm `show_transactions()` tập trung vào việc trình bày dữ liệu. Nó không tự đọc file và không tự thêm giao dịch, nhờ đó trách nhiệm được tách rõ.


## 13. Hướng dẫn chức năng: lọc giao dịch

Chọn `3`. Bạn có thể nhập loại giao dịch và tháng.

Ví dụ lọc khoản chi trong tháng 10 năm 2026:

```text
Loại (income/expense, Enter để bỏ qua): expense
Tháng (YYYY-MM, Enter để bỏ qua): 2026-10
```

Nếu chỉ muốn lọc theo tháng, nhấn Enter ở câu hỏi loại. Nếu muốn xem tất cả, nhấn Enter ở cả hai trường.

### 13.1 Kết hợp điều kiện

Nếu người dùng chọn cả loại và tháng, giao dịch phải thỏa mãn cả hai điều kiện mới được giữ lại.

### 13.2 Kết quả không có giao dịch

Nếu không giao dịch nào thỏa mãn bộ lọc, hàm trả về list rỗng. CLI hiển thị thông báo thay vì xem đây là lỗi.


## 14. Hướng dẫn chức năng: báo cáo

Chọn `4` để xem báo cáo.

Báo cáo gồm tổng thu, tổng chi, số dư và tổng chi theo danh mục. Tổng thu được tính bằng cách cộng số tiền các giao dịch có `kind == "income"`. Tổng chi được tính tương tự với `kind == "expense"`.

### 14.1 Công thức

```text
Số dư = Tổng thu - Tổng chi
```

Ví dụ, nếu tổng thu là 12.500.000 VND và tổng chi là 415.000 VND, số dư là 12.085.000 VND.

### 14.2 Chi theo danh mục

Các giao dịch chi được gom theo `category`. Nếu có nhiều khoản chi thuộc cùng danh mục, số tiền của chúng được cộng lại.

### 14.3 Không có giao dịch

Nếu danh sách trống, các tổng đều bằng 0. Hàm báo cáo vẫn trả về kết quả hợp lệ.


## 15. Hướng dẫn chức năng: xóa giao dịch

Chọn `5`, sau đó nhập ID muốn xóa.

- Nếu ID tồn tại, giao dịch bị xóa khỏi danh sách và danh sách mới được lưu vào JSON.
- Nếu ID không tồn tại, ứng dụng thông báo không tìm thấy.
- Nếu ID không phải số nguyên, ứng dụng báo ID phải là số nguyên.

### 15.1 Vì sao hàm trả về Boolean?

`delete_transaction()` trả về `True` khi xóa thành công và `False` khi không tìm thấy ID. CLI dựa vào giá trị này để quyết định có cần lưu file hay không.


## 16. Luồng chạy tổng thể

```text
Người dùng chạy python main.py
            |
            v
main.py gọi run_app()
            |
            v
cli.py nạp dữ liệu qua reload_transactions()
            |
            v
storage.py đọc transactions.json
            |
            v
cli.py hiển thị menu trong vòng lặp
            |
            +---- Chọn thêm ----> services.py
            |                         |
            |                         v
            |                   validators.py
            |                         |
            |                         v
            |                   models.py tạo Transaction
            |                         |
            |                         v
            |                   storage.py ghi JSON
            |
            +---- Chọn xem -----> show_transactions()
            |
            +---- Chọn lọc -----> filter_transactions()
            |
            +---- Chọn báo cáo -> reports.py
            |
            +---- Chọn xóa -----> delete_transaction()
            |                         |
            |                         v
            |                   storage.py ghi JSON
            |
            +---- Chọn 0 --------> Thoát
```

Sơ đồ mô tả luồng khái niệm. Tên hàm cụ thể có thể xem trong mã nguồn của từng module.


## 17. Giải thích module models.py

`models.py` định nghĩa lớp `Transaction`, đại diện cho một giao dịch.

### 17.1 `@dataclass`

Decorator này tự tạo một số phương thức tiện ích, trong đó có hàm khởi tạo nhận các trường đã khai báo. Nhờ vậy, không cần tự viết hàm `__init__` dài.

### 17.2 `to_dict()`

Hàm dùng `asdict(self)` để chuyển đối tượng thành dictionary. Dictionary là định dạng phù hợp để tiếp tục chuyển thành JSON.

### 17.3 `from_dict()`

Đây là class method, nhận dictionary rồi tạo một đối tượng `Transaction`. Hàm chuyển ID thành `int` và số tiền thành `float`.

### 17.4 Ví dụ

```python
transaction = Transaction(
    id=10,
    date="2026-10-28",
    kind="income",
    amount=1000000,
    category="Lương",
    note="Lương làm thêm",
)
print(transaction.category)
```

Kết quả:

```text
Lương
```


## 18. Giải thích module validators.py

Module này chứa các hàm kiểm tra đầu vào. Việc gom kiểm tra vào một nơi tránh viết lại cùng quy tắc ở nhiều chức năng.

### 18.1 `validate_date()`

Dùng `date.fromisoformat()` để kiểm tra ngày. Không chỉ kiểm tra hình thức chuỗi, hàm còn phát hiện những ngày không tồn tại trong lịch.

### 18.2 `validate_kind()`

Chuẩn hóa loại giao dịch bằng `strip()` và `lower()`, rồi kiểm tra xem giá trị có thuộc `VALID_KINDS` hay không.

### 18.3 `validate_amount()`

Cố chuyển input thành số thực. Nếu không chuyển được, hàm phát sinh `ValueError` với thông báo dễ hiểu. Số tiền bằng 0 hoặc âm cũng bị từ chối.

### 18.4 `validate_text()`

Loại bỏ khoảng trắng ở đầu và cuối. Nếu giá trị không phải chuỗi hoặc chỉ gồm khoảng trắng, hàm báo lỗi.

### 18.5 `validate_month()`

Kiểm tra định dạng năm-tháng và bảo đảm tháng từ 1 đến 12. Hàm không cho phép tháng 00 hoặc 13.

### 18.6 Nguyên tắc quan trọng

Hàm xác thực nên báo lỗi rõ ràng, không âm thầm thay dữ liệu sai bằng một giá trị khác. Điều này giúp người dùng sửa input và giúp test xác định được hành vi mong muốn.


## 19. Giải thích module storage.py

`storage.py` chịu trách nhiệm đọc và ghi file JSON.

### 19.1 `DEFAULT_DATA_PATH`

Đường dẫn mặc định được tạo từ vị trí file Python bằng `Path(__file__).resolve()`. Cách này giúp ứng dụng tìm file dữ liệu dựa trên cấu trúc dự án thay vì phụ thuộc hoàn toàn vào thư mục terminal hiện tại.

### 19.2 `load_transactions()`

Hàm thực hiện các bước:
1. Chuyển đầu vào thành `Path`.
2. Nếu file chưa tồn tại, tạo thư mục cha và file JSON rỗng `[]`.
3. Nếu file có tồn tại, đọc nội dung UTF-8.
4. Dùng `json.loads()` chuyển chuỗi thành dữ liệu Python.
5. Kiểm tra dữ liệu gốc là list.
6. Chuyển từng dictionary thành `Transaction`.
7. Báo `ValueError` nếu JSON hoặc cấu trúc giao dịch sai.

### 19.3 `save_transactions()`

Hàm tạo thư mục cha nếu cần, chuyển các đối tượng thành dictionary, dùng `json.dumps()` để tạo JSON dễ đọc và ghi ra file.

### 19.4 Vì sao dùng UTF-8?

UTF-8 giúp lưu tiếng Việt trong danh mục và ghi chú mà không cần chuyển sang chuỗi ký tự khó đọc.

### 19.5 Lưu ý về file hỏng

Nếu file JSON bị sửa sai cú pháp, ứng dụng báo lỗi và yêu cầu người dùng sửa file. Không nên tự động ghi đè file hỏng bằng danh sách rỗng vì có thể làm mất dữ liệu cũ.


## 20. Giải thích module services.py

`services.py` chứa các thao tác nghiệp vụ chính.

### 20.1 `add_transaction()`

Hàm nhận danh sách giao dịch và các trường dữ liệu. Sau khi xác thực, hàm tạo ID tiếp theo, tạo `Transaction`, thêm vào list và trả về đối tượng mới.

### 20.2 `filter_transactions()`

Hàm nhận bộ lọc tùy chọn. Nếu có loại giao dịch, kiểm tra loại trước. Nếu có tháng, kiểm tra tháng rồi chỉ giữ các giao dịch có ngày bắt đầu bằng chuỗi năm-tháng đó.

### 20.3 `delete_transaction()`

Hàm duyệt danh sách kèm chỉ số bằng `enumerate()`. Khi tìm thấy ID cần xóa, hàm xóa phần tử đó và trả về `True`. Nếu duyệt hết mà không tìm thấy, trả về `False`.

### 20.4 `persist()`

Hàm gọi `save_transactions()` để lưu danh sách hiện tại vào file dữ liệu mặc định.

### 20.5 `reload_transactions()`

Hàm gọi `load_transactions()` để nạp dữ liệu mới nhất từ file mặc định.

### 20.6 Vì sao tách service khỏi CLI?

Nhờ tách riêng, test có thể gọi `add_transaction()` trực tiếp mà không phải giả lập bàn phím. Đây là cách thiết kế giúp code dễ kiểm thử hơn.


## 21. Giải thích module reports.py

Module báo cáo không đọc input và không ghi file. Nó nhận list giao dịch rồi trả về kết quả tính toán.

### 21.1 `calculate_totals()`

Dùng `sum()` kết hợp generator expression để tính tổng thu và tổng chi. Kết quả là dictionary có ba khóa `income`, `expense`, `balance`.

### 21.2 `summarize_by_category()`

Duyệt từng giao dịch. Chỉ xử lý loại giao dịch được chọn, mặc định là `expense`. Dùng dictionary để cộng dồn số tiền theo danh mục.

### 21.3 `format_money()`

Định dạng số tiền có dấu phân cách hàng nghìn và thêm hậu tố `VND`.

### 21.4 Tại sao báo cáo không in trực tiếp?

Trả về dữ liệu giúp phần tính toán dễ kiểm thử. CLI chịu trách nhiệm quyết định cách hiển thị kết quả cho người dùng.


## 22. Giải thích module cli.py

`cli.py` là giao diện dòng lệnh. Nó nhận input, gọi service, hiển thị kết quả và xử lý thông báo lỗi phù hợp.

### 22.1 `show_transactions()`

Hiển thị danh sách giao dịch thành bảng. Nếu danh sách rỗng, thông báo và kết thúc hàm sớm bằng `return`.

### 22.2 `_add_flow()`

Nhận các trường từ người dùng, gọi `add_transaction()`, lưu dữ liệu nếu thành công. Nếu dữ liệu không hợp lệ, bắt `ValueError` và in thông báo.

### 22.3 `_filter_flow()`

Nhận các điều kiện lọc tùy chọn. Chuỗi rỗng được chuyển thành `None`, nghĩa là bỏ qua điều kiện đó.

### 22.4 `_delete_flow()`

Chuyển ID nhập vào thành số nguyên. Nếu chuyển đổi thất bại, in lỗi và không tiếp tục xóa. Nếu xóa thành công, lưu lại dữ liệu.

### 22.5 `_show_report()`

Gọi hàm tính tổng và thống kê danh mục, sau đó định dạng các giá trị để hiển thị.

### 22.6 `run_app()`

Nạp dữ liệu ban đầu, sau đó chạy vòng lặp menu. Mỗi lựa chọn dẫn tới một hàm tương ứng. Khi lựa chọn là `0`, vòng lặp kết thúc.


## 23. Quy tắc xác thực dữ liệu

| Trường | Hợp lệ | Không hợp lệ |
|---|---|---|
| Ngày | `2026-10-28` | `28/10/2026`, ngày không tồn tại |
| Loại | `income`, `expense` | `cash`, chuỗi rỗng |
| Số tiền | `10000`, `25000.5` | `abc`, `0`, `-1` |
| Danh mục | `Ăn uống` | chỉ có khoảng trắng |
| Tháng | `2026-10` | `2026-00`, `2026-13` |
| ID xóa | số nguyên | chữ hoặc chuỗi không chuyển được thành số |

### 23.1 Tại sao cần xác thực?

Dữ liệu từ `input()` luôn bắt đầu dưới dạng chuỗi. Nếu chương trình trực tiếp dùng dữ liệu đó để tính toán, có thể phát sinh lỗi kiểu dữ liệu hoặc lưu giá trị không hợp lệ.

### 23.2 Kiểm tra ở đâu?

Các quy tắc dữ liệu tập trung trong `validators.py`. CLI vẫn xử lý lỗi để hiển thị thông báo thân thiện, nhưng service cũng gọi validator để bảo vệ nghiệp vụ kể cả khi được gọi từ test hoặc module khác.


## 24. Lưu dữ liệu JSON

File dữ liệu có dạng list các object JSON.

Ví dụ một giao dịch:

```json
[
  {
    "id": 1,
    "date": "2026-10-01",
    "kind": "income",
    "amount": 12000000,
    "category": "Lương",
    "note": "Lương tháng 10"
  }
]
```

### 24.1 Vì sao JSON?

JSON dễ đọc, dễ chỉnh sửa bằng trình soạn thảo văn bản và có hỗ trợ sẵn trong Python qua module `json`.

### 24.2 Tạo dữ liệu trống

Sao lưu file trước, sau đó có thể thay nội dung thành:

```json
[]
```

### 24.3 Không chỉnh sửa đồng thời

Khi ứng dụng đang chạy, nên tránh sửa file JSON bằng một chương trình khác. Nếu sửa thủ công, hãy thoát ứng dụng trước và giữ một bản sao lưu.

### 24.4 Giới hạn của JSON

JSON phù hợp cho dự án học tập nhỏ. Nếu dữ liệu lớn, có nhiều người dùng hoặc cần cập nhật đồng thời, nên cân nhắc SQLite hoặc một hệ quản trị cơ sở dữ liệu.


## 25. Kiểm thử bằng pytest

Cài pytest bằng:

```bash
python -m pip install -r requirements.txt
```

Chạy toàn bộ test:

```bash
python -m pytest -v
```

Chạy một nhóm test:

```bash
python -m pytest tests/test_services.py -v
```

Chạy một test theo tên:

```bash
python -m pytest -k delete -v
```

### 25.1 Vai trò của `conftest.py`

File này thêm thư mục gốc dự án vào `sys.path`, giúp test import package `expense_tracker` khi chạy pytest.

### 25.2 `assert`

`assert actual == expected` kiểm tra kết quả thực tế có bằng kết quả mong đợi hay không.

### 25.3 `pytest.raises`

Dùng để xác nhận một đoạn code phát sinh ngoại lệ như dự kiến.

### 25.4 `pytest.mark.parametrize`

Cho phép chạy cùng một test với nhiều giá trị đầu vào. Cách này hữu ích khi kiểm tra nhiều dạng dữ liệu sai.

### 25.5 `tmp_path`

Pytest cung cấp fixture `tmp_path` để test đọc ghi file trong thư mục tạm. Nhờ đó test lưu trữ không làm thay đổi file dữ liệu mẫu thật.


## 26. Danh sách test và mục tiêu

### 26.1 `test_validators.py`

Kiểm tra:
- Ngày ISO hợp lệ.
- Ngày sai định dạng.
- Ngày không tồn tại.
- Chuẩn hóa loại giao dịch.
- Từ chối loại không được hỗ trợ.
- Chuyển chuỗi số thành số.
- Từ chối số tiền không hợp lệ.
- Loại bỏ khoảng trắng trong danh mục.
- Từ chối nội dung rỗng.
- Chấp nhận tháng hợp lệ.
- Từ chối tháng ngoài phạm vi.

### 26.2 `test_services.py`

Kiểm tra:
- Thêm giao dịch và gán ID tiếp theo.
- Không thêm giao dịch khi dữ liệu sai.
- Lọc theo loại và tháng cùng lúc.
- Kết quả lọc rỗng.
- Xóa ID tồn tại.
- ID không tồn tại không làm thay đổi danh sách.

### 26.3 `test_reports.py`

Kiểm tra:
- Tổng thu.
- Tổng chi.
- Số dư.
- Tổng của danh sách rỗng.
- Tổng chi theo danh mục.
- Định dạng số tiền.

### 26.4 `test_storage.py`

Kiểm tra:
- Lưu và đọc lại giao dịch.
- Tạo file khi chưa tồn tại.
- Phát hiện JSON sai cú pháp.
- Phát hiện dữ liệu JSON không phải list.

### 26.5 Test không thay thế kiểm tra thủ công

Test tự động xác nhận logic ở các hàm. Người học vẫn nên chạy ứng dụng thật để kiểm tra trải nghiệm menu và luồng nhập liệu.


## 27. Kiểm thử thủ công

Dùng checklist sau sau mỗi lần thay đổi chương trình:

- [ ] Chạy ứng dụng từ `main.py`.
- [ ] Xem dữ liệu mẫu.
- [ ] Thêm một khoản thu hợp lệ.
- [ ] Thêm một khoản chi hợp lệ.
- [ ] Thử nhập số tiền là `abc`.
- [ ] Thử nhập số tiền bằng `0`.
- [ ] Thử nhập số tiền âm.
- [ ] Thử nhập ngày sai định dạng.
- [ ] Thử nhập ngày không tồn tại.
- [ ] Thử để trống danh mục.
- [ ] Lọc theo loại `income`.
- [ ] Lọc theo loại `expense`.
- [ ] Lọc theo tháng hợp lệ.
- [ ] Lọc tháng không có giao dịch.
- [ ] Xem báo cáo.
- [ ] Xóa một ID có thật.
- [ ] Xóa một ID không tồn tại.
- [ ] Nhập chữ thay cho ID.
- [ ] Thoát và chạy lại ứng dụng.
- [ ] Kiểm tra giao dịch đã thêm vẫn tồn tại.
- [ ] Chạy lại toàn bộ pytest.

Ghi lại kết quả nếu phát hiện lỗi. Một báo cáo lỗi tốt gồm các bước tái hiện, dữ liệu đầu vào, kết quả thực tế và kết quả mong muốn.


## 28. Ánh xạ Week 01–15

| Week | Kiến thức | Áp dụng trong dự án |
|---|---|---|
| 01 | Terminal, Python, thư mục, Git/GitHub | Tạo dự án và chạy lệnh. |
| 02 | Biến, kiểu dữ liệu, input/output | Nhận và hiển thị dữ liệu. |
| 03 | Điều kiện Boolean | Menu, xác thực loại và số tiền. |
| 04 | Chuỗi và xử lý text | Chuẩn hóa input, định dạng thông báo. |
| 05 | List, tuple, mutability | Danh sách giao dịch và thao tác xóa. |
| 06 | Vòng lặp, enumerate, comprehension | Duyệt giao dịch, lọc và chuyển đổi dữ liệu. |
| 07 | Hàm và phạm vi biến | Tách nhiệm vụ thành hàm. |
| 08 | Dictionary, set, mô hình dữ liệu | Biểu diễn giao dịch và thống kê danh mục. |
| 09 | Dự án tổng hợp giữa kỳ | Kết hợp các kiến thức cơ bản thành ứng dụng. |
| 10 | File, pathlib, CSV/JSON | Đọc và ghi file JSON. |
| 11 | Exception, traceback, defensive coding | Bắt lỗi dữ liệu sai và file JSON lỗi. |
| 12 | Kiểm thử pytest | Test hợp lệ, không hợp lệ và trường hợp biên. |
| 13 | Module, package, CLI | Chia package và entry point. |
| 14 | OOP, composition, inheritance cơ bản | Mô hình `Transaction` bằng `dataclass`. |
| 15 | Capstone | Hoàn thiện tính năng, test, tài liệu và demo. |

Không phải mọi chủ đề của mỗi tuần đều cần xuất hiện trực tiếp trong code. Ví dụ, dự án này không cần dùng HTTP chỉ để chứng minh đã học HTTP; thay vào đó, các kiến thức được chọn theo mức độ phù hợp với bài toán.


## 29. Quy trình debug

Khi gặp lỗi, làm theo chu trình:

1. Tái hiện lỗi bằng các bước cụ thể.
2. Đọc dòng cuối traceback để biết loại exception và thông báo.
3. Tìm frame gần code của dự án nhất.
4. Xác định dữ liệu đầu vào gây lỗi.
5. Thu nhỏ ví dụ để cô lập nguyên nhân.
6. Sửa một nguyên nhân tại một thời điểm.
7. Chạy lại test liên quan.
8. Chạy toàn bộ test để phát hiện hồi quy.
9. Thử lại luồng thủ công trong ứng dụng.

### 29.1 Ví dụ lỗi nhập số

Nếu người dùng nhập `abc` vào số tiền, `float("abc")` phát sinh `ValueError`. Validator bắt lỗi chuyển đổi và phát sinh thông báo nghiệp vụ dễ hiểu hơn. CLI bắt `ValueError` đó và hiển thị cho người dùng.

### 29.2 Tránh bắt mọi lỗi một cách mù quáng

Không nên dùng `except Exception: pass`, vì cách này có thể che giấu lỗi lập trình. Chỉ bắt những ngoại lệ mà chương trình biết cách xử lý.


## 30. Git và GitHub

### 30.1 Khởi tạo repository

Từ thư mục dự án:

```bash
git init
git status
```

### 30.2 Thêm file và commit

```bash
git add .
git commit -m "Build personal expense tracker"
```

### 30.3 Kiểm tra trạng thái

```bash
git status
```

### 30.4 Xem lịch sử

```bash
git log --oneline
```

### 30.5 Lưu ý

- Không commit thư mục `.venv`.
- Không commit dữ liệu tài chính cá nhân thật.
- Nên giữ dữ liệu mẫu giả lập trong repository.
- Đọc quy định của repository lớp học trước khi tạo thư mục hoặc mở Pull Request.
- Nếu dự án được đặt vào repository lớn hơn, cần kiểm tra `.gitignore` ở cả thư mục gốc.


## 31. Demo trước lớp

Một buổi demo ngắn có thể theo thứ tự sau:

1. Giới thiệu bài toán quản lý thu chi.
2. Cho xem cấu trúc thư mục.
3. Chạy `python main.py`.
4. Xem dữ liệu mẫu.
5. Thêm một giao dịch chi.
6. Thử nhập số tiền sai để chứng minh validation.
7. Xem báo cáo tổng thu, tổng chi và số dư.
8. Thoát ứng dụng rồi chạy lại để chứng minh dữ liệu được lưu.
9. Chạy `python -m pytest -v`.
10. Giải thích một test và một hàm nghiệp vụ.
11. Kết thúc bằng hướng nâng cấp.

### 31.1 Lời giới thiệu mẫu

“Đây là Personal Expense Tracker, ứng dụng quản lý thu chi cá nhân viết bằng Python. Dự án dùng menu terminal, chia logic thành các module, lưu giao dịch bằng JSON và dùng pytest để kiểm tra các chức năng chính.”

### 31.2 Điểm cần nhấn mạnh

- Chia module để mỗi file có một trách nhiệm rõ ràng.
- Validation ngăn dữ liệu đầu vào sai.
- JSON giúp dữ liệu tồn tại sau khi chương trình kết thúc.
- Test tự động giúp phát hiện lỗi khi sửa code.
- README giúp người khác cài đặt và chạy dự án.


## 32. Câu hỏi thường gặp

### Hỏi: Vì sao chạy `python main.py` báo không tìm thấy module?

Kiểm tra bạn đã mở đúng thư mục gốc và chạy lệnh tại nơi có file `main.py` chưa. Không chạy từ bên trong `expense_tracker` nếu chưa cấu hình đường dẫn phù hợp.

### Hỏi: Vì sao `pytest` không được nhận diện?

Hãy kích hoạt môi trường ảo rồi chạy `python -m pip install -r requirements.txt`. Sau đó chạy `python -m pytest -v`.

### Hỏi: Dữ liệu có mất khi tắt chương trình không?

Giao dịch đã thêm hoặc xóa thành công được lưu vào JSON. Dữ liệu chưa được lưu, hoặc file bị xóa thủ công, có thể không còn.

### Hỏi: Có thể đổi tên danh mục không?

Có thể nhập tên danh mục khác khi tạo giao dịch. Phiên bản hiện tại chưa có chức năng đổi danh mục của giao dịch đã lưu.

### Hỏi: Có thể dùng dấu phẩy trong số tiền không?

Phiên bản hiện tại yêu cầu nhập dạng số mà `float()` có thể chuyển đổi, ví dụ `1200000`. Không nhập chuỗi định dạng như `1,200,000`.

### Hỏi: Có thể dùng tiếng Việt cho loại giao dịch không?

Hiện tại quy ước nội bộ là `income` và `expense`. CLI hiển thị “Thu” và “Chi” khi xem bảng. Có thể bổ sung lựa chọn tiếng Việt ở giao diện sau này.

### Hỏi: Tại sao không dùng database?

JSON đơn giản và phù hợp mục tiêu học file. SQLite là một bước nâng cấp hợp lý khi muốn học truy vấn, khóa chính và giao dịch cơ sở dữ liệu.

### Hỏi: Dữ liệu mẫu có phải dữ liệu thật không?

Không. Dữ liệu trong repository là dữ liệu giả lập để demo.


## 33. Hạn chế hiện tại

- Giao diện chỉ chạy trong terminal.
- Chưa có đăng nhập và phân quyền.
- Chưa có chức năng sửa giao dịch.
- Chưa có tìm kiếm theo từ khóa ghi chú.
- Chưa có xuất báo cáo CSV.
- Chưa có biểu đồ trực quan.
- Chưa có sao lưu tự động theo thời gian.
- Chưa có đồng bộ nhiều thiết bị.
- File JSON không tối ưu cho nhiều tiến trình cùng ghi dữ liệu.
- Số tiền dùng `float`, phù hợp học tập nhưng không phải lựa chọn lý tưởng cho hệ thống tài chính yêu cầu độ chính xác tuyệt đối.


## 34. Ý tưởng nâng cấp

Có thể phát triển dự án theo từng cấp độ.

### Cấp độ 1 — Dễ

- Thêm chức năng sửa giao dịch.
- Thêm lọc theo danh mục.
- Thêm tìm kiếm theo ghi chú.
- Thêm xác nhận trước khi xóa.
- Thêm lựa chọn bắt đầu với dữ liệu rỗng.

### Cấp độ 2 — Trung bình

- Xuất giao dịch ra CSV.
- Nhập giao dịch từ CSV.
- Báo cáo theo từng tháng.
- Hiển thị khoản chi lớn nhất.
- Kiểm tra ID bị trùng trong file JSON.
- Tạo file sao lưu trước khi ghi dữ liệu.

### Cấp độ 3 — Nâng cao

- Chuyển từ JSON sang SQLite.
- Thêm lớp repository để tách nghiệp vụ khỏi kiểu lưu trữ.
- Tạo giao diện đồ họa.
- Xây dựng API HTTP.
- Thêm báo cáo trực quan.
- Thêm cấu hình đường dẫn dữ liệu từ dòng lệnh.
- Thêm logging thay vì chỉ in thông báo.


## 35. Checklist hoàn thành

### Cài đặt

- [ ] Python 3.10 trở lên đã được cài.
- [ ] VS Code đã mở đúng thư mục dự án.
- [ ] Môi trường ảo `.venv` đã được tạo.
- [ ] Đã chọn đúng Python interpreter.
- [ ] Đã cài pytest.

### Chức năng

- [ ] Chương trình khởi động được.
- [ ] Có thể xem giao dịch.
- [ ] Có thể thêm giao dịch hợp lệ.
- [ ] Có thể lọc theo loại.
- [ ] Có thể lọc theo tháng.
- [ ] Báo cáo thu chi chính xác với dữ liệu đã nhập.
- [ ] Có thể xóa giao dịch.
- [ ] Dữ liệu được lưu sau khi thêm hoặc xóa.
- [ ] Dữ liệu còn sau khi chạy lại chương trình.
- [ ] Dữ liệu sai được xử lý bằng thông báo rõ ràng.

### Kiểm thử và tài liệu

- [ ] Toàn bộ pytest chạy thành công.
- [ ] Đã thử một số trường hợp nhập sai bằng tay.
- [ ] README mô tả cài đặt và cách chạy.
- [ ] Đã hiểu vai trò của từng module.
- [ ] Đã chuẩn bị demo.
- [ ] Đã kiểm tra `git status` trước khi commit.


## 36. Thuật ngữ

| Thuật ngữ | Giải thích ngắn |
|---|---|
| CLI | Giao diện dòng lệnh. |
| Module | Một file Python có thể import. |
| Package | Thư mục tổ chức các module Python. |
| Entry point | Điểm bắt đầu chạy chương trình. |
| JSON | Định dạng văn bản lưu dữ liệu có cấu trúc. |
| Persistence | Lưu dữ liệu để dùng lại sau khi chương trình kết thúc. |
| Validation | Kiểm tra dữ liệu đầu vào. |
| Exception | Đối tượng biểu diễn một lỗi hoặc tình huống bất thường. |
| Traceback | Thông tin các lời gọi hàm dẫn đến lỗi. |
| Unit test | Test một đơn vị nhỏ như hàm hoặc phương thức. |
| Regression | Lỗi cũ xuất hiện lại sau khi thay đổi code. |
| Fixture | Dữ liệu hoặc tài nguyên được pytest chuẩn bị cho test. |
| `assert` | Kiểm tra điều kiện mong muốn đúng. |
| `dataclass` | Công cụ tạo lớp dữ liệu ngắn gọn. |
| `pathlib` | Module thao tác đường dẫn theo hướng đối tượng. |


## 37. Phụ lục: các lệnh thường dùng

### Xem phiên bản Python

```bash
python --version
```

### Tạo môi trường ảo trên Windows

```powershell
py -m venv .venv
```

### Kích hoạt môi trường ảo trên Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Cài dependency

```bash
python -m pip install -r requirements.txt
```

### Chạy ứng dụng

```bash
python main.py
```

### Chạy toàn bộ test

```bash
python -m pytest -v
```

### Chạy test theo file

```bash
python -m pytest tests/test_storage.py -v
```

### Chạy test theo từ khóa

```bash
python -m pytest -k amount -v
```

### Kiểm tra Git

```bash
git status
git log --oneline
```


## 38. Phụ lục: ví dụ dữ liệu mẫu

File `data/transactions.json` được chuẩn bị sẵn để ứng dụng có dữ liệu khi chạy lần đầu. Ví dụ cấu trúc giao dịch:

```json
{
  "id": 2,
  "date": "2026-10-03",
  "kind": "expense",
  "amount": 45000,
  "category": "Ăn uống",
  "note": "Ăn sáng"
}
```

Khi đọc file, `storage.py` chuyển dictionary thành đối tượng `Transaction`. Khi lưu file, đối tượng được chuyển lại thành dictionary rồi thành JSON. Hai chiều chuyển đổi giúp chương trình dùng đối tượng trong logic nhưng vẫn lưu dữ liệu ở định dạng văn bản.


## 39. Phụ lục: nguyên tắc viết code dễ bảo trì

- Dùng tên hàm mô tả hành động, ví dụ `add_transaction`.
- Mỗi hàm nên có một trách nhiệm chính.
- Tách input/output khỏi logic nghiệp vụ.
- Kiểm tra dữ liệu ở ranh giới hệ thống.
- Dùng ngoại lệ cụ thể thay vì bắt mọi lỗi.
- Không lặp lại cùng một quy tắc xác thực ở nhiều nơi.
- Viết test cho hành vi quan trọng.
- Giữ README đồng bộ với code.
- Trước khi commit, chạy test và kiểm tra diff.
- Không đưa dữ liệu cá nhân hoặc bí mật vào repository công khai.


## 40. Kết luận

Personal Expense Tracker là dự án thực hành tổng hợp phù hợp để củng cố Python từ nền tảng đến capstone. Giá trị quan trọng nhất không chỉ là ứng dụng chạy được, mà là người học hiểu được trách nhiệm của từng module, luồng dữ liệu, cách xác thực đầu vào, cách lưu dữ liệu, cách kiểm thử và cách viết tài liệu cho người dùng khác.

Khi có thể tự giải thích từng hàm, sửa một chức năng nhỏ, viết test mới và chạy lại toàn bộ test, bạn đã thực hành được quy trình phát triển phần mềm cơ bản: xác định yêu cầu, thiết kế, triển khai, kiểm thử, tài liệu hóa và cải tiến.

**Bước tiếp theo đề xuất:** chạy dự án trong VS Code, xem dữ liệu mẫu, thêm một giao dịch, chạy pytest và lần lượt đọc từng module theo thứ tự trong phần cấu trúc thư mục.


## Quy trình thêm giao dịch

- Người dùng bắt đầu ở menu và chọn chức năng thêm giao dịch.
- CLI thu thập dữ liệu từ bàn phím dưới dạng chuỗi.
- Service gọi validator cho từng trường cần kiểm tra.
- Validator trả về giá trị đã chuẩn hóa hoặc phát sinh ValueError.
- Service tính ID mới dựa trên danh sách hiện có.
- Đối tượng Transaction được tạo từ dữ liệu hợp lệ.
- Đối tượng được thêm vào danh sách đang nằm trong bộ nhớ.
- CLI gọi persist để lưu danh sách xuống file.
- Thông báo thành công chỉ xuất hiện sau khi các bước trước hoàn tất.
- Người học có thể đặt breakpoint ở cli.py và services.py để quan sát luồng.


## Quy trình lọc giao dịch

- CLI nhận loại giao dịch và tháng từ người dùng.
- Chuỗi rỗng được đổi thành None để biểu thị không lọc theo trường đó.
- Service bắt đầu với danh sách ban đầu.
- Nếu có loại, service xác thực loại.
- Danh sách được lọc để giữ giao dịch đúng loại.
- Nếu có tháng, service xác thực tháng.
- Danh sách tiếp tục được lọc theo tiền tố YYYY-MM của ngày.
- Kết quả là một danh sách mới; danh sách gốc không bị xóa phần tử.
- CLI đưa kết quả vào hàm hiển thị bảng.
- Nếu kết quả rỗng, ứng dụng hiển thị thông báo thân thiện.


## Quy trình báo cáo

- CLI gọi calculate_totals với danh sách giao dịch.
- Hàm tính tổng các giao dịch income.
- Hàm tính tổng các giao dịch expense.
- Số dư được tính bằng tổng thu trừ tổng chi.
- CLI định dạng từng tổng thành chuỗi tiền tệ.
- CLI gọi summarize_by_category để gom khoản chi.
- Hàm dùng dictionary để cộng dồn theo danh mục.
- CLI sắp xếp danh mục theo số tiền giảm dần.
- Người dùng xem tổng quát và chi tiết theo danh mục.
- Test kiểm tra kết quả bằng các giá trị số cụ thể.


## Quy trình xóa giao dịch

- CLI yêu cầu người dùng nhập ID.
- Giá trị đầu vào được chuyển thành số nguyên.
- Nếu chuyển đổi thất bại, CLI báo lỗi và dừng thao tác.
- Service duyệt danh sách cùng chỉ số bằng enumerate.
- Khi tìm được ID, phần tử tương ứng bị xóa.
- Hàm trả về True khi xóa thành công.
- Nếu không tìm được, hàm trả về False.
- CLI chỉ ghi file khi có giao dịch bị xóa.
- Thông báo cho người dùng phụ thuộc vào kết quả Boolean.
- Test bảo đảm ID không tồn tại không làm thay đổi danh sách.


## Bài tập tự luyện

- Thêm test xác nhận validate_amount chấp nhận số nguyên dương.
- Thêm test xác nhận validate_amount từ chối số âm.
- Thêm test xác nhận danh mục được bỏ khoảng trắng hai đầu.
- Thêm test lọc theo income trong một tháng cụ thể.
- Thêm test tính số dư âm khi tổng chi lớn hơn tổng thu.
- Thêm test lưu một giao dịch có ghi chú tiếng Việt.
- Thêm chức năng lọc theo danh mục.
- Thêm chức năng sửa ghi chú của giao dịch.
- Thêm chức năng xác nhận trước khi xóa.
- Viết mô tả cho từng chức năng mới vào README.


## Checklist debug nâng cao

- Xác nhận lỗi có thể tái hiện nhiều lần.
- Ghi lại input chính xác gây lỗi.
- Đọc exception type ở cuối traceback.
- Xác định file và dòng code gần nhất thuộc dự án.
- Kiểm tra biến đầu vào có đúng kiểu không.
- Kiểm tra dữ liệu JSON có đúng cấu trúc không.
- Viết test nhỏ tái hiện lỗi nếu có thể.
- Sửa lỗi ở nơi chịu trách nhiệm phù hợp.
- Chạy test liên quan trước.
- Chạy toàn bộ test sau khi sửa.


## Hướng dẫn review code

- Đọc tên file để hiểu trách nhiệm module.
- Đọc chữ ký hàm để hiểu input và output.
- Kiểm tra hàm có làm quá nhiều việc không.
- Kiểm tra hàm có phụ thuộc trực tiếp vào input hoặc print không.
- Kiểm tra trường hợp dữ liệu rỗng.
- Kiểm tra trường hợp dữ liệu sai.
- Kiểm tra có ngoại lệ bị bỏ qua không.
- Kiểm tra test có xác nhận hành vi thực sự không.
- Kiểm tra README có mô tả đúng code không.
- Chạy test trước khi chấp nhận thay đổi.


## Chuẩn bị nộp bài

- Kiểm tra tên dự án và tên thư mục.
- Kiểm tra README có lệnh cài đặt và chạy.
- Kiểm tra dữ liệu mẫu không chứa thông tin cá nhân thật.
- Kiểm tra requirements.txt có pytest.
- Kiểm tra file .gitignore bỏ qua môi trường ảo.
- Chạy ứng dụng từ thư mục gốc.
- Chạy toàn bộ pytest.
- Kiểm tra không còn file tạm không cần thiết.
- Kiểm tra Git diff trước khi commit.
- Chuẩn bị giải thích ít nhất một hàm và một test.


## 41. Thuật ngữ mở rộng kèm ví dụ

### 1. Biến

Tên tham chiếu tới một giá trị trong chương trình.

Ví dụ: `amount = 50000`

### 2. Kiểu dữ liệu

Cho biết dữ liệu có thể biểu diễn và thao tác theo cách nào.

Ví dụ: `int, float, str, list, dict`

### 3. List

Dãy phần tử có thứ tự, có thể thay đổi.

Ví dụ: `transactions = []`

### 4. Dictionary

Cấu trúc lưu cặp khóa-giá trị.

Ví dụ: `record = {'kind': 'expense'}`

### 5. Hàm

Khối code được đặt tên và có thể gọi lại.

Ví dụ: `def calculate_totals(...):`

### 6. Tham số

Tên biến nhận dữ liệu truyền vào hàm.

Ví dụ: `def validate_kind(kind):`

### 7. Giá trị trả về

Kết quả hàm gửi lại nơi gọi.

Ví dụ: `return normalized`

### 8. Ngoại lệ

Cơ chế báo lỗi hoặc tình huống bất thường.

Ví dụ: `raise ValueError('...')`

### 9. try/except

Cấu trúc thử chạy code và xử lý loại lỗi dự kiến.

Ví dụ: `try: amount = float(raw)`

### 10. JSON

Định dạng dữ liệu văn bản có object, array và giá trị cơ bản.

Ví dụ: `json.dumps(data)`

### 11. Path

Đối tượng đại diện đường dẫn file hoặc thư mục.

Ví dụ: `Path('data/transactions.json')`

### 12. Package

Cách nhóm các module liên quan trong một thư mục.

Ví dụ: `expense_tracker`

### 13. Import

Đưa tên hoặc chức năng từ module khác vào module hiện tại.

Ví dụ: `from expense_tracker.models import Transaction`

### 14. Test

Code kiểm tra hành vi của code khác.

Ví dụ: `assert validate_kind('income') == 'income'`

### 15. Fixture

Tài nguyên pytest cung cấp cho test.

Ví dụ: `tmp_path`

### 16. Refactor

Cải thiện cấu trúc code mà giữ nguyên hành vi mong muốn.

Ví dụ: `tách hàm dài thành hàm nhỏ`

### 17. CLI

Giao diện tương tác bằng văn bản trong terminal.

Ví dụ: `python main.py`

### 18. Persistence

Giữ dữ liệu sau khi chương trình kết thúc.

Ví dụ: `ghi giao dịch vào JSON`

### 19. Validation

Xác nhận dữ liệu đáp ứng quy tắc.

Ví dụ: `validate_amount('50000')`

### 20. Traceback

Dấu vết lời gọi dẫn tới exception.

Ví dụ: `đọc từ dòng cuối để bắt đầu tìm lỗi`


## 42. Bảng tình huống và phản ứng của ứng dụng

### 1. Người dùng nhập ngày sai

validate_date phát sinh ValueError; CLI bắt lỗi và hiển thị lý do.

### 2. Người dùng nhập loại không hỗ trợ

validate_kind từ chối giá trị ngoài income/expense.

### 3. Người dùng nhập số tiền chữ

float chuyển đổi thất bại và được chuyển thành thông báo ValueError.

### 4. Người dùng nhập số tiền bằng không

Điều kiện amount <= 0 từ chối giao dịch.

### 5. Người dùng để trống danh mục

validate_text phát sinh lỗi vì danh mục bắt buộc.

### 6. Người dùng lọc tháng sai

validate_month từ chối định dạng hoặc tháng ngoài 1–12.

### 7. Người dùng xóa ID không tồn tại

Hàm trả về False và dữ liệu không bị ghi lại.

### 8. File dữ liệu chưa tồn tại

load_transactions tạo file chứa list rỗng.

### 9. File dữ liệu sai JSON

load_transactions báo lỗi để người dùng sửa file.

### 10. File JSON chứa object thay vì list

storage từ chối cấu trúc không đúng yêu cầu.

### 11. Danh sách giao dịch rỗng

Báo cáo trả về tổng thu, tổng chi và số dư bằng 0.

### 12. Không có kết quả lọc

CLI hiển thị thông báo chưa có giao dịch phù hợp.


## 43. Kế hoạch học theo tuần

### Week 01

**Chủ đề:** Môi trường và terminal

**Việc thực hành:** Mở thư mục, kiểm tra Python, chạy main.py.

### Week 02

**Chủ đề:** Biến và kiểu dữ liệu

**Việc thực hành:** Quan sát input là chuỗi rồi chuyển số tiền thành float.

### Week 03

**Chủ đề:** Điều kiện

**Việc thực hành:** Giải thích nhánh menu và điều kiện amount <= 0.

### Week 04

**Chủ đề:** Chuỗi

**Việc thực hành:** Giải thích strip, lower, startswith và định dạng chuỗi.

### Week 05

**Chủ đề:** List và mutability

**Việc thực hành:** Quan sát append, del và việc danh sách thay đổi.

### Week 06

**Chủ đề:** Vòng lặp

**Việc thực hành:** Giải thích for, enumerate, sum và list comprehension.

### Week 07

**Chủ đề:** Hàm

**Việc thực hành:** Mô tả input, xử lý, output của từng hàm.

### Week 08

**Chủ đề:** Dictionary và mô hình dữ liệu

**Việc thực hành:** Giải thích transaction dictionary và tổng theo danh mục.

### Week 09

**Chủ đề:** Dự án giữa kỳ

**Việc thực hành:** Chia yêu cầu thành tính năng và ghép các kiến thức đã học.

### Week 10

**Chủ đề:** File và JSON

**Việc thực hành:** Thêm giao dịch rồi mở file JSON để quan sát.

### Week 11

**Chủ đề:** Debug và defensive coding

**Việc thực hành:** Nhập dữ liệu sai, đọc thông báo lỗi và lần theo validator.

### Week 12

**Chủ đề:** pytest

**Việc thực hành:** Chạy test, cố ý đổi kết quả mong đợi rồi quan sát test fail.

### Week 13

**Chủ đề:** Module và CLI

**Việc thực hành:** Theo dõi import và điểm vào main.py.

### Week 14

**Chủ đề:** OOP

**Việc thực hành:** Tạo đối tượng Transaction và gọi phương thức to_dict.

### Week 15

**Chủ đề:** Capstone

**Việc thực hành:** Demo đầy đủ, giải thích thiết kế, test và README.


## 44. Bảo trì dự án

Khi thêm tính năng, hãy cập nhật cả code, test và README. Nếu thêm trường mới vào `Transaction`, cần kiểm tra nơi tạo đối tượng, nơi chuyển đổi dictionary, file JSON mẫu và các test liên quan.

Nếu đổi tên hàm, tìm tất cả nơi import hoặc gọi hàm đó. Sau đó chạy pytest để phát hiện chỗ chưa cập nhật.

Nếu đổi quy tắc validation, thêm test cho quy tắc mới và test cho các trường hợp trước đây hợp lệ. Điều này giảm nguy cơ làm hỏng hành vi cũ.

Nếu đổi định dạng JSON, cần xem xét khả năng đọc dữ liệu cũ. Với ứng dụng học tập, có thể hướng dẫn người dùng tạo file mới; với ứng dụng thật, cần có chiến lược migration và sao lưu.

Nên commit từng thay đổi nhỏ, ví dụ một commit cho thêm chức năng lọc theo danh mục và một commit khác cho test của chức năng đó.


## 45. Quy ước đặt tên

- Tên biến và hàm dùng `snake_case`.
- Tên lớp dùng `PascalCase`.
- Hằng số cấu hình dùng chữ hoa, ví dụ `VALID_KINDS`.
- Tên test bắt đầu bằng `test_`.
- Tên file test bắt đầu bằng `test_`.
- Tên hàm nên mô tả hành động hoặc kết quả.
- Tránh tên quá chung như `do_it`, `thing`, `x` cho logic nghiệp vụ.
- Giữ tên trường dữ liệu nhất quán trong model, JSON và test.


## 46. Bảo vệ dữ liệu

Dữ liệu mẫu trong dự án chỉ phục vụ học tập. Không nên commit giao dịch thật, số tài khoản, địa chỉ, thông tin định danh hoặc dữ liệu nhạy cảm vào repository công khai.

Nếu muốn thử nghiệm với dữ liệu cá nhân, hãy tạo một bản sao của dự án, giữ dữ liệu đó ngoài repository và thêm đường dẫn riêng vào `.gitignore`.

File JSON hiện chưa được mã hóa. Bất kỳ ai có quyền đọc file đều có thể xem nội dung. Vì vậy, không nên xem ứng dụng này là một hệ thống lưu trữ tài chính an toàn cho dữ liệu nhạy cảm.


## 47. Tiêu chí đánh giá dự án

Một bài demo tốt có thể được đánh giá qua các tiêu chí sau:

1. **Chạy được:** người khác làm theo README và khởi động thành công.
2. **Đủ chức năng:** thêm, xem, lọc, báo cáo và xóa giao dịch.
3. **Dữ liệu bền vững:** giao dịch đã lưu vẫn còn sau khi chạy lại.
4. **Xử lý dữ liệu sai:** chương trình không dừng đột ngột với các lỗi nhập phổ biến.
5. **Tổ chức code:** module có trách nhiệm rõ ràng.
6. **Kiểm thử:** test bao phủ chức năng chính và trường hợp biên.
7. **Tài liệu:** README nêu yêu cầu, cài đặt, chạy và cấu trúc.
8. **Khả năng giải thích:** người làm hiểu các hàm chính và luồng dữ liệu.
9. **Lịch sử phát triển:** Git commit có ý nghĩa và dễ theo dõi.
10. **Trung thực về giới hạn:** tài liệu nói rõ điều ứng dụng chưa hỗ trợ.

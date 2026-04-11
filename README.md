
# Hệ thống Quản lý Điểm Học sinh

## Giới thiệu
Dự án này là bài tập môn học, minh họa cho kiến trúc phân lớp (Layered Architecture) và quy trình CI/CD với GitHub Actions.

## Công nghệ sử dụng
- Python 3.11
- SQLite (database nhúng)
- Pytest cho unit test
- GitHub Actions cho CI/CD

## Cách cài đặt và chạy
1. Clone dự án: `git clone <đường-dẫn-repo>`
2. Di chuyển vào thư mục dự án: `cd student-grade-management`
3. Cài đặt thư viện: `pip install -r requirements.txt`
4. Chạy ứng dụng: `python src/main.py`

## Cách chạy test
```bash
pytest tests/ -v

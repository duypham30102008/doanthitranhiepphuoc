# Ứng dụng Điểm Danh Đoàn Viên

Đây là một ứng dụng web đơn giản giúp điểm danh Đoàn viên của các khu phố. Ứng dụng này hoạt động offline và chỉ có quản trị viên mới có quyền truy cập vào danh sách tổng hợp.

## Cách chạy ứng dụng:

1. Cài đặt các thư viện cần thiết:
    ```bash
    pip install flask pandas openpyxl
    ```

2. Chạy ứng dụng bằng lệnh:
    ```bash
    python diem_danh_doan_vien.py
    ```

3. Truy cập vào trình duyệt với đường dẫn `http://localhost:5000` để sử dụng trang điểm danh.

4. Để truy cập quản trị viên, truy cập `http://localhost:5000/admin` và đăng nhập với:
    - Username: `admin`
    - Password: `password`

## Chức năng:

- Người dùng nhập họ tên và chọn khu phố để điểm danh.
- Quản trị viên có thể xem, xóa tên Đoàn viên và tải danh sách dưới dạng file Excel.

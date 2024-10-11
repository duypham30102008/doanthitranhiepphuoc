
from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import os

app = Flask(__name__)

# File Excel để lưu trữ điểm danh
EXCEL_FILE = 'diem_danh_doan_vien.xlsx'

# Tạo file Excel nếu chưa có
if not os.path.exists(EXCEL_FILE):
    df = pd.DataFrame(columns=['Họ và tên', 'Khu phố'])
    df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

# Trang chủ cho người dùng nhập thông tin điểm danh
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ho_ten = request.form['ho_ten']
        khu_pho = request.form['khu_pho']

        # Đọc file Excel hiện tại và thêm dữ liệu mới
        df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
        # Kiểm tra xem đã điểm danh chưa (dựa trên họ tên)
        if ho_ten not in df['Họ và tên'].values:
            df = df.append({'Họ và tên': ho_ten, 'Khu phố': khu_pho}, ignore_index=True)
            df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')
        return redirect(url_for('index'))

    return render_template('index.html')

# Đăng nhập quản trị viên
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Xác thực tài khoản quản trị viên
        if username == 'admin' and password == 'password':  # Thay 'password' bằng mật khẩu của bạn
            return redirect(url_for('admin_dashboard'))
        else:
            error = 'Sai tài khoản hoặc mật khẩu'
    return render_template('login.html', error=error)

# Dashboard quản trị viên, xem và xóa danh sách
@app.route('/admin_dashboard', methods=['GET', 'POST'])
def admin_dashboard():
    df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
    if request.method == 'POST':
        if 'delete' in request.form:
            ho_ten = request.form['delete']
            df = df[df['Họ và tên'] != ho_ten]
            df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')
        elif 'download' in request.form:
            # Xuất file Excel với định dạng font Times New Roman
            writer = pd.ExcelWriter(EXCEL_FILE, engine='openpyxl')
            df.to_excel(writer, index=False)
            writer.save()
            return send_file(EXCEL_FILE, as_attachment=True)
    return render_template('admin_dashboard.html', tables=df.values)

if __name__ == '__main__':
    app.run(debug=True)

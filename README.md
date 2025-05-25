---
title: PDF Splitter by Size
emoji: 📄
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 5.31.0
app_file: app.py
license: mit
pinned: false
---
# 📦 PDF Splitter by Size - Gradio App

Tách một file PDF thành nhiều phần nhỏ hơn, với mỗi phần có dung lượng không vượt quá giới hạn do bạn chọn. Ứng dụng chạy trực tiếp trên nền tảng [Gradio](https://www.gradio.app/), dễ sử dụng và không cần cài đặt phần mềm phức tạp.

---

## 🚀 Tính năng nổi bật

- 📁 Tải lên file PDF bất kỳ
- ✂️ Tách file thành nhiều phần nhỏ theo giới hạn dung lượng (tính bằng MB)
- 📤 Tải về toàn bộ các phần đã tách
- ⚡ Giao diện đơn giản, trực quan
- 🛡️ Hoạt động toàn bộ trên trình duyệt — không lưu trữ dữ liệu người dùng

---

## 🧠 Cách hoạt động

1. Người dùng tải lên file PDF
2. Ứng dụng tính toán dung lượng từng trang khi thêm vào
3. Khi gần vượt quá giới hạn, ứng dụng dừng và tạo một phần PDF mới
4. Quá trình lặp lại cho đến khi xử lý hết toàn bộ tài liệu

---

## 🛠 Cài đặt thủ công (tuỳ chọn)

```bash
git clone https://github.com/hoangthuan-dev/PDF-Splitter-by-Size
cd pdf-splitter
pip install -r requirements.txt
python app.py
```

---

## 📦 Triển khai trên Hugging Face Spaces

Đây là ứng dụng Gradio nên bạn chỉ cần upload các file sau:

```
├── app.py
├── requirements.txt
└── README.md
```

> Hugging Face sẽ tự động nhận diện đây là ứng dụng Gradio và triển khai ngay.

---

## 📬 Liên hệ tác giả

- 👨‍💻 **Tên:** Hoàng Thuận DEV  
- 🌐 **Website:** [https://hoangthuan.dev](https://hoangthuan.dev)  
- 📧 **Email:** huggingface@hoangthuan.dev  
- 🐙 **GitHub:** [https://github.com/hoangthuan-dev](https://github.com/hoangthuan-dev)

---

## 📜 Giấy phép

Dự án này sử dụng giấy phép [MIT License](https://opensource.org/licenses/MIT) — bạn có thể tự do chỉnh sửa và phân phối.

---

## 💡 Gợi ý

Nếu bạn thấy dự án hữu ích, hãy ⭐ star repo trên GitHub hoặc chia sẻ cho cộng đồng. Mọi đóng góp đều được chào đón!
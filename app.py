import gradio as gr
from PyPDF2 import PdfReader, PdfWriter
import os
import tempfile
import shutil
from datetime import datetime

# Tạo thư mục output tạm
OUTPUT_DIR = "gradio_outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def split_pdf_by_size_gradio(pdf_file, max_size_mb):
    # Tạo thư mục tạm để xử lý PDF
    with tempfile.TemporaryDirectory() as tmpdir:
        # Ghi file PDF đầu vào
        input_path = os.path.join(tmpdir, "input.pdf")
        with open(input_path, "wb") as f:
            f.write(pdf_file)

        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        part = 1
        page_start = 0
        output_files = []

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        output_subdir = os.path.join(OUTPUT_DIR, f"session_{timestamp}")
        os.makedirs(output_subdir, exist_ok=True)

        while page_start < total_pages:
            temp_writer = PdfWriter()
            temp_pages = []
            page_end = page_start

            while page_end < total_pages:
                temp_pages.append(reader.pages[page_end])
                temp_writer.add_page(reader.pages[page_end])

                temp_path = os.path.join(tmpdir, "temp_test.pdf")
                with open(temp_path, "wb") as temp_file:
                    temp_writer.write(temp_file)

                file_size_mb = os.path.getsize(temp_path) / (1024 * 1024)
                if file_size_mb > max_size_mb:
                    temp_pages.pop()
                    break
                page_end += 1

            writer = PdfWriter()
            for page in temp_pages:
                writer.add_page(page)

            # Lưu file kết quả sang thư mục output cố định
            output_path = os.path.join(output_subdir, f"part_{part}.pdf")
            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            output_files.append(output_path)
            part += 1
            page_start += len(temp_pages)

        return output_files

# Giao diện Gradio
with gr.Blocks() as demo:
    gr.Markdown("## 📄 Tách PDF thành nhiều file theo dung lượng")

    with gr.Row():
        pdf_input = gr.File(label="Tải lên file PDF", file_types=[".pdf"], type="binary")
        size_input = gr.Slider(1, 50, value=10, label="Giới hạn dung lượng mỗi file (MB)")

    output = gr.File(label="Các phần đã tách", file_types=[".pdf"], file_count="multiple")

    btn = gr.Button("🚀 Tách file PDF")
    btn.click(fn=split_pdf_by_size_gradio, inputs=[pdf_input, size_input], outputs=output)

demo.launch()

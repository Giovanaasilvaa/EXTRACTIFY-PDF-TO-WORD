<h1 align="center">📄 EXTRACTIFY - PDF TO WORD (PYTHON & FLASK)</h1>

<p align="center"><em>Convert PDFs to Word files quickly, simply, and automatically</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/last%20commit-june-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/python-26.7%25-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/technologies-4-blue?style=flat-square" />
</p>

<h3 align="center">Technologies and Tools Used:</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
</p>

---

## 📋 About the Project

**Extractify** is a web application developed with **Python (Flask)** that allows the user to **upload a PDF file** and **automatically convert the content to a Word (.docx) file**.

This tool performs **text extraction from PDF documents** using the **pdfplumber** library and **Word file generation** with the **python-docx** library.

> ⚠️ *The system only performs simple text extraction. More complex layouts, such as tables or images, may not be preserved.*

---

## 🧠 Features

✅ Upload PDF files via drag & drop or button. <br>
✅ Automatic text extraction from PDF. <br>
✅ Instant generation and download of Word file (.docx). <br>
✅ Progress feedback (status message). <br>
✅ Lightweight and responsive web interface.

---

## 🛠 Estrutura do Projeto

<pre>
/app.py → Flask backend responsible for routes and conversion logic
/assets → Static files such as HTML, CSS, JS and videos
/assets/css → Visual style of the page
/assets/js → JavaScript interaction scripts (upload, drag & drop, etc.)
/assets/videos → Demo video displayed on the page
</pre>

---

## 🚀 How to Run the Project

1. **Clone this repository**

2. **Create and activate a virtual environment (optional, but recommended):**

3. **Install dependencies:**

```bash
pip install flask flask_cors pdfplumber python-docx
```

4. **Run the Flask server:**

```bash
python app.py
```

5. **Access in browser:**

```
http://localhost:5000
```

---

## 📂 Usage Example

✅ Upload a PDF file <br>
✅ The system will process <br>
✅ The Word download will start automatically

---

## ⚠️ Limitations

- Does not maintain layout formatting (only plain text) <br>
- Very large PDF files may take longer

---

## 📦 Version

1.0.0

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

Giovana Marques Silva  
giovanamarquessilva24@gmail.com

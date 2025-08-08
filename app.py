import webbrowser
from threading import Timer
from flask import Flask, request, send_file, send_from_directory, make_response
from flask_cors import CORS
import pdfplumber
from docx import Document
import io
import os

app = Flask(__name__, static_folder='assets')
CORS(app)


os.makedirs('upload', exist_ok=True)

# Main route: serve the index.html file
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Upload and convert PDF to Word (.docx)
@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Check if PDF file was sent
    if 'pdf' not in request.files:
        return "PDF file not uploaded.", 400

    pdf_file = request.files['pdf']
    output_path = os.path.join('upload', 'saida.docx')

    try:
        full_text = ""
        # Open PDF using pdfplumber and extract text from all pages
        with pdfplumber.open(pdf_file.stream) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
        
        # Create a Word document and add the extracted text
        doc = Document()
        doc.add_paragraph(full_text)
        doc.save(output_path)

        # Send the Word document as a downloadable file response
        response = make_response(send_file(
            output_path,
            as_attachment=True,
            download_name='saida.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ))

        # Ensure the temporary file is deleted after sending
        response.call_on_close(lambda: os.remove(output_path))
        return response

    except Exception as e:
        # Handle exceptions and return error message
        return f"Error processing PDF: {str(e)}", 500

# Route to serve static files
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Route to serve CSS files
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(app.static_folder, 'css'), filename)

# Route to serve JS files 
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.static_folder, 'js'), filename)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    # Automatically open the browser after 1 second and run the app
    Timer(1, lambda: webbrowser.open('http://127.0.0.1:5000/')).start()
    app.run(debug=False, use_reloader=False)

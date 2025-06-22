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

        # Save the Word document physically in the /upload folder
        output_path = os.path.join('upload', 'saida.docx')
        doc.save(output_path)

        # Load the saved Word document into memory
        with open(output_path, 'rb') as f:
            doc_stream = io.BytesIO(f.read())
            doc_stream.seek(0)

        # Send the Word document as a downloadable file response
        response = make_response(send_file(
            doc_stream,
            as_attachment=True,
            download_name='saida.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ))

        return response

    except Exception as e:
        # Handle exceptions and return error message
        return f"Error processing PDF: {str(e)}", 500

# Route to serve static files from the assets folder
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Route to serve CSS files if there is a css folder inside assets
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(app.static_folder, 'css'), filename)

# Route to serve JS files if there is a js folder inside assets
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.static_folder, 'js'), filename)

# Optional: Route for favicon (if you want to add later)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    # Automatically open the browser after 1 second and run the app
    Timer(1, lambda: webbrowser.open('http://127.0.0.1:5000/')).start()
    app.run()

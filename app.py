from flask import Flask, request, send_file, send_from_directory, make_response
from flask_cors import CORS
import pdfplumber
from docx import Document
import io
import os

app = Flask(__name__, static_folder='assets')
CORS(app)

# Rota principal: carrega o index.html
@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Upload e conversão do PDF para Word (.docx)
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return "Arquivo PDF não enviado.", 400

    pdf_file = request.files['pdf']

    try:
        texto_completo = ""
        with pdfplumber.open(pdf_file.stream) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_completo += texto + "\n"
        
        # Criar documento Word
        doc = Document()
        doc.add_paragraph(texto_completo)

        # Salvar o Word fisicamente na pasta /upload
        output_path = os.path.join('upload', 'saida.docx')
        doc.save(output_path)

        # Salvar o Word em memória
        with open(output_path, 'rb') as f:
            doc_stream = io.BytesIO(f.read())
            doc_stream.seek(0)

        # Enviar como download
        response = make_response(send_file(
            doc_stream,
            as_attachment=True,
            download_name='saida.docx',
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ))

        return response

    except Exception as e:
        return f"Erro ao processar o PDF: {str(e)}", 500

# Rota para servir arquivos estáticos da pasta assets
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Rota para CSS (se tiver pasta css dentro de assets)
@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory(os.path.join(app.static_folder, 'css'), filename)

# Rota para JS (se tiver pasta js dentro de assets)
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory(os.path.join(app.static_folder, 'js'), filename)

# Opcional: Rota pro favicon (se quiser criar depois)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, jsonify, send_from_directory
from app import app
from app.models import save_user_data
from app.services.ai_service import generate_latex
from app.services.latex_service import compile_latex

@app.route('/submit', methods=['POST'])
def submit_data():
    user_data = request.json
    user_id = save_user_data(user_data)
    latex_code = generate_latex(user_data)
    pdf_path = compile_latex(latex_code)
    return jsonify({'user_id': str(user_id), 'pdf_path': pdf_path})

@app.route('/download/<path:pdf_path>', methods=['GET'])
def download_pdf(pdf_path):
    return send_from_directory(directory='/tmp', path=pdf_path)

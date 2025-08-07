A comprehensive system for extracting structured data from medical documents using OCR (Optical Character Recognition) and natural language processing techniques. This project can parse prescription documents and patient detail forms to extract relevant medical information.

## 🏥 Features

- **Document Processing**: Extract text from PDF medical documents using OCR
- **Prescription Parsing**: Extract patient information, medications, directions, and refill details from prescription documents
- **Patient Details Parsing**: Extract patient information, contact details, medical problems, and vaccination history
- **RESTful API**: FastAPI-based web service for document processing
- **Image Preprocessing**: Advanced image processing techniques to improve OCR accuracy
- **Modular Architecture**: Separate parsers for different document types

## 📋 Supported Document Types

1. **Prescription Documents**
   - Patient name and address
   - Medication list
   - Dosage directions
   - Refill information

2. **Patient Details Forms**
   - Patient name and contact information
   - Medical problems and conditions
   - Hepatitis B vaccination status
   - Emergency contact details

## 🛠️ Technology Stack

- **Backend**: Python, FastAPI
- **OCR**: Tesseract OCR, pdf2image
- **Image Processing**: OpenCV, PIL
- **Data Processing**: NumPy, Pandas
- **Testing**: pytest

## 📦 Installation

### Prerequisites

1. **Python 3.7+**
2. **Tesseract OCR**
   - **Windows**: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - **macOS**: `brew install tesseract`
   - **Linux**: `sudo apt-get install tesseract-ocr`

3. **Poppler** (for PDF processing)
   - **Windows**: Download from [poppler releases](http://blog.alivate.com.au/poppler-windows/)
   - **macOS**: `brew install poppler`
   - **Linux**: `sudo apt-get install poppler-utils`

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd 4_project_medical_data_extraction
   ```

2. **Install Python dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Configure paths** (if needed)
   
   Update the paths in `backend/src/extractor.py`:
   ```python
   POPPLER_PATH = r'C:\poppler-21.02.0\Library\bin'  # Update for your system
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update for your system
   ```

## 🚀 Usage

### Running the API Server

1. **Start the FastAPI server**
   ```bash
   cd backend/src
   python main.py
   ```

2. **Access the API**
   - Server runs on: `http://127.0.0.1:8000`
   - API documentation: `http://127.0.0.1:8000/docs`

### API Endpoints

#### POST `/extract_from_doc`

Extract data from uploaded medical documents.

**Parameters:**
- `file_format` (string): Document type - either "prescription" or "patient_details"
- `file` (file): PDF file to process

**Example Request:**
```bash
curl -X POST "http://127.0.0.1:8000/extract_from_doc" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file_format=prescription" \
     -F "file=@path/to/prescription.pdf"
```

**Response Format:**
```json
{
  "patient_name": "Marta Sharapova",
  "patient_address": "9 tennis court, new Russia, DC",
  "medicines": "Prednisone 20 mg\nLialda 2.4 gram",
  "directions": "Prednisone, Taper 5 mg every 3 days...",
  "refills": "3"
}
```

### Direct Python Usage

```python
from backend.src.extractor import extract

# Extract prescription data
prescription_data = extract('path/to/prescription.pdf', 'prescription')
print(prescription_data)

# Extract patient details
patient_data = extract('path/to/patient_details.pdf', 'patient_details')
print(patient_data)
```

## 🧪 Testing

Run the test suite:

```bash
cd backend
pytest tests/
```

## 📁 Project Structure

```
4_project_medical_data_extraction/
├── backend/
│   ├── src/
│   │   ├── extractor.py          # Main extraction logic
│   │   ├── main.py               # FastAPI application
│   │   ├── parser_generic.py     # Base parser class
│   │   ├── parser_prescription.py # Prescription document parser
│   │   ├── parser_patient_details.py # Patient details parser
│   │   └── util.py               # Image preprocessing utilities
│   ├── tests/                    # Test files
│   ├── notebooks/                # Jupyter notebooks for development
│   ├── resources/                # Sample documents
│   ├── uploads/                  # Temporary file storage
│   └── requirements.txt          # Python dependencies
└── frontend/                     # Frontend application (to be implemented)
```

## 🔧 Configuration

### Environment Variables

The following paths can be configured in `backend/src/extractor.py`:

- `POPPLER_PATH`: Path to Poppler binaries
- `TESSERACT_CMD`: Path to Tesseract executable

### Image Processing Settings

Image preprocessing parameters can be adjusted in `backend/src/util.py`:

- Resize factor: `fx=1.5, fy=1.5`
- Adaptive threshold parameters: `blockSize=61, C=11`

## 📊 Sample Data

The project includes sample documents in `backend/resources/`:

- **Prescriptions**: `prescription/pre_1.pdf`, `prescription/pre_2.pdf`
- **Patient Details**: `patient_details/pd_1.pdf`, `patient_details/pd_2.pdf`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes

- Ensure Tesseract OCR and Poppler are properly installed and configured
- The system is designed for English language documents
- Image quality significantly affects OCR accuracy
- Always validate extracted data for medical applications

## 🆘 Troubleshooting

### Common Issues

1. **Tesseract not found**: Update the `tesseract_cmd` path in `extractor.py`
2. **Poppler not found**: Update the `POPPLER_PATH` in `extractor.py`
3. **Poor OCR results**: Check image quality and preprocessing parameters
4. **Import errors**: Ensure all dependencies are installed from `requirements.txt`

### Getting Help

- Check the API documentation at `http://127.0.0.1:8000/docs`
- Review the sample notebooks in `backend/notebooks/`
- Run tests to verify installation: `pytest tests/`

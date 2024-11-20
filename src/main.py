from fastapi import FastAPI, File, UploadFile, HTTPException
import fitz  # PyMuPDF
from io import BytesIO

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the PDF Text Extractor API!"}

@app.post("/extract-text/")
async def extract_text_from_pdf(file: UploadFile = File(...)):
    """
    Endpoint to upload a PDF file and extract text from it using PyMuPDF.
    """
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        # Read the uploaded PDF file
        file_content = await file.read()
        pdf_document = fitz.open(stream=BytesIO(file_content), filetype="pdf")

        # Extract text from all pages
        extracted_text = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            extracted_text += page.get_text()

        pdf_document.close()

        return {"filename": file.filename, "text": extracted_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the PDF: {str(e)}")

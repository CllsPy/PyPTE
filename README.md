# **PDF Text Extractor API Documentation**

## **Overview**
The **PDF Text Extractor API** allows users to upload PDF files and receive the extracted text from those files. This API is built using FastAPI and leverages the PyMuPDF library for efficient text extraction.

### **Base URL**
```
http://127.0.0.1:8000
```

---

## **Endpoints**

### **1. Root Endpoint**
**URL:** `/`  
**Method:** `GET`  

#### **Description:**
Returns a welcome message indicating that the API is running.

#### **Example Response:**
```json
{
    "message": "Welcome to the PDF Text Extractor API!"
}
```

---

### **2. Extract Text from PDF**
**URL:** `/extract-text/`  
**Method:** `POST`  

#### **Description:**
Accepts a PDF file as input and returns the extracted text.

#### **Request Parameters:**
- **file** (required): A PDF file to extract text from.  
  - Type: `File`
  - Format: PDF file (`.pdf`)

#### **Example Request (Swagger UI):**
1. Navigate to `http://127.0.0.1:8000/docs`.
2. Open the `/extract-text/` endpoint.
3. Click **Try it out**.
4. Upload a PDF file using the file input.
5. Click **Execute** to process the file.

#### **Example Request (`curl`):**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/extract-text/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@example.pdf'
```

#### **Response:**
- **200 OK**: Text extracted successfully.
- **400 Bad Request**: Invalid file type (e.g., not a PDF).
- **500 Internal Server Error**: Issue with PDF processing.

#### **Example Response:**
```json
{
    "filename": "example.pdf",
    "text": "This is the extracted text from the PDF."
}
```

---

## **How to Run the API**

### **1. Prerequisites**
Ensure you have Python 3.7+ installed. Install the required libraries:
```bash
pip install fastapi uvicorn pymupdf python-multipart
```

### **2. Running the Application**
Save the API code in a file called `main.py`, then run the following command:
```bash
uvicorn main:app --reload
```

### **3. Access the API**
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Testing the API**

### **1. Using Swagger UI**
1. Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
2. Select the `/extract-text/` endpoint.
3. Click **Try it out**.
4. Upload a PDF file.
5. Click **Execute** to see the extracted text in the response.

### **2. Using `curl`**
Test the `/extract-text/` endpoint using the command line:
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/extract-text/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path_to_your_pdf.pdf'
```

### **3. Using Postman**
1. Set the request type to `POST` and the URL to `http://127.0.0.1:8000/extract-text/`.
2. Under the **Body** tab, select `form-data`.
3. Add a key named `file` with type set to `File`.
4. Upload the PDF file and click **Send**.

---

## **Error Handling**

| **Error Code** | **Description**                                  |
|----------------|--------------------------------------------------|
| `400`          | Invalid file type. Only PDF files are supported. |
| `500`          | An error occurred while processing the PDF file. |

---

## **Example Use Cases**
- Extract text from invoices, academic papers, or legal documents.
- Process multiple PDF files for text mining or analysis.
- Integrate into document management systems for automated text extraction.

---

Let me know if you'd like me to enhance the documentation further! 🚀

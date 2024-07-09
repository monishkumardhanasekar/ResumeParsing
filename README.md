# Resume Parsing Project using Django Framework

Welcome to the Resume Parsing Project! This project provides a web application for parsing resume files in `.pdf`, `.txt`, and `.docx` formats. The parsed data is stored in MongoDB and Amazon S3, and the extracted information is displayed on the web page for easy review.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

This project allows users to upload resume files in various formats. The application extracts relevant data from the resumes and stores it in MongoDB for structured storage and Amazon S3 for file storage. The parsed data is then displayed on a webpage for users to view.

The application supports:
- Uploading resumes in `.pdf`, `.txt`, and `.docx` formats.
- Parsing the uploaded files to extract resume data.
- Storing resume files in Amazon S3 and metadata in MongoDB.
- Displaying extracted resume information on the web page.

**Upload your resume files here:** [Upload Resume](http://127.0.0.1:8000/resumes/upload/)

## Features

- **File Upload:** Users can upload `.pdf`, `.txt`, and `.docx` files.
- **Resume Parsing:** Extracts information such as name, contact details, and work experience.
- **Data Storage:** Stores files in Amazon S3 and metadata in MongoDB.
- **Data Display:** Shows parsed resume data on the web page.

## Technologies Used

- **Django Framework:** Web framework for developing the application.
- **Django REST Framework:** For building the API endpoints.
- **MongoDB:** NoSQL database for storing resume metadata.
- **Amazon S3:** Cloud storage for storing resume files.
- **OpenAI API:** For advanced resume parsing (optional, depending on implementation).
- **Python Libraries:**
  - **`fitz` (PyMuPDF):** For parsing `.pdf` files.
  - **`python-docx`:** For parsing `.docx` files.
  - **`utf-8` Encoding:** For handling `.txt` file content.

## Getting Started

To get started with the Resume Parsing Project, follow these instructions:

### Prerequisites

- **Python 3.x**: Ensure you have Python 3.x installed.
- **Pip**: Python package installer.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone git@github.com:monishkumardhanasekar/ResumeParsing.git
   cd resume-parsing-project
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables:**

   Create a `.env` file in the project root directory and add the following variables:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   MONGODB_URI=your_mongodb_connection_string
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   AWS_STORAGE_BUCKET_NAME=your_s3_bucket_name
   AWS_S3_CUSTOM_DOMAIN=your_s3_custom_domain
   ```

6. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/resumes/upload/`.

## Usage

1. **Upload a Resume:**

   - Navigate to [http://127.0.0.1:8000/resumes/upload/](http://127.0.0.1:8000/resumes/upload/)
   - Choose a `.pdf`, `.txt`, or `.docx` file and click "Upload."

2. **View Parsed Data:**

   - After uploading, the extracted resume data will be displayed on the page.

## API Endpoints

- **POST /resumes/upload/**

  Upload a resume file and get the parsed data.

  **Request:**
  ```http
  POST /resumes/upload/
  ```

  **Form Data:**
  - `file`: The resume file (must be `.pdf`, `.txt`, or `.docx`).

  **Response:**
  - `200 OK`: Returns the parsed resume data.

## Contributing

We welcome contributions to improve the Resume Parsing Project. To contribute:

1. **Fork the Repository**
2. **Create a New Branch**
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Make Changes**
4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add new feature"
   ```
5. **Push to Your Fork**
   ```bash
   git push origin feature/new-feature
   ```
6. **Create a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me:

- **Name:** Monish Kumar Dhanasekar
- **Email:** monishkumard1712@gmail.com
- **GitHub:** [yourusername](https://github.com/monishkumardhanasekar)

---

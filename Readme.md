# Flask Application README

## Prerequisites
Before running this Flask application, ensure you have the following installed on your system:
- Python (3.x recommended)
- pip (Python package installer)
- virtualenv (for creating isolated Python environments)

## Setup Instructions

### For Windows

1. **Install virtualenv (if not installed)**:
   Open Command Prompt and run:
   ```bash
   pip install virtualenv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/ManasMadan/c4gt-website.git
   cd c4gt-website
   ```

3. **Create a new virtual environment**:
   ```bash
   venv env
   ```

4. **Activate the virtual environment**:
   ```bash
   .\env\Scripts\activate
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Configure environment variables**:
   Create a `.env` file in the root directory of the project and add the required variables. You can use the provided `.env.example` file as a reference:
   ```bash
   cp .env.example .env
   ```

7. **Run the application**:
   ```bash
   python main.py
   ```

8. Access the application in your web browser at `http://127.0.0.1:5000`.

### For Mac/Linux

1. **Install virtualenv (if not installed)**:
   Open Terminal and run:
   ```bash
   pip3 install virtualenv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/ManasMadan/c4gt-website.git
   cd c4gt-website
   ```

3. **Create a new virtual environment**:
   ```bash
   python3 -m venv env
   ```

4. **Activate the virtual environment**:
   ```bash
   source env/bin/activate
   ```

5. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Configure environment variables**:
   Create a `.env` file in the root directory of the project and add the required variables. You can use the provided `.env.example` file as a reference:
   ```bash
   cp .env.example .env
   ```

7. **Run the application**:
   ```bash
   python3 main.py
   ```

8. Access the application in your web browser at `http://127.0.0.1:5000`.

## Additional Notes

- If you encounter any issues during installation or execution, please refer to the official documentation for [Flask](https://flask.palletsprojects.com/) and ensure all prerequisites are correctly installed.

- Customize `main.py`, `requirements.txt`, and `.env` as per your application's specific requirements.
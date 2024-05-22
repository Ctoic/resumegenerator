# Flask Resume Builder

Flask Resume Builder is a simple web application that allows users to create professional resumes using LaTeX templates. The application collects necessary information from users, generates LaTeX code for the resume, and compiles it into a downloadable PDF.

## Features

- Easy-to-use interface for creating resumes.
- Integration with MongoDB for storing user data.
- Utilizes OpenAI API for generating LaTeX code.
- Customizable LaTeX templates for professional-looking resumes.

## Requirements

- Python 3
- Flask
- Flask-PyMongo
- python-dotenv

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/flask-resume-builder.git
    cd flask-resume-builder
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and set environment variables:

    ```plaintext
    SECRET_KEY=your_secret_key
    MONGO_URI=mongodb://localhost:27017/your_database_name
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Run the Flask application:

    ```bash
    python run.py
    ```

## Usage

1. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).
2. Fill out the resume form with your information.
3. Submit the form to generate and download your professional resume.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

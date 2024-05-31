# Automated Google Form Filler

This project is a Python script that automates the process of filling out a Google Form using Selenium WebDriver.

## Prerequisites

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your version of Google Chrome)
- `selenium` library
- `python-dotenv` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the project directory and add the following environment variables:

   ```plaintext
   NAME=your_name
   NUMBER=your_phone_number
   EMAIL=your_email
   ADDRESS=your_address
   PINCODE=your_pincode
   DOBDATE=your_date_of_birth_day
   DOBMONTH=your_date_of_birth_month
   DOBYEAR=your_date_of_birth_year
   GENDER=your_gender
   ```

## Usage

1. **Ensure ChromeDriver is in your PATH or specify its location:**

   ```python
   chrome_options = webdriver.ChromeOptions()
   chrome_options.add_experimental_option("detach", True)
   driver = webdriver.Chrome(options=chrome_options, executable_path='/path/to/chromedriver')
   ```

2. **Run the script:**

   ```bash
   python main.py
   ```

   The script will open the specified Google Form, fill in the details using the values from the `.env` file, and submit the form.

## Note

- Ensure that the XPaths used in the script match the actual XPaths of the form fields in the Google Form. If the form structure changes, you may need to update the XPaths accordingly.

## Output of our code
![Screenshot 2024-05-31 154712.png](Screenshot%202024-05-31%20154712.png))
## Acknowledgments

- [Selenium](https://www.selenium.dev/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)


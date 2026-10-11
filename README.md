# Stock Portfolio Tracker

A web-based stock portfolio management application built with **Python, Flask, and MySQL**. The application allows users to create accounts, log in, manage their stock holdings, and monitor portfolio performance through profit and loss calculations.

## Features

- **User Authentication** — Account registration and login functionality.
- **Portfolio Management** — Add, view, and delete stock holdings.
- **MySQL Database** — Store user accounts and portfolio information.
- **Portfolio Performance** — Calculate total money invested, current portfolio value, and overall profit or loss.
- **Stock Price Integration** — Retrieve stock information and market prices through an external stock API.
- **Web Interface** — HTML templates and CSS styling for a user-friendly dashboard.
- **Password Security** — Password hashing using Werkzeug, if enabled in the current version.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web framework and routing |
| MySQL | Database management |
| HTML | Web page structure |
| CSS | User interface styling |
| Werkzeug | Password hashing and verification |
| Python dotenv | Environment variable management |
| Stock Market API | Retrieve stock market data |

## Project Structure

```text
stockportfoliotracker/
├── app.py
├── main.py
├── database.py
├── stock_api.py
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── main.html
│   └── create_user.html
├── static/
│   └── style.css
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

*Note: Adjust the file names above to match the actual structure of your project.*

## Getting Started

### 1. Prerequisites

Install the following before running the application:

- Python 3
- MySQL Server
- pip (Python package manager)

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd stockportfoliotracker
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your GitHub repository.

### 3. Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and configure your database connection:

```dotenv
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
```

Replace the example values with your own MySQL configuration. Ensure that the application loads these environment variables using `python-dotenv`.

**Security:** Never commit your `.env` file, database credentials, or API keys to GitHub.

### 5. Set Up the Database

Create the required MySQL database and tables according to the schema used in `database.py`.

Ensure your MySQL server is running and the configured credentials have the necessary database permissions.

### 6. Run the Application

```bash
python3 app.py
```

Open the local address displayed in your terminal, typically:

```text
http://127.0.0.1:5000
```

## Security

- Keep database credentials in environment variables rather than hardcoding them in source files.
- Exclude `.env`, virtual environments, and other sensitive files through `.gitignore`.
- Use Werkzeug password hashing and verification for user passwords.
- Avoid committing API keys or personal information to the repository.

## Future Improvements

- Interactive charts showing individual stock performance.
- Improved stock market data integration.
- Enhanced input validation and error handling.
- Automated testing for database operations and authentication.
- Improved dashboard responsiveness and user experience.

## Author

**Mohamed Anees Odayapurath**

BEng Computer Science  
The University of Hong Kong

---


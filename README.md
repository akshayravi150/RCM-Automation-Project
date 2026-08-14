# RCM Automation Project

A Python-based RCM (Revenue Cycle Management) automation project that combines a Flask web interface with Selenium-based workflow automation for charge entry processing.

## Overview
This project demonstrates a practical healthcare automation workflow where:
- a web login screen is served via Flask
- a charge entry form captures patient billing details
- automation logic can process charge data from Excel files
- processing results are written back to the spreadsheet

## Features
- Flask login and charge entry interface
- SQLite database support for RCM data
- Excel-driven charge processing workflow
- Selenium browser automation foundation
- Logging and error handling for automation tasks
- Recruiter-friendly project structure and documentation

## Tech Stack
- Python 3.12
- Flask
- Selenium
- Pandas + OpenPyXL
- SQLite
- WebDriver Manager

## Project Structure
```text
RCM_Automation_Project/
├── app.py                      # Flask app entry point
├── main.py                     # Bot execution entry point
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore rules
├── automation/                 # Selenium and automation modules
│   ├── browser_service.py
│   ├── login_bot.py
│   ├── rcm_processor.py
│   └── util/
├── config/                     # Project config and settings
│   ├── config_dev.json
│   └── settings.py
├── database/                   # Database helpers
│   └── db_connection.py
├── data/                       # Demo Excel files
├── db/                         # SQLite database files
├── logs/                       # Automation logs
├── services/                   # Application processing services
│   ├── logger.py
│   ├── screenshot_service.py
│   └── ui_charge_processor.py
├── templates/                  # Flask HTML templates
│   ├── login.html
│   ├── charge_entry.html
│   └── index.html
├── tests/                      # Test files
├── utils/                      # Shared utilities
│   ├── custom_exceptions.py
│   └── logger.py
└── venv/                       # Local virtual environment (ignored in git)
```

## Setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate it:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run the App
```bash
python app.py
```
Then open:
```text
http://127.0.0.1:5000/login
```

## Run the Automation Flow
```bash
python main.py
```

## Notes
- This project is designed to showcase automation and process logic for RCM workflows.
- It can be extended with real login credentials, production APIs, and more robust end-to-end automation flows.

## License
This project is for portfolio and learning purposes.

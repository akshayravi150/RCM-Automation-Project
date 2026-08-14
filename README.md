# RCM Automation Project

A Python-based automation portfolio project focused on Revenue Cycle Management (RCM) workflows, combining Flask web interfaces with Selenium automation to streamline charge entry and billing operations.

## Project Overview
This project demonstrates how automation can reduce manual effort in healthcare billing workflows by:
- serving a login and charge-entry interface through Flask
- processing billing data from Excel files
- automating browser-based actions with Selenium
- logging progress and failures for operational visibility
- providing a clean automation workflow that is easy to explain in interviews and portfolio reviews

## Why This Project Matters
In healthcare organizations, repetitive billing and charge entry tasks can consume hours of manual effort. This project simulates a practical automation workflow that helps improve speed, consistency, and data tracking in RCM operations.

## Key Features
- Flask-based UI for login and charge entry pages
- Excel-driven charge processing workflow
- Selenium-based browser automation foundation
- SQLite database integration setup for RCM data storage
- Logging and error tracking for automation monitoring
- Clean, recruiter-friendly project structure for portfolio presentation

## Tech Stack
- Python
- Flask
- Selenium
- Pandas
- OpenPyXL
- SQLite
- WebDriver Manager

## Workflow
```text
Excel Data -> Python Processing -> Selenium Automation -> Charge Submission -> Status Update
```

The project reads billing data, processes each record, updates result status, and logs outcomes for review.

## Project Structure
```text
RCM_Automation_Project/
├── app.py                      # Flask application entry point
├── main.py                     # Main automation runner
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── automation/
│   ├── browser_service.py
│   ├── login_bot.py
│   └── rcm_processor.py
├── config/
│   ├── config_dev.json
│   └── settings.py
├── database/
│   └── db_connection.py
├── data/
│   └── Excel files for automation demo
├── db/
│   └── SQLite database files
├── logs/
│   └── Runtime and error logs
├── services/
│   ├── logger.py
│   ├── screenshot_service.py
│   └── ui_charge_processor.py
├── templates/
│   ├── login.html
│   ├── charge_entry.html
│   └── index.html
├── tests/
│   └── Test files
├── utils/
│   ├── custom_exceptions.py
│   └── logger.py
└── venv/                      # Local environment (ignored by Git)
```

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
   ```bash
   python -m venv venv
   ```
3. Activate the environment
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application
```bash
python app.py
```
Then open:
```text
http://127.0.0.1:5000/dashboard
```

## Run the Automation Flow
```bash
python main.py
```

## Automation Use Case
This project is designed to simulate a real-world healthcare admin workflow where staff handle charge entry, validation, and status updates. The automation layer is structured to process bulk records and reduce repetitive manual actions.

## Portfolio Highlights
- Built a full-stack Python automation demo with UI + backend logic
- Applied Selenium for browser automation testing and workflow simulation
- Worked with data processing using Excel and pandas
- Integrated logging, error handling, and modular project architecture
- Designed the repository to look professional and recruiter-friendly

## Notes
This project is intended for portfolio and learning purposes. It can be extended with real authentication, API integrations, production-grade validations, and more advanced RCM workflows.

## License
This project is for demonstration and portfolio use.

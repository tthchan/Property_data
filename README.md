**Project Overview**
This project is designed to automatically scrape property data from Centanet, a prominent real estate listing website in Hong Kong. Utilizing Python with Selenium and BeautifulSoup, this repository contains two versions of the script: main.py for basic scraping and main_v2.py for a more advanced approach.

Features
Automated Scraping: Runs daily to fetch the latest property sale and lease data.
GitHub Actions: Orchestrated with a YAML file to run the scraping script on a schedule.
Data Extraction: Gathers information on property sales and leases, storing it in Excel format.
Scripts
main.py: A straightforward script using Selenium and BeautifulSoup to scrape and process data.
main_v2.py: An advanced version implementing additional data processing and error handling techniques.
GitHub Actions Workflow
The .github/workflows/web_scraping_v2.yml file defines the GitHub Actions workflow to automate the execution of main_v2.py script. The workflow is scheduled to run every day at 19:00 UTC.

Workflow Steps:
Setup: Initializes the environment with Chrome and Python.
Script Execution: Runs main_v2.py, followed by storing the results in 中原放盤.xlsx.
Auto-push to GitHub: Commits and pushes the updated Excel file to the repository.
Setup and Usage
Clone the repository:
bash
Copy code
git clone [repository-url]
Install dependencies:
Copy code
pip install -r requirements.txt
Run the script:
For the simple version: python3 main.py
For the advanced version: python3 main_v2.py
Dependencies
Selenium
BeautifulSoup
Pandas
Chrome WebDriver

# Automated Web Scraping for Property Data

## Project Overview
This project is designed to automatically scrape property data from Centaline Property Hong Kong. Utilizing Python with Selenium and BeautifulSoup, this repository contains two versions of the script: main.py for basic scraping and main_v2.py for a more advanced approach.

## Features
* Automated Scraping: Runs daily to fetch the latest property sale and lease data.
* GitHub Actions: Orchestrated with a YAML file to run the scraping script on a schedule.
* Data Extraction: Gathers information on property sales and leases, storing it in Excel format.

## Scripts
1. main.py: A straightforward script using Selenium and BeautifulSoup to scrape and process data.
1. main_v2.py: An advanced version implementing additional data processing and error handling techniques.

## GitHub Actions Workflow
The web_scraping.yml and web_scraping_v2.yml files define the GitHub Actions workflow to automate the execution of main.py and main_v2.py scripts. The workflow is scheduled to run every day at 19:00 UTC.

## Workflow Steps:
1. Setup: Initializes the environment with Chrome and Python.
1. Script Execution: Runs main_v2.py, followed by storing the results in 中原放盤.xlsx.
1. Auto-push to GitHub: Commits and pushes the updated Excel file to the repository.

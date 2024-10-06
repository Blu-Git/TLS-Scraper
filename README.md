# TLS Web Scraper

This web scraper collects all article titles and links from **The LaSallian (TLS)** website for a given year. The user inputs a year (from 2010 onward), and the scraper gathers data from each page of articles published that year. The scraped data includes the article titles and their corresponding links, which are saved in a text file.

## Features

- Scrapes all article titles and links from a given year.
- Saves the scraped data in a text file named `{year}-articles.txt`.
- Handles pagination by automatically detecting the number of pages for each year.

## Installing and Using the Python Script (From GitHub Repo)

**Prerequisites:**

* Python 3.x (Download and install from https://www.python.org/downloads/)
* Packages: `requests`, `beautifulsoup4`, and `re`

**Install Code from Repo via Zip (for those unfamiliar with git):**
1. Click on the Code button and select Download ZIP.
2. Extract the ZIP file to your desired location.

**Install Modules (Using pip):**

1. Open a terminal or command prompt.
2. Make sure you're in the directory where you want to download the script.
3. Run the following command to install the required packages:

   ```bash
   pip install requests beautifulsoup4 re
   # replace "pip" with "pip3" if you are using a later version

**Running the Script:**
1. Navigate to the directory containing the script.
2. Open a terminal or command prompt in that directory.
3. Run the following command to execute the script:

    ```bash
    python3 scraper.py

# Sports News Scraper

## Overview:
- This is a simple Python web scraper that extracts the latest sports news from the **"The News"** website. It collects the news title, a short description, date, image link, and the full news article description. The extracted data is saved in a JSON format for easy use.

## Prerequisites:
- **Python 3.x**
- **Requests**: Install by running `pip install requests`
- **BeautifulSoup** (from `bs4`): Install by running `pip install beautifulsoup4`
- **Pandas**: Install by running `pip install pandas`

## How to Run the Script:
1. Clone the repository or save the script file to your local machine.
2. Navigate to the directory containing the script and install the necessary dependencies:

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

3. Run the script by executing:

    ```bash
    python script_name.py
    ```

4. The script will fetch the latest sports news articles, including titles, short descriptions, dates, and images, and save them to a JSON file named `sports_news.json`.

## Features:
- **News Title**: Extracts the headline of each news article.
- **Short Description**: Extracts a brief description from the news.
- **Date**: Extracts the publication date of the news.
- **Image Links**: Extracts the link to the image associated with the news article.
- **Full Description**: Scrapes the detailed news article from each link provided on the sports news page.

## File Information:
- **Script File**: Contains the logic to fetch, parse, and extract data from the website and save it to a JSON file.
- **Output File**: The extracted data is saved in `sports_news.json` in a structured format with fields such as `News_Title`, `Short_Discrition`, `Date`, `Image`, `Link`, and `Discription`.

## Example Usage:
1. Run the script as described in the **How to Run the Script** section.
2. Check the generated `sports_news.json` file in the same directory for the extracted sports news data.



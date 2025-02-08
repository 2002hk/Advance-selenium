# Used Advance Selenium Techniques to scrape amazon website
## Libraries used 
- undetected_chromedriver
- selenium
- pandas
- os
## workflow summary
### Initialize WebDriver:
- Uses undetected_chromedriver (uc) to launch a Chrome browser in non-headless mode (headless=False).
- use_subprocess=True allows execution without an if __name__ == "__main__" block.
### Navigate to Amazon & Perform Search:
- Opens Amazon India homepage.
- Finds the search bar using XPath and enters "pendrive".
### Scrape Product Links:
- Extracts product links from the search results using the provided XPath.
### Iterate Through Product Links:
- Clicks each product link to open it in a new tab.
- Extracts name, price, and brand using their respective XPath selectors.
- Stores extracted data in a list.
- Closes the product tab and switches back to the original search results page.
### Save Data to CSV:
- Converts the extracted data into a Pandas DataFrame.
- Saves it as pendrives.csv in an output2 directory.

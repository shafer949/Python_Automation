# Python Automation 101
If you have tasks that are repetative or time consuming then stick around as this repo contains various examples on how to get started using Python for automation. 

#### Why use automation?
- It is significantly faster than any human action.
- Thousands of requests can be executed at once.

## Setup
You will need to install Python from [here](https://www.python.org/downloads/). Be sure to pick the installation option that suits your operating system. 
>Note: Windows and gitbash was used when creating this content.

#### Install the following Python libraries: 
- requests - Used for creating the requests
  - (Windows) py -m pip install requests 
- lxml - Used to process the html when web scrapping
  - (Windows) py -m pip install lxml 
- beautifulsoup4 - Used to create a navigable and readable HTML response
  - (Windows) py -m pip install beautifulsoup4

#### Install Selenium items:
- Selenium example use the Chrome Driver installed from [here](https://chromedriver.chromium.org/downloads)
- For Windows:
  - Extract the contents of the download and move the chromedrive.exe file to your C://Windows directory.
- Then install Selenium 
  - (Windows) py -m pip install selenium


## Topics Covered
1. Introduction with printing "Hello World"
    - Check out script.py
2. Introduction on how to make API requests and read the response.
    - Check out apiCall.py and apiCallWithApiKey.py
4. Automating the process of reading a file and sorting the data into additional output files. 
    - Check out fileIO.py
5. Automating the process of organizing files within a given directory into additional directories based by filetype.
    - Check out organize.py
6. Web scrapping, single and multiple, websites for information.
    - Check out scrape.py and scrapePages.py
7. Automating web browser interactions with Selenium.
    - Check out webBrowsing.py, interactions.py, and dragAndDrop.py

## Practical Use Cases
Any repetitive task can be optimized with a Python script.
 - Sorting student grades based on if they passed or failed the class.
 - Organizing your messy computer files.
 - Comparing prices between websites.
 
## Resources
##### Documentation
- [Selenium Docs](https://www.selenium.dev/documentation/)
- [Selenium Tutorials](https://www.seleniumeasy.com/)
- [Beautiful Soup 4 Docs](https://beautiful-soup-4.readthedocs.io/en/latest/) 
- [Requests: HTTP for Humans Docs](https://docs.python-requests.org/en/latest/)
- [User Guide for Running pip](https://pip.pypa.io/en/latest/user_guide/)
##### Websites for Scraping
- [Scraping Club](https://scrapingclub.com/)
- [Quotes to Scrape](http://quotes.toscrape.com/)
- [Google Earth](https://www.google.com/earth/)
##### Demo Websites for Testing
- [Drag and Drop Demo](http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html)
- [Form Demo](http://demo.seleniumeasy.com/basic-first-form-demo.html)
##### APIs
- [Borded API](http://www.boredapi.com/api/activity/)
- [Giphy API](https://api.giphy.com/v1/gifs/random)
##### E-Learning Course
- [Using Python for Automation Course via LinkedIn Learning](https://www.linkedin.com/learning/using-python-for-automation?u=93824650)
##### Book
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
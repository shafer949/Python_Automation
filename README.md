# Python Automation 101
If you have tasks that are repetative or time consuming then stick around as this repo contains various examples on how to get started using Python for automation. 

## Setup
You will need to install Python from [here](https://www.python.org/downloads/). Be sure to pick the installation option that suits your operating system. 
>Note: Windows and gitbash was used when creating this content.

## Topics Covered
1. Introduction with printing "Hello World"
-- Check out script.py
2. Introduction on how to make API requests and read the response.
-- Check out apiCall.py and apiCallWithApiKey.py
4. Automating the process of reading a file and sorting the data into additional output files. 
-- Check out fileIO.py
5. Automating the process of organizing files within a given directory into additional directories based by filetype.
-- Check out organize.py
6. Web scrapping, single and multiple, websites for information.
-- Check out scrape.py and scrapePages.py
7. Automating web browser interactions with Selenium.
-- Check out webBrowsing.py, interactions.py, and dragAndDrop.py

## Getting Started

Sort Grades by Pass or Fail
1. Navigate to the Source Code directory, cd "Source Code", and run py fileIO.py in the terminal.
2. Notice two files are created: PassFile.txt and FailFile.txt within the Source Code directory.

Organize Files into Directories
1. Navigate to the OrganizeMe directory, cd .. then cd OrganizeMe.
2. Notice the list of files in the OrganizeMe directory.
3. Organize the files into directories by running py organize.py in the terminal.
4. Notice the list of files are now under corresponding directories based on filetype.

Web Scraping
https://pip.pypa.io/en/latest/user_guide/
1. Install libraries: 
- (Windows) py -m pip install requests - used for creating the GET query 
- (Windows) py -m pip install lxml - used to process the html
- (Windows) py -m pip install beautifulsoup4 - works with lxml to create a more navigable and readable HTML response 

Navigate to quotes.toscrape.com
Right click > Inspect

Scraping Multiple Pages 
https://scrapingclub.com/

Automate Web Browsing with Selenium
1. Install Chrome Driver - https://chromedriver.chromium.org/downloads
    - Extract contents
    - Move chromedrive.exe file to C://Windows directory
2. Install Selenium - (Windows) py -m pip install selenium
3. Using site https://www.seleniumeasy.com/ for demo


Any repetitive online task can be optimized with a Python script.

Use cases:
Botting limited quantity items like:
- Tickets to shows
- Exclusive merchandise

Why use automation?
- significantly faster than human actions
- execute thousands of requests at once

Drag and Drop
URL - http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html


Why use Wait Functions?
- Many websites use asynchronous techniques to load content
- Technique creates a problem when Selenium tries to locate an element that isn't loaded yet
- Avoid exceptions in scripts - failing scripts

Wait functions add crucial time intervals in between actions performed. Allowing the web driver to wait until the element is loaded before it interacts with it. 

Explicit Wait Functions
- Will wait until a condition is satisfied before executing

Implicit Wait Functions
- Pull DOM for a certain amount of time, until the element becomes available

URL for demo: googe.com/earth (uses ajax)

Automating with APIs
An Applications Programming Interface (API) enables developers to create repetitive but highly sophisticated software with minimal code.

API 
- prepackaged functionality that can be dropped into a developers code
Ex. google maps
- acts as an intermediary for 2 pieces of software

2 Steps
1. Get Query sent to API with parameters
2. API returns JSON response

Resources:
Selenium Docs
Beautiful Soup Docs
Requests Docs
Book: Automate the Boring Stuff with Python - https://automatetheboringstuff.com/

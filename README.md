# Facebook Group/Page Follower Scraper

This is a quick and simple piece of functional programming I put together for a project my brother is creating, regarding genealogical research communities.

He needed a piece of software to harvest data from his list of several thousand unique Facebook pages, take names and member counts, and print them to a CSV file for ease of management.

The code I wrote followed these steps:

* Iterate through list of Facebook Group/Page URLs
* Use Selenium's Chrome Driver to open link in separate Chrome window
* Create DOM soup using BeautifulSoup
* Locate <div> elements by unique list of classnames
* Harvest information from those elements
* Format text data into numerical data
* Append to the CSV

Any questions about this project, please don't hesitate to get in touch.
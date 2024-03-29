# Popular sites

This repo is to grab some data from the most popular websites visited on the web according to Wikipedia.

The initial use case was to quickly find out the sites using `data-testid` attributes, but could be extended to grab any data from the home page source code of the 50 most popular sites on the web.

_Note: As it was a quick and dirty project to grab some data to support a presentation, no effort was made to fix any errors returned by any website._

## Instructions

Simply run `search_html()` to get the sites currently using data-testid attributes. Or search for a different attribute by changing `attribute` in `search_html()`.

### Example output

![Example output](./readme_images/data-testid_popular_sites.png)

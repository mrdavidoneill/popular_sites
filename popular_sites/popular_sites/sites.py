import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_site_urls():
    """
        Retrieves the URLs of the most visited websites from the Wikipedia page _List_of_most-visited_websites_.

    Returns:
        list: A list containing the URLs of the most visited websites.

        The function fetches the HTML content of a Wikipedia page listing the most visited websites.
        It parses the HTML content and extracts the URLs from the second column of the first table
        with the class 'wikitable'. If a URL is missing a scheme, it adds 'http://' as a default scheme.

        If successful, it returns a list of URLs. If any error occurs during the process, it prints
        an error message and returns an empty list.

    Example:
        >>> site_urls = get_site_urls()
        >>> print(site_urls)"""

    try:
        url = "https://en.wikipedia.org/wiki/List_of_most-visited_websites"

        # Fetch the HTML content of the Wikipedia page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the first table with class wikitable
        table = soup.find("table", class_="wikitable")

        if table:
            # Extract URLs from the second column of the table
            urls = []
            for row in table.find_all("tr")[1:]:  # Exclude header row
                cells = row.find_all("td")
                if len(cells) >= 2:
                    url_cell = cells[1]
                    cell_text = url_cell.get_text().strip()
                    # Add a scheme if it's missing
                    parsed_url = urlparse(cell_text)
                    if parsed_url.scheme:
                        urls.append(cell_text)
                    else:
                        urls.append("http://" + cell_text)

            return urls
        else:
            print("No table with class 'wikitable' found on the page.")
            return []

    except Exception as e:
        print("An error occurred:", e)
        return []


if __name__ == "__main__":
    popular_site_urls = get_site_urls()
    print("Popular site URLs:")
    for index, url in enumerate(popular_site_urls):
        print(f"{index + 1}: {url}")

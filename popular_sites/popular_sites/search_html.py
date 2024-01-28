import requests
from bs4 import BeautifulSoup
from sites import get_site_urls


class Style:
    """Utility class for styling the print statements"""

    RED = "\033[31m"
    GREEN = "\033[32m"


def search_for_attribute(url, attribute="data-testid"):
    """
        Searches for elements with a specified attribute in the HTML content of a webpage.

    Args:
        url (str): The URL of the webpage to search.
        attribute (str, optional): The attribute to search for in the HTML elements.
            Defaults to "data-testid".

    Returns:
        None: Prints the number of elements found with the specified attribute in the provided URL.
            If an error occurs during the process, it prints the error message along with the URL.
    """
    try:
        # Fetch the HTML content of the page
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Search for elements with data-testid attribute
        elements_with_testids = soup.find_all(attrs={attribute: True})

        if elements_with_testids:
            print(
                f"{Style.GREEN}{url} has {len(elements_with_testids)} {attribute} elements"
            )

    except Exception as e:
        print(f"{Style.RED}{url}: {e}")


# Example usage
if __name__ == "__main__":
    [search_for_attribute(url) for url in get_site_urls()]

import requests
from bs4 import BeautifulSoup

# Write a function to Get and parse html content from a Wikipedia page

def get_and_parse(url):
    print("Starting Operation.....")
    print("Getting URL......")
    print("Accessing webpage.....")
    
    try: # This try block is used to catch any exceptions that may occur during the HTTP request.
        webpage = requests.get(url)
        webpage.raise_for_status()  # This checks for HTTP errors
        print("Parsing webpage......")
        parsed_webpage = BeautifulSoup(webpage.content, "html.parser")
        print("Webpage Parsed successfully......")
        return parsed_webpage
    
    except requests.exceptions.RequestException as e: # This catches any RequestException and assigns the exception object to {e}.
        print(f"Error accessing the webpage: {e}")
        return None

def extract_article_title(parsed_webpage):
    print("Extracting title from parsed_webpage.............")
    Article_Title = parsed_webpage.find("span", class_="mw-page-title-main")
    print("Article Title extracteed successfully............")
    return Article_Title.text if Article_Title else "No title found" #This returns the text content of Article_Title if it exists; otherwise, returns "No title found".

def extract_article_text(parsed_webpage):
    content = {}
    current_heading = ""
    corresponding_paragraph = []
    
    print("Finding all Headers and paragraphs...........")
    elements = parsed_webpage.find_all(['h2', 'p'])

    for element in elements:
        if element.name == "h2":
            if current_heading and corresponding_paragraph: # Checks if there is a current heading and corresponding paragraphs.
                content[current_heading] = corresponding_paragraph # Adds the current heading and its paragraphs to the content dictionary.
            current_heading = element.get_text().strip()
            corresponding_paragraph = []
        
        elif element.name == 'p':
            corresponding_paragraph.append(element.get_text().strip())

    if current_heading and corresponding_paragraph:
        content[current_heading] = corresponding_paragraph
    print("Extraction of Headers and Paragraphs was successful..........")    

    return content

def redirecting_links(parsed_webpage):
    links = []
    print("Extracting all redirecting links..............")
    for link in parsed_webpage.find_all("a", href=True):
        href = link['href'] # Assigns the value of the href attribute to href.
        if href.startswith("/wiki/"): # Checks if the href starts with "/wiki/" to identify Wikipedia page links.
            full_url = "https://en.wikipedia.org" + href # Constructs the full URL by appending href to "https://en.wikipedia.org".
            links.append(full_url) # Adds the full URL to the links list.
    print("Extraction of all links was succesful..............")

    return links

def analyze_wikipedia_page(url):
    parsed_webpage = get_and_parse(url)
    if parsed_webpage is None:
        return None
    
    article_title = extract_article_title(parsed_webpage)
    article_text = extract_article_text(parsed_webpage)
    wiki_links = redirecting_links(parsed_webpage)
    print("Creating dictionary for all the extracts............")
    
    return {
        'article_title': article_title,
        'article_text': article_text,
        'wiki_links': wiki_links
    } # Returns a dictionary containing the article_title, article_text, and wiki_links.
      # This dictionary structure makes it easy to access each part of the extracted data.

# Test the last function on a Wikipedia page of your choice
url = "https://en.wikipedia.org/wiki/Web_scraping"
result = analyze_wikipedia_page(url)

if result: # Checks if result is not None. This will be the case if the analysis was successful.
    # Print article title
    print("The Article Title is:............")
    print(result['article_title'])
    print("\n")

    # Print article text
    print("Article Text:")
    for heading, paragraphs in result['article_text'].items(): # runs a loop over the items in the article_text dictionary, unpacking each key-value pair into heading and paragraphs.
        print(f"Heading: {heading}")
        for paragraph in paragraphs:
            print(paragraph)
        print("\n")

    # Print Wikipedia links
    print("Wikipedia Links:")
    for link in result['wiki_links']:
        print(link)
else:
    print("Failed to analyze the Wikipedia page.")
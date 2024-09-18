import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# List of URLs to scrape
urls = [
    "https://onepiece.limitlesstcg.com/cards/misc-promos?display=text",
    "https://onepiece.limitlesstcg.com/cards/prize-cards?display=text",
    "https://onepiece.limitlesstcg.com/cards/promotion-pack-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/film-red-promotion-card-set?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/event-pack-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/regional-participation-pack-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-02?display=text",
    "https://onepiece.limitlesstcg.com/cards/promotion-pack-02?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-03?display=text",
    "https://onepiece.limitlesstcg.com/cards/event-pack-02?display=text",
    "https://onepiece.limitlesstcg.com/cards/store-championship-participation-pack-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/premium-card-collection-25th-edition?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-04?display=text",
    "https://onepiece.limitlesstcg.com/cards/dash-pack-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/store-championship-participation-pack-02?display=text",
    "https://onepiece.limitlesstcg.com/cards/regional-participation-pack-02?display=text",
    "https://onepiece.limitlesstcg.com/cards/gift-collection-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/premium-card-collection-film-red?display=text",
    "https://onepiece.limitlesstcg.com/cards/sealed-battle-kit-01?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-05?display=text",
    "https://onepiece.limitlesstcg.com/cards/championship-2023-celebration-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/championship-2023-event-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/championship-2023-top-players-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/uta-deck-battle-participation-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/japanese-1st-anniversary-set?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-06?display=text",
    "https://onepiece.limitlesstcg.com/cards/event-pack-03?display=text",
    "https://onepiece.limitlesstcg.com/cards/regional-participation-pack-2024-1?display=text",
    "https://onepiece.limitlesstcg.com/cards/english-version-1st-anniversary-set?display=text",
    "https://onepiece.limitlesstcg.com/cards/event-pack-04?display=text",
    "https://onepiece.limitlesstcg.com/cards/regional-participation-pack-2024-2?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-07?display=text",
    "https://onepiece.limitlesstcg.com/cards/championship-2024-celebration-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/championship-2024-event-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/championship-2024-top-players-pack?display=text",
    "https://onepiece.limitlesstcg.com/cards/tournament-pack-08?display=text",
    "https://onepiece.limitlesstcg.com/cards/event-pack-05?display=text",
    "https://onepiece.limitlesstcg.com/cards/regional-participation-pack-2024-3?display=text",
    "https://onepiece.limitlesstcg.com/cards/st01-straw-hat-crew?display=text",
    "https://onepiece.limitlesstcg.com/cards/st02-worst-generation?display=text",
    "https://onepiece.limitlesstcg.com/cards/st03-the-seven-warlords-of-the-sea?display=text",
    "https://onepiece.limitlesstcg.com/cards/st04-animal-kingdom-pirates?display=text",
    "https://onepiece.limitlesstcg.com/cards/st05-one-piece-film-edition?display=text",
    "https://onepiece.limitlesstcg.com/cards/st06-absolute-justice?display=text",
    "https://onepiece.limitlesstcg.com/cards/st07-big-mom-pirates?display=text",
    "https://onepiece.limitlesstcg.com/cards/st08-monkey-d-luffy?display=text",
    "https://onepiece.limitlesstcg.com/cards/st09-yamato?display=text",
    "https://onepiece.limitlesstcg.com/cards/st10-the-three-captains?display=text",
    "https://onepiece.limitlesstcg.com/cards/st11-uta?display=text",
    "https://onepiece.limitlesstcg.com/cards/st12-zoro-sanji?display=text",
    "https://onepiece.limitlesstcg.com/cards/st13-the-three-brothers?display=text",
    "https://onepiece.limitlesstcg.com/cards/st14-3D2Y?display=text",
    "https://onepiece.limitlesstcg.com/cards/st15-red-edward-newgate?display=text",
    "https://onepiece.limitlesstcg.com/cards/st16-green-uta?display=text",
    "https://onepiece.limitlesstcg.com/cards/st17-blue-donquixote-doflamingo?display=text",
    "https://onepiece.limitlesstcg.com/cards/st18-purple-monkey-d-luffy?display=text",
    "https://onepiece.limitlesstcg.com/cards/st19-black-smoker?display=text",
    "https://onepiece.limitlesstcg.com/cards/st20-yellow-charlotte-katakuri?display=text",
    "https://onepiece.limitlesstcg.com/cards/op01-romance-dawn?display=text",
    "https://onepiece.limitlesstcg.com/cards/op02-paramount-war?display=text",
    "https://onepiece.limitlesstcg.com/cards/op03-pillars-of-strength?display=text",
    "https://onepiece.limitlesstcg.com/cards/op04-kingdoms-of-intrigue?display=text",
    "https://onepiece.limitlesstcg.com/cards/op05-awakening-of-the-new-era?display=text",
    "https://onepiece.limitlesstcg.com/cards/op06-wings-of-the-captain?display=text",
    "https://onepiece.limitlesstcg.com/cards/eb01-memorial-collection?display=text",
    "https://onepiece.limitlesstcg.com/cards/op07-500-years-in-the-future?display=text",
    "https://onepiece.limitlesstcg.com/cards/op08-two-legends?display=text",
    "https://onepiece.limitlesstcg.com/cards/op09-emperors-in-the-new-world?display=text"
]

# Initialize an empty list to hold all the card data
all_cards = []

# Loop through each URL and scrape data
for url in urls:
    print(f"Scraping {url}...")
    # Send an HTTP GET request to the website
    response = requests.get(url)

    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the relevant information from the HTML code
    cards = []
    for card in soup.select('div.card'):
        name = card.find('span', class_='card-text-name').get_text(strip=True)
        card_id = card.find('span', class_='card-text-id').get_text(strip=True)
        category = card.find('span', {'data-tooltip': 'Category'}).get_text(strip=True) if card.find('span', {'data-tooltip': 'Category'}) else 'No Category'
        color = card.find('span', {'data-tooltip': 'Color'}).get_text(strip=True) if card.find('span', {'data-tooltip': 'Color'}) else 'No Color'
        attribute = card.find('span', {'data-tooltip': 'Attribute'}).get_text(strip=True) if card.find('span', {'data-tooltip': 'Attribute'}) else 'No Attribute'

        # Initialize life, power, counter, and cost
        life = None
        power = None
        counter = None
        cost = None

        # Extracting data from 'card-text-type' section, handling both life and cost based on category
        type_section = card.find('p', class_='card-text-type')
        if type_section:
            type_text = type_section.get_text(strip=True)
            # Extracting life or cost from the end of the 'card-text-type' content
            if 'Life' in type_text:
                life = type_text.split('Life')[-1].split('•')[0].strip()
            elif 'Cost' in type_text:
                cost = type_text.split('Cost')[-1].split('•')[0].strip()

        # Power and attributes
        power_section = card.find('p', class_='card-text-section')
        if power_section:
            power_text = power_section.get_text(strip=True)
            if "Power" in power_text:
                power = power_text.split("Power")[0].strip()
            # Extracting counter, ensuring to remove any leading bullet points or spaces
            if attribute and 'Counter' in power_text:
                counter_text = power_text.split(attribute)[-1]
                counter = counter_text.replace('•', '').strip()

        # Default power to 'null' for event and stage cards
        if category in ['Event', 'Stage'] and not power:
            power = 'null'

        # Ability Text
        ability_text_sections = card.find_all('div', class_='card-text-section')
        ability_text = ability_text_sections[-1].get_text(strip=True) if ability_text_sections else 'No Ability Text'

        card_type = card.find('span', {'data-tooltip': 'Type'}).get_text(strip=True) if card.find('span', {'data-tooltip': 'Type'}) else 'No Type'

        # Append the extracted data to the list
        cards.append([name, card_id, category, color, attribute, life, power, counter, cost, ability_text, card_type])

    # Add the scraped data for this URL to the overall list
    all_cards.extend(cards)

    # Add a delay between requests to avoid overwhelming the website with requests
    time.sleep(1)

# Store the information in a pandas dataframe
df = pd.DataFrame(all_cards, columns=['Name', 'ID', 'Category', 'Color', 'Attribute', 'Life', 'Power', 'Counter', 'Cost', 'Ability Text', 'Type'])

# Export the data to a CSV file
df.to_csv('onepiece-cards.csv', index=False)

print("Data scraping complete.")

import requests

API_KEY = "YOUR_NEWSAPI_KEY_HERE"

def get_news(category):
    """Fetch top headlines for a category from NewsAPI."""
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "category": category,
        "country": "us",
        "pageSize": 5,
        "apiKey": API_KEY
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()["articles"]

def main():
    print("=== TODAY'S NEWS BRIEF ===")
    print("1. Technology")
    print("2. Business")
    print("3. Health")
    print("4. Sports")
    print("5. Science")

    choice = input("\nPick a category (1-5): ")
    categories = {"1": "technology", "2": "business", "3": "health", "4": "sports", "5": "science"}
    category = categories.get(choice, "technology")

    print(f"\n--- TOP 5 {category.upper()} HEADLINES ---\n")

    try:
        articles = get_news(category)
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   {article['description'] or 'No description'}")
            print(f"   Link: {article['url']}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Check your API key and internet.")

if __name__ == "__main__":
    main()
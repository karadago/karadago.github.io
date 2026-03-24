import os
import json
import urllib.request

api_key = os.environ.get("SCOPUS_API_KEY")
author_id = os.environ.get("SCOPUS_AUTHOR_ID")

# The Scopus Author Retrieval API endpoint
url = f"https://api.elsevier.com/content/author/author_id/{author_id}"
headers = {
    "Accept": "application/json",
    "X-ELS-APIKey": api_key
}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        
        # Extract the citation count
        author_data = data.get('author-retrieval-response', [{}])[0]
        citation_count = author_data.get('coredata', {}).get('citation-count', '0')
        
        # Save to a local JSON file
        with open('citations.json', 'w') as f:
            json.dump({"total_citations": citation_count}, f)
            
        print(f"Success! Saved citation count: {citation_count}")

except Exception as e:
    print(f"An error occurred: {e}")

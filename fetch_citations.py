import json
import urllib.request

author_id = "A5019444409" 

headers = {
    "User-Agent": "mailto:omer.karadag@ozyegin.edu.tr" 
}

url = f"https://api.openalex.org/authors/{author_id}"

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        
        # OpenAlex stores the number under 'cited_by_count'
        citation_count = data.get('cited_by_count', 0)
        
        # Save to the exact same JSON file so your HTML doesn't break!
        with open('citations.json', 'w') as f:
            json.dump({"total_citations": citation_count}, f)
            
        print(f"Success! Saved OpenAlex citation count: {citation_count}")

except Exception as e:
    print(f"An error occurred: {e}")

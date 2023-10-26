import os
import requests

def fetchAndSaveToFile(url, filename):
    r = requests.get(url)
    
    # Create the 'data' directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    with open(os.path.join("data", filename), "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://www.thedailystar.net/opinion/editorial/news/gaza-bleeding-and-needs-help-urgently-3446006"
fetchAndSaveToFile(url, "times.html")




# import requests

# def fetchAndSaveToFile(url, path):
#     r = requests.get(url)
#     with open(path, "w") as f:
#         f.write(r.text)

# url = "https://www.thedailystar.net/opinion/editorial/news/gaza-bleeding-and-needs-help-urgently-3446006"
# fetchAndSaveToFile(url, "data/times.html")
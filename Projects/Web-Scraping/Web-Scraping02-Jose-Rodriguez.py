import requests
res = requests.get("https://gutenberg.org/cache/epub/67641/pg67641.txt")
res.raise_for_status()
playFile = open("Idealia, a Utopian Dream.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
import re
import requests
WORD_LENGTH = 5
GAME_DISPLAY = []
LIVES = 6

meaningpedia_resp = requests.get(
    "https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')

ACCEPTABLE_WORDS_LIST = pattern.findall(meaningpedia_resp.text)

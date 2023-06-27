import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Два кота, два друга, шли как-то по тропинке в лесу. Шли два кота, шли, пока не ушли с тропинки и не дошли
до деревни. Два кота решили не идти дальше и остаться жить в деревне"""
print(top_10_words(text))
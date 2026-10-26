dictionary = {
    "i": "من",
    "love": "عاشق هستم",
    "python": "پایتون",
    "programming": "برنامه‌نویسی",
    "is": "است",
    "fun": "جذاب"
}

sentence = "I love python"
words = sentence.lower().split()

translated_words = []
for word in words:
    translated_words.append(dictionary.get(word, word))

translated_sentence = " ".join(translated_words)

print(f"جمله اصلی: {sentence}")
print(f"ترجمه: {translated_sentence}")
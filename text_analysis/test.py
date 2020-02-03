import operator
PUNCTUATION = "!.?,;:\'\"[]{}()/\\-+="

def main():
    #text = "This is a long story. Some sentances can go on and on for days but others are short.\nThis is another point to be made, but not too well or else I will not see anything. This is also how I normally talk.\n This is a statement. I am not too well and I will not say others are short."
    text, stats = load_text("neuromancer.txt")
    three_words = phrase_analysis(text)
    four_words = phrase_analysis(text, 4)

    for phrase, count in three_words[:20]:
        print (f"{count} => {phrase}")

    for phrase, count in four_words[:20]:
        print (f"{count} => {phrase}")

    char_count, word_count = stats
    print (f"Chars: {char_count}\nWords: {word_count}")

def phrase_analysis(_text, _length=3):
    words = _text.split()
    words = [word.strip(PUNCTUATION).strip().lower().strip() for word in words if word.strip(PUNCTUATION).strip().lower().strip()]

    phrases = {}
    end = len(words) - _length
    for i in range(end):
        phrase = ""
        for j in range(_length):
            phrase += f" {words[i + j]}"
        phrase = phrase.strip()
        if phrase not in phrases.keys():
            phrases[phrase] = 0
        phrases[phrase] += 1

    phrases = sorted(phrases.items(), key=operator.itemgetter(1), reverse=True)

    return phrases

def load_text(_file):
    file = open(_file)
    text = file.read()
    file.close()
    stats = get_stats(text)
    return text, stats

def get_stats(_text):
    char_length = len(_text.replace(' ', ''))
    word_length = len(_text.split())
    return (char_length, word_length)



if __name__ == "__main__":
    main()

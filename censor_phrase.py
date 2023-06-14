def censor_phrase(phrase, text):
    words_to_censor = phrase.split()
    censored_text = text

    for word in words_to_censor:
        censored_text = censored_text.replace(word, "**" + word + "**")

    return censored_text
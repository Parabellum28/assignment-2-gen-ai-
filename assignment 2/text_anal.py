def analyze_text(text):
    words=text.split()
    vowels= "aeiou AEIOU"
    vowel_count=0
    consonant_count=0
    for ch in text:
        if ch in vowels:
            vowel_count +=1
        elif ch.isalpha():
            consonant_count+= 1
    freq={}
    for w in words:
        w=w.lower()
        freq[w]=freq.get(w,0) +1
    longest = words[0]
    for w in words:
        if len(w)> len(longest):
            longest=w

    print("TEXT ANALYSIS")
    print("words:",len(words))
    print("vowels:",vowel_count)
    print("Consonants:", consonant_count)
    print("reversed:",text[::-1])
    print("Palindrome:", "Yes" if text.replace(" ","").lower()==text.replace(" ","").lower()[::-1] else"No")
    print("Without vowels:","".join(c for c in text if c not in vowels))
    print("longest word:", longest, "(", len(longest), "letters)")
    print("word Frequency:", freq)
text = input("enter text: ")
analyze_text(text)
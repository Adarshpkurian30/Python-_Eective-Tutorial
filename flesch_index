ef calculate_word_count(content):
    word_list = content.split()
    return len(word_list)

def calculate_sentence_count(content):
    sentence_terminators = ['.', '?', '!']
    sentence_count = 0
    is_inside_sentence = False

    for character in content:
        if character in sentence_terminators:
            sentence_count += 1
            is_inside_sentence = False
        else:
            is_inside_sentence = True

    if is_inside_sentence:
        sentence_count += 1

    return sentence_count

def calculate_syllable_count(word):
    word = word.lower()
    syllable_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    if len(word) <= 3:
        return 1

    if word.endswith(('es', 'ed')):
        word = word[:-2]
    elif word.endswith('e') and not word.endswith('le'):
        word = word[:-1]

    for index, char in enumerate(word):
        if char in vowels:
            syllable_count += 1
            if index > 0 and word[index - 1] in vowels:
                syllable_count -= 1

    return syllable_count

def calculate_total_syllables(content):
    total_syllable_count = 0
    for word in content.split():
        total_syllable_count += calculate_syllable_count(word)
    return total_syllable_count

def compute_flesch_index(total_words, total_sentences, total_syllables):
    if total_words == 0 or total_sentences == 0:
        return 0
    return 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)

def compute_grade_level(total_words, total_sentences, total_syllables):
    if total_words == 0 or total_sentences == 0:
        return 0
    return 0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59

def analyze_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    total_words = calculate_word_count(content)
    total_sentences = calculate_sentence_count(content)
    total_syllables = calculate_total_syllables(content)

    flesch_score = compute_flesch_index(total_words, total_sentences, total_syllables)
    grade_level = compute_grade_level(total_words, total_sentences, total_syllables)

    print(f"Flesch Index: {flesch_score:.2f}")
    print(f"Grade Level: {grade_level:.2f}")

    if flesch_score >= 90:
        print("Readability: 4th Grade")
    elif flesch_score >= 50:
        print("Readability: High School")
    else:
        print("Readability: College")

# Run the analysis
analyze_text_file('input.txt')

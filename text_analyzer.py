# Helper function to separate text into words for further use.
def separate_words(text):
    # Creating skips list for ignoring non-letter signs.
    skips = [".", ",", "\n", ":", ";", "'", '"', "’", "!", "?", "(", ")"]
    # Searching and replacing skip signs with "".
    for char in skips:
        if char == "\n":
            text = text.replace(char, " ")
        else:
            text = text.replace(char, "")

    # Splitting text into words.
    words = text.split(" ")

    for word in words:
        if word == "":
            words.remove("")

    return words


# Function for finding word count in the text.
def word_count(text):
    words = separate_words(text)
    return len(words)


# Function for finding letter count in the text.
def letter_count(text):
    words = separate_words(text)
    count = 0
    for word in words:
        count += len(word)

    return count


# Function for finding longest word in the text.
def longest_word(text):
    words = separate_words(text)

    word_longest = ""
    for word in words:
        if len(word) > len(word_longest):
            word_longest = word

    return word_longest


# Function for finding average word length in the text.
def avg_word_length(text):
    return letter_count(text) / float(word_count(text))


# Function for finding reading duration of the text.
def reading_duration(text):
    time_for_one_word = 60.0 / 200
    return word_count(text) * time_for_one_word


# Helper function for median functions.
# Sorts all words according to their lengths and returns all information as a list of (length, word) for further use.
def helper_median(text):
    words = separate_words(text)
    length_list = []

    for word in words:
        length_list.append([len(word), word])

    length_list.sort()
    return length_list


# Function for finding median word length of the text.
def median_word_length(text):
    length_list = helper_median(text)
    size = len(length_list)
    if size % 2 == 1:
        return length_list[size // 2][0]
    else:
        median = (length_list[size // 2][0] + length_list[(size // 2) - 1][0]) / 2.0
        return median


# Function for finding median word by length in the text.
def median_word_by_length(text):
    length_list = helper_median(text)
    size = len(length_list)
    if size % 2 == 1:
        return length_list[size // 2][1]
    else:
        return length_list[size // 2][1], length_list[(size // 2) - 1][1]


# Function for finding five most common words in the text.
def five_most_common_word(text):
    words = separate_words(text.lower())
    unique_word_list = []
    freq_list = []

    for word in words:
        if word not in unique_word_list:
            unique_word_list.append(word)

    for unique_word in unique_word_list:
        freq_list.append([words.count(unique_word), unique_word])

    freq_list.sort(reverse=True)    # reverse=True means sort in ascending order.
    # print(freq_list)
    result = []
    for i in range(5):
        result.append(freq_list[i][1])

    return result


# Function for finding language of the text.
def text_language(text):
    words = separate_words(text.lower())    # Here we lower text to count Deep and deep as same for example.

    # Stop words list for English
    stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
                  "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
                  "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
                  "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be",
                  "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
                  "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
                  "with", "about", "against", "between", "into", "through", "during", "before", "after", "above",
                  "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
                  "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
                  "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                  "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    # Some words can be both in English and Turkish.
    collision_words = ["it", "an", "as", "of", "at", "in", "on"]

    for word in words:
        if (word in stop_words) and (word not in collision_words):
            return "English"

    return "Turkish"

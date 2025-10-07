import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download necessary data for NLTK
nltk.download('punkt')
nltk.download('stopwords')

def nltk_summarize(text, summary_ratio=0.3):
    """
    Summarize the input text using frequency-based scoring.
    summary_ratio: 0.3 means 30% of sentences will be kept in the summary.
    """
    # Step 1: Tokenize words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())

    # Step 2: Create frequency table of important words
    freq_table = {}
    for word in words:
        if word not in stop_words and word not in string.punctuation:
            freq_table[word] = freq_table.get(word, 0) + 1

    # Step 3: Score each sentence
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq

    # Step 4: Select top sentences for summary
    summary_length = int(len(sentences) * summary_ratio)
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:summary_length])
    return summary
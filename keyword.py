import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

sentence = "here’s so much more about Trump to investigate than just Russia: Tax evasion, fraud, misuse of charitable funds..."

lemmatizer = WordNetLemmatizer()

def preprocess_with_lemmatization(text):
    # convert text to lowercase
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # split text into words
    tokens = word_tokenize(text)
    # remove stopwords - remove words like a, and, at, etc
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # lemmatization - break down a word to its root meaning
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    text = ' '.join(lemmatized_tokens)
    return text

preprocessed_sentence = preprocess_with_lemmatization(sentence)

print("Preprocessed sentence:")
print(preprocessed_sentence)
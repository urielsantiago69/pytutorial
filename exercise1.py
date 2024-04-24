def count_words(input): # DO-NOT CHANGE NAME OF THE FUNCTION
  # Because words are delimited by spaces
  words = input.split()
  num_words = len(words)

  # Because sentences are delimited by punctuation marks
  num_sentences = 0
  punctuation = {'.', '!', '?'}

  for char in input:
      if char in punctuation:
          num_sentences += 1

  return {'words': num_words, 'sentences': num_sentences} # Update this  function according to the tasks.
  
# print(count_words("Hello. How are you?"))


def detect_all(input): # DO-NOT CHANGE NAME OF THE FUNCTION
  # Split the text into words based on whitespace
  words = input.split()

  # Initialize an empty list to store the words with less than 5 letters
  short_words = []

  # Loop through each word in the list
  for word in words:
      # If the length of the word is less than 5, add it to the list
      if len(word) < 5:
          short_words.append(word)

  return short_words # Update this  function according to the tasks.

#print(detect_all("I walked through the door with you, the air was cold"))

def detect_exclude_vowels(input): # DO-NOT CHANGE NAME OF THE FUNCTION
  # Define vowels as a string
  vowels = 'aeiouAEIOU'
  # Split the text into words based on whitespace
  words = input.split()

  # Initialize an empty list to store the qualifying words
  filtered_words = []

  # Loop through each word in the list
  for word in words:
      # Count non-vowel characters
      non_vowel_count = 0
      for char in word:
          if char not in vowels:
              non_vowel_count += 1

      # Check if non-vowel count is less than 5
      if non_vowel_count < 5:
          filtered_words.append(word)

  return filtered_words # Update this  function according to the tasks.

input_text = "Here are some words: tree, cat, apple, dog, cup, fantastic."
result = detect_exclude_vowels(input_text)
print("Words with less than 5 non-vowel letters:", result)

def special_ordering(input): # DO-NOT CHANGE NAME OF THE FUNCTION
  return None # Update this  function according to the tasks.

def remember_previous(input): # DO-NOT CHANGE NAME OF THE FUNCTION
  return None # Update this  function according to the tasks.

class Submission: # DO-NOT CHANGE THIS LINE

  def __init__(self): # DO-NOT CHANGE THIS line

      self.EXERCISE = "1" # DO-NOT CHANGE THIS line

      self.NAME = "Emerson Banez" # Replace with your name
      self.ID   = "3LA23003K"   # Replace with your enrollment ID

  # DO-NOT CHANGE THIS FUNCTION
  def run(self):
      return (count_words, detect_all, detect_exclude_vowels, special_ordering, remember_previous) # DO-NOT CHANGE THIS LINE
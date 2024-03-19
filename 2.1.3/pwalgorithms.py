# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  word = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
    word.append(line[:-1])
  dictionary_file.close()
  return words, word


# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    print(w)
    if (w == password):
      return True, guesses
  return False, guesses

def two_word(password):
  words = get_dictionary()
  guesses = 0
  for w in words:
    for ws in words:
      guesses += 1
      myGuess = w + ws
      print(myGuess)
      if (w + ws) == password:
        return True, guesses
  return False, guesses



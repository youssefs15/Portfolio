
def censor(text, word):
  split_text = text.split()
  l = "*" * len(word)
  new_text = ""
  count= 0
  for char in split_text:
    if char == word:
      split_text[count] = l
    count += 1
  new_text = " ".join(split_text)
  print new_text
  return new_text

censor("I III I I I I IIIII", "I")

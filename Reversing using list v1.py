def reverse(text):
  reversed_str=[]
  index = len(text)
  while index > 0:
    reversed_str += text[index - 1]
    index -= 1
  string = ''.join(reversed_str)
  print string

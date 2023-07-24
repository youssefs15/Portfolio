x=0
while x == 0:
  try:
    PassCredit = int(input("Please enter your credit at pass:"))
    if PassCredit == 0 or PassCredit == 20 or PassCredit == 40 or PassCredit == 60 or PassCredit == 80 or PassCredit == 100 or PassCredit == 120:
      DeferCredit = int(input("Please enter your credit at defer:"))
      if DeferCredit == 0 or DeferCredit == 20 or DeferCredit == 40 or DeferCredit == 60 or DeferCredit == 80 or DeferCredit == 100 or DeferCredit == 120:
        FailCredit = int(input("Please enter your credit at fail:"))
        if FailCredit == 0 or FailCredit == 20 or FailCredit == 40 or FailCredit == 60 or FailCredit == 80 or FailCredit == 100 or FailCredit == 120:
          TotalCredit = PassCredit+DeferCredit+FailCredit
          if TotalCredit == 120:
            x+=1
          else:
            print("Error: Total incorrect")
        else:
          print("Error: Out of range")
      else:
        print("Error: Out of range")
    else:
      print("Error: Out of range")
  except ValueError:
    print("Intger required")

if PassCredit == 120 and DeferCredit == 0 and FailCredit == 0:
  print("Progress")
elif PassCredit == 100 and DeferCredit == 20 and FailCredit == 0:
  print("Progress(module trailer)")
elif PassCredit == 100 and DeferCredit == 0 and FailCredit == 20:
  print("Progress(module trailer)")
elif PassCredit == 80 and DeferCredit == 40 and FailCredit == 0:
  print("Do not Progress – module retriever")
elif PassCredit == 80 and DeferCredit == 20 and FailCredit == 20:
  print("Do not Progress – module retriever")
elif PassCredit == 80 and DeferCredit == 0 and FailCredit == 40:
  print("Do not Progress – module retriever")
elif PassCredit == 60 and DeferCredit == 60 and FailCredit == 0:
  print("Do not Progress – module retriever")
elif PassCredit == 60 and DeferCredit == 40 and FailCredit == 20:
  print("Do not Progress – module retriever")
elif PassCredit == 60 and DeferCredit == 20 and FailCredit == 40:
  print("Do not Progress – module retriever")
elif PassCredit == 60 and DeferCredit == 0 and FailCredit == 60:
  print("Do not Progress – module retriever")
elif PassCredit == 40 and DeferCredit == 80 and FailCredit == 0:
  print("Do not Progress – module retriever")
elif PassCredit == 40 and DeferCredit == 60 and FailCredit == 20:
  print("Do not Progress – module retriever")
elif PassCredit == 40 and DeferCredit == 40 and FailCredit == 40:
  print("Do not Progress – module retriever")
elif PassCredit == 40 and DeferCredit == 20 and FailCredit == 60:
  print("Do not Progress – module retriever")
elif PassCredit == 40 and DeferCredit == 0 and FailCredit == 80:
  print("Exclude")
elif PassCredit == 20 and DeferCredit == 100 and FailCredit == 0:
  print("Do not Progress – module retriever")
elif PassCredit == 20 and DeferCredit == 80 and FailCredit == 20:
  print("Do not Progress – module retriever")
elif PassCredit == 20 and DeferCredit == 60 and FailCredit == 40:
  print("Do not Progress – module retriever")
elif PassCredit == 20 and DeferCredit == 40 and FailCredit == 60:
  print("Do not Progress – module retriever")
elif PassCredit == 20 and DeferCredit == 20 and FailCredit == 80:
  print("Exclude")
elif PassCredit == 20 and DeferCredit == 0 and FailCredit == 100:
  print("Exclude")
elif PassCredit == 0 and DeferCredit == 120 and FailCredit == 0:
  print("Do not Progress – module retriever")
elif PassCredit == 0 and DeferCredit == 100 and FailCredit == 20:
  print("Do not Progress – module retriever")
elif PassCredit == 0 and DeferCredit == 80 and FailCredit == 40:
  print("Do not Progress – module retriever")
elif PassCredit == 0 and DeferCredit == 60 and FailCredit == 60:
  print("Do not Progress – module retriever")
elif PassCredit == 0 and DeferCredit == 40 and FailCredit == 80:
  print("Exclude")
elif PassCredit == 0 and DeferCredit == 20 and FailCredit == 100:
  print("Exclude")
elif PassCredit == 0 and DeferCredit == 0 and FailCredit == 120:
  print("Exclude")

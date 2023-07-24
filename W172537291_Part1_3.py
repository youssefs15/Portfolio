TempProgress = 0
TempExclude = 0
TempTrailer = 0
TempRetriever = 0
def Marks():
  Progress = 0
  Trailer = 0
  Retriever = 0
  Exclude = 0
  x = 0
  while x == 0:
    x = 0
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
    Progress +=1
  elif PassCredit == 100 and DeferCredit == 20 and FailCredit == 0:
    print("Progress(module trailer)")
    Trailer +=1
  elif PassCredit == 100 and DeferCredit == 0 and FailCredit == 20:
    print("Progress(module trailer)")
    Trailer +=1
  elif PassCredit == 80 and DeferCredit == 40 and FailCredit == 0:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 80 and DeferCredit == 20 and FailCredit == 20:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 80 and DeferCredit == 0 and FailCredit == 40:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 60 and DeferCredit == 60 and FailCredit == 0:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 60 and DeferCredit == 40 and FailCredit == 20:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 60 and DeferCredit == 20 and FailCredit == 40:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 60 and DeferCredit == 0 and FailCredit == 60:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 40 and DeferCredit == 80 and FailCredit == 0:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 40 and DeferCredit == 60 and FailCredit == 20:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 40 and DeferCredit == 40 and FailCredit == 40:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 40 and DeferCredit == 20 and FailCredit == 60:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 40 and DeferCredit == 0 and FailCredit == 80:
    print("Exclude")
    Exclude +=1
  elif PassCredit == 20 and DeferCredit == 100 and FailCredit == 0:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 20 and DeferCredit == 80 and FailCredit == 20:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 20 and DeferCredit == 60 and FailCredit == 40:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 20 and DeferCredit == 40 and FailCredit == 60:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 20 and DeferCredit == 20 and FailCredit == 80:
    print("Exclude")
    Exclude +=1
  elif PassCredit == 20 and DeferCredit == 0 and FailCredit == 100:
    print("Exclude")
    Exclude +=1
  elif PassCredit == 0 and DeferCredit == 120 and FailCredit == 0:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 0 and DeferCredit == 100 and FailCredit == 20:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 0 and DeferCredit == 80 and FailCredit == 40:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 0 and DeferCredit == 60 and FailCredit == 60:
    print("Do not Progress – module retriever")
    Retriever +=1
  elif PassCredit == 0 and DeferCredit == 40 and FailCredit == 80:
    print("Exclude")
    Exclude +=1
  elif PassCredit == 0 and DeferCredit == 20 and FailCredit == 100:
    print("Exclude")
    Exclude +=1
  elif PassCredit == 0 and DeferCredit == 0 and FailCredit == 120:
    print("Exclude")
    Exclude +=1

  return Exclude,Retriever,Trailer,Progress

def Graph():
  global TempProgress,TempExclude,TempRetriever,TempTrailer
  Exclude,Retriever,Trailer,Progress= Marks()
  TempProgress += Progress
  TempExclude += Exclude
  TempRetriever += Retriever
  TempTrailer += Trailer
  Again = str(input("\nDo you want to enter another set of data?\nEnter 'Y' for yes or 'Q' for quit and view results: "))
  if Again in  ["Y", "y"]:
    Graph()
  elif Again in  ["Q", "q"]:
    Totaloutcomes = TempExclude+TempRetriever+TempTrailer+TempProgress
    print("-------------------------------------------------------------------")
    print ("Progress",TempProgress," : ", end=="")
    for starE in range(TempProgress):
           print("*", end=="")
    print ("\nTrailer",TempTrailer,"  : ", end=="")
    for starE in range(TempTrailer):
           print("*", end=="")
    print ("\nRetriever",TempRetriever,":",end=="")
    for starE in range(TempRetriever):
            print("*", end=="")
    print ("\nExclude",TempExclude,"  : ", end=="")
    for starE in range(TempExclude):
            print("*", end=="")
    print("\n\nTotal outcomes:", Totaloutcomes)
    print("-------------------------------------------------------------------")

Graph()
  

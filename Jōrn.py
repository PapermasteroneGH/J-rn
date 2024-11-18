import webbrowser
import wikipedia

def wiki(search, limit):
    try:
        summary = wikipedia.summary(search, sentences=limit)
        print("Jōrn: Here's a summary of the page")
        print(summary)
        print("(type r to return)")
        search = input("what would you like to know next?: ")
        if search == "r":
            main()
        else:
            wiki(search, limit)
    except wikipedia.exceptions.DisambiguationError as e:
        print("The search term is ambiguous. Options are:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print("The page could not be found.")

def Reconnaissance():
  print("")
        
def engineer():
  print("welcome to engineering")
  print("what would you like to build?")
  input1 = input("(type (x) for an introduction)")
  if input1 == "x":
    print("")
  elif "plane" in input1:
    print("")

def main():
  print("          welcome to Jōrn(S.A.K)              ")
  print("                                              ")
  print("         what would you like to do?           ")
  print("(type (show list) to see the list of commands)")
  input1 = input("Enter:")
  if input1 == "show list":
    print("Jōrn: Heres a good list of what I can do")
    print("      a. generate information artificially (due to its current limitations by its code compiler, datas will be limited)")
    print("      b. active/passive reconnaissance")
    print("      c. engineer")
    print("      more")
    input2 = input("Enter: ")
    if input2 == "a":
      search = input("Jōrn: Enter search query: ")
      limit = input("summary length: ")
      try:
        summary = wikipedia.summary(search, sentences=limit)
        print("Jōrn: Here's a summary of the page")
        print(summary)
        search = input("what would you like to know next?: ")
        limit = input("summary length: ")
        if search == "r":
          main()
        else:
          wiki(search, limit)
      except wikipedia.exceptions.DisambiguationError as e:
        print("The search term is ambiguous. Options are: ")
        print(e.options)
      except wikipedia.exceptions.PageError:
        print("The page could not be found.")
        print("(type r to return)")
        search = input("what would you like to know next?: ")
        limit = input("summary length: ")
        if search == "r":
          main()
        else:
          wiki(search, limit)
    elif input2 == "b":
      print("still under construction")
      reTurn = input("(type r to return)")
      if reTurn == "r":
        main()
    elif input2 == "c":
      print("still under construction")
      reTurn = input("(type r to return)")
      if reTurn == "r":
        main()
    elif input2 == "more":
      print("a. what is Jōrn?")
      print("")
      input3 = input("")
      if input3 == "a":
        print("Jōrn is a swiss army knife program (S.A.K) that is built to simplify complex tasks such as reconnaissance, engineering, and more.")
        print('Jōrn was built by a high schooler with the name "剣太郎光中村" (for more info type "go")')
        reTurn = input("(type r to return)")
        if reTurn == "r":
          main()
        elif reTurn == "go":
          webbrowser.open("https://papermasteronegh.github.io/PAPYRUS-II/")
          afterRead = input("(type r to return)")
          if afterRead == "r":
            main()
    
main()
  

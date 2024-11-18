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
  print("")
        
def engineer():
  print("welcome to engineering")
  print("what would you like to build?")
  input1 = input("(type (x) for an introduction)")
  if input1 == "x":
    print("")
  elif "plane" in input1:
    print("")
    print("                          /\\")
    print("                         |  |")
    print("                         |  |")
    print("                        .'  '.")
    print("                        |    |")
    print("                        |    |")
    print("                        | /\\ |")
    print("                      .' |__|'.")
    print("                      |  |  |  |")
    print("                     .'  |  |  '.")
    print("                /\\   |   \\__/   |   /\\")
    print("               |  |  |   |  |   |  |  |")
    print("           /|  |  |,-\\   |  |   /-,|  |  |\\")
    print("           ||  |,-'   |  |  |  |   '-,|  ||")
    print("           ||-'       |  |  |  |       '-||")
    print("|\\     _,-'           |  |  |  |           '-,_     /|")
    print("||  ,-'   _           |  |  |  |               '-,  ||")
    print("||-'    =(*)=         |  |  |  |                  '-||")
    print("||                    |  \\  /  |                    ||")
    print("|\\________....--------\\   ||   /--------....________/|")
    print("                      /|  ||  |\\")
    print("                     / |  ||  | \ ")
    print("                    /  |  \\/  |  \\")
    print("                   /   |      |   \\")
    print("                 //   .|      |.   \\\ ")
    print("               .' |_./ |      | \\._| '.")
    print("              /     _.-|||  |||-._     \\")
    print("              \\__.-'   \\||/\\||/   '-.__/")
  elif "car" in input1:
    print("")
    print("                     //|           |        \\")
    print("                   //  |           |          \\")
    print("      ___________//____|___________|__________()\\__________________")
    print("    /__________________|_=_________|_=___________|_________________{}")
    print("    [           ______ |           | .           | ==  ______      { }")
    print("  __[__        /##  ##\\|           |             |    /##  ##\\    _{# }_")
    print(" {_____)______|##    ##|___________|_____________|___|##    ##|__(______}")
    print("             /  ##__##                              /  ##__##        \\")
  elif "gun" in input1:
    print("")
    print("         ^")
    print("        | |")
    print("      @#####@")
    print("    (###   ###)-.")
    print("  .(###     ###) \\")
    print(" /  (###   ###)   )")
    print("(-=  .@#####@|_--\"")
    print(" /\\    \\_|l|_/ (\\")
    print("(=-\\     |l|    /")
    print(" \\  \\.___|l|___/")
    print(" /\\      |_|   /")
    print("(=-\\._________/\\")
    print(" \\             /")
    print("   \\._________/")
    print("     #  ----  #")
    print("     #   __   #")
    print("     \\########/")
  elif "cannon" in input1:
    print("")
    print("                          __..-----..__")
    print("                   __..--'__..-----..__`--..__")
    print("            __..--'__..--'    |  ||  - `--..__`--..__")
    print("           |`--..__`--..__    |  ||   __..---' __..--'")
    print("            `--..__`--..__`--..__..--\\\\__..---'__..--'")
    print("            |  ||  `--..__`--.._\\_..--\\)__..---' |  ||")
    print("            |  ||| \\|     `--.._|_..--/|         |  ||")
    print("((-.....____|  ||\\ ||        |  || \\| ||         |  ||")
    print("(o \\_  .-=./|  ||`-\\|--...___|  || || /|         |  ||")
    print(" `.( `-.__/ |  ||  |/ -  _   |  || `--|\\-....._____ ||")
    print("         / /|  ||.(/_ -    _ |  || _  ||   _       `---- .----.`")
    print("        / //|  ||    `--..___|  ||  _ \\\\      -   _   _ /      \\")
    print("       / // |  ||___....----`|  ||__  |/_     _         |      |")
    print("    ,` ` `. |  |\\\\.......--`/|  ||  `(/-....__        _ \\      /")
    print("   /  \\ /  \\|  | \\\\    _   / |  ||`-.._       `---....___`.__.'")
    print("   |  (O)  ||  |\\ \\\\ _    / /|  |\\\\_   `-.__ / //|  | \\")
    print("   \\  / \\  /._ ||\\ \\\\    / //|  | \\\\  _     / //-|  |\\ \\.`")
    print("    `/_ _\\'._ `-._\\ \\\\  / // |  |\\ \\\\          _ |  ||\\ \\\\")
    print("             `-.__ `-._/ //  |  ||\\ \\\\  _      _      _.-'||")
    print("                  `-.__ `-.__|,` ` `.`\\         _..--'_  |//")
    print("                       `-.__'/  \\ /  \\\\_  _..--'   _  _.-'.")
    print("                             |  (O)| || ||   _  _..--'")
    print("                             \\  / \\  //_||_..--'")
    print("                              `/_ _\\''")



    

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
      # print("still under construction")
      engineer()
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
  

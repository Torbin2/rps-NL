import random

draw = 0
lose = 0
win = 0

while True:
  
  def get_choices():

    pl = "kaas"
    
    spul = ["steen", "papier", "schaar"]
    keuze = random.choice(spul)
    een = keuze
    
    twee = input("kies(steen (1), papier (2), schaar (3)")
    
    if twee == "1":
      pl = "steen"
    elif twee == "2":
      pl = "papier"
    elif twee == "3":
      pl = "schaar"
    
    choices = {"player" : pl,"computer" : een}
    return choices
  
  def check_win(play, rng):

    global draw
    global win
    global lose
    
    print(f"computer keuze = {rng}\n")
    if play == rng:
      draw += 1
      return("gelijkspel")
    
    elif play == "steen":
      if rng == "schaar":
        win += 1
        return "steen breekt schaar,win!"
      else:
        lose = lose + 1
        return "papier stopt steen,verlies "
    
    elif play == "papier":
      if rng == "schaar":
        lose = lose + 1
        return "schaar knipt papier,verlies"
      else:
        win = win + 1
        return "papier stopt steen,win! "
    
    elif play == "schaar":
      if rng == "papier":
        win = win + 1
        return "schaar knipt papier,win!"
      else:
        lose = lose + 1
        return "steen breekt schaar,verlies"
  
   
  
  choices = get_choices()
  result = check_win(choices["player"],choices["computer"])
  print(result)
  print(f"W{win}, D{draw}, L{lose}\n\n")

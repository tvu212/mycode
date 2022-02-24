#!/usr/bin/env python3


char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)")

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")


marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }


print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat]}")

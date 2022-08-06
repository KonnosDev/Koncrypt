def K_dec(word):
    dec_word=""
    for char in word:
       if char == "#" :
            dec_word = dec_word + "A"
       elif char == "!" :
            dec_word = dec_word + "B"
       elif char == ":" :
            dec_word = dec_word + "C"
       elif char == "%" :
            dec_word = dec_word + "D"
       elif char == ";" :
            dec_word = dec_word + "E"
       elif char == "@" :
            dec_word = dec_word + "F"
       elif char == "e" :
            dec_word = dec_word + "G"
       elif char == "/" :
            dec_word = dec_word + "H"
       elif char == "[" :
            dec_word = dec_word + "I"
       elif char == "{" :
            dec_word = dec_word + "J"
       elif char == "(" :
            dec_word = dec_word + "K"
       elif char == "]" :
            dec_word = dec_word + "L"
       elif char == "}" :
            dec_word = dec_word + "M"
       elif char == ")" :
            dec_word = dec_word + "N"
       elif char == "=" :
            dec_word = dec_word + "O"
       elif char == "<" :
            dec_word = dec_word + "P"
       elif char == "?" :
            dec_word = dec_word + "Q"
       elif char == "+" :
            dec_word = dec_word + "R"
       elif char == "-" :
            dec_word = dec_word + "S"
       elif char == ">" :
            dec_word = dec_word + "T"
       elif char == "_" :
            dec_word = dec_word + "U"
       elif char == "*" :
            dec_word = dec_word + "V"
       elif char == "|" :
            dec_word = dec_word + "W"
       elif char == "&" :
            dec_word = dec_word + "X"
       elif char == "~" :
            dec_word = dec_word + "Y"
       elif char == "$" :
            dec_word = dec_word + "Z"
       elif char == "ς" :
            dec_word =dec_word + "a"
       elif char == "μ" :
            dec_word =dec_word + "b"
       elif char == "ε" :
            dec_word =dec_word + "c"
       elif char == "ν" :
            dec_word =dec_word + "d"
       elif char == "ρ" :
            dec_word =dec_word + "e"
       elif char == "β" :
            dec_word =dec_word + "f"
       elif char == "ω" :
            dec_word =dec_word + "g"
       elif char == "τ" :
            dec_word =dec_word + "h"
       elif char == "ψ" :
            dec_word =dec_word + "i"
       elif char == "υ" :
            dec_word =dec_word + "j"
       elif char == "θ" :
            dec_word =dec_word + "k"
       elif char == "ζ" :
            dec_word =dec_word + "l"
       elif char == "χ" :
            dec_word =dec_word + "m"
       elif char == "π" :
            dec_word =dec_word + "n"
       elif char == "ι" :
            dec_word =dec_word + "o"
       elif char == "α" :
            dec_word =dec_word + "p"
       elif char == "λ" :
            dec_word =dec_word + "q"
       elif char == "σ" :
            dec_word =dec_word + "r"
       elif char == "δ" :
            dec_word =dec_word + "s"
       elif char == "κ" :
            dec_word =dec_word + "t"
       elif char == "ξ" :
            dec_word =dec_word + "u"
       elif char == "η" :
            dec_word =dec_word + "v"
       elif char == "γ" :
            dec_word =dec_word + "w"
       elif char == "δ" :
            dec_word =dec_word + "x"
       elif char == "£" :
            dec_word =dec_word + "y"
       elif char == "Η" :
            dec_word =dec_word + "z"
       elif char == "Α" :
            dec_word =dec_word + "0"
       elif char == "Μ" :
            dec_word =dec_word + "1"
       elif char == "Π" :
            dec_word =dec_word + "2"
       elif char == "Ο" :
            dec_word =dec_word + "3"
       elif char == "Ξ" :
            dec_word =dec_word + "4"
       elif char == "Ε" :
            dec_word =dec_word + "5"
       elif char == "Ρ" :
            dec_word =dec_word + "6" 
       elif char == "Β" :
            dec_word =dec_word + "7"
       elif char == "Χ" :
            dec_word =dec_word + "8"
       elif char == "Ζ" :
            dec_word =dec_word + "9"
       else:
            dec_word =dec_word + char
    return dec_word

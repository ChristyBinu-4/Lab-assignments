def digitToWord(number):
    digitArray = {
        1 : "Uni",
        2 : "Bi",
        3 : "Tri",
        4 : "Four",
        5 : "Five",
        6 : "Six", 
        7 : "Seven", 
        8 : "Eight",
        9 : "Nine"
    }
    word = digitArray[number]
    return word
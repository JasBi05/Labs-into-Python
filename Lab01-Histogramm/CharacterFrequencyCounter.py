import os
class CharacterFrequencyCounter:
    def __init__(self):
        print("Welcome to the file editor, where it is even possible to create a histogram.")
        print("")
        print("Enter ‘create’ to create a file.")
        print("Enter ‘count’ to analyze a file.")
        print("Enter ‘histo’ to convert a text.txt file into a histogram.")
        print("Enter ‘exit’ to exit the program.")

    def create_file(self):
        while True:
            text = input()
            if text == "done":
                break
            with open("text.txt", "w") as file:
                file.write(text + "\n")

    def count_file(self):
        letterCounter = [0]*26
        letter = 0
        with open("text.txt", "r") as file:
            letter = file.read()
            for y in letter:
                if y.isalpha():
                    y = letter.upper()
                    index = ord(y) - ord('A')
                    letterCounter[index] += 1

        with open("frequency.txt", "w+") as freqWriter:
            for x in letterCounter:
                if x > 0:
                    chr(x + ord('A'))
                    freqWriter.write(str(letterCounter[x]) + "\n")

    def create_histo(self):
        print("create_histo() not implemented yet.")

    def run(self):
        while True:
            userinput = input("> ")

            if userinput == "create":
                self.create_file()
            elif userinput == "count":
                self.count_file()
            elif userinput == "histo":
                self.create_histo()
            elif userinput == "exit":
                print("Exiting program.")
                break
            else:
                print("Unknown command.")

app = CharacterFrequencyCounter()
app.run()

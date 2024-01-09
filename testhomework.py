file_input = "fizzbazzinput3.txt"
file_output = "fizzbazzoutput3.txt"
file_writing = open (file_output, "w")
with open (file_input,"r") as file_reading:
    for line in file_reading:
        fizz, buzz, num = map(int, line.split(","))
        for i in range(1, num + 1):
            fizz_buzz = ""
            if not i % fizz and not i % buzz:
                fizz_buzz += "FB"
            elif i % fizz == 0:
                fizz_buzz += "F"
            elif i % buzz == 0:
                fizz_buzz += "B"
            else:
                fizz_buzz += str(i)
            print(fizz_buzz, end = " ")
            file_writing.write(fizz_buzz + " ")
        file_writing.write("\n")
        print()
file_writing.close()
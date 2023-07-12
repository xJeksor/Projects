import sys

if __name__ == "__main__":
    # check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Error: Invalid number of arguments. Usage: python stegano.py [-e/-d] [algorithm number] [cover/watermark file]")
        sys.exit()

    # read message file
    with open("mess.txt", "r") as f:
        message = f.read()

    if sys.argv[1] == "-e":
        # read cover file
        with open(sys.argv[3], "r") as f:
            cover_text = f.read()

        # check if cover is large enough for the message
        if len(cover_text) < len(message):
            print("Error: Cover file is not large enough to hide the message.")
            sys.exit()

        # choose appropriate algorithm
        if int(sys.argv[2]) == 1:
            # add a space at the end of each line for each bit of the message
            new_cover = ""
            for line, bit in zip(cover_text.splitlines(), message):
                new_cover += line + " " if bit == "1" else line
            # write modified cover to watermark.html
            with open("watermark.html", "w") as f:
                f.write(new_cover)
        elif int(sys.argv[2]) == 2:
            # replace single or double spaces with a space or a tab for each bit of the message
            new_cover = ""
            i = 0
            for c in cover_text:
                if c == " ":
                    new_cover += " " if message[i] == "1" else "\t"
                    i += 1
                    if i == len(message):
                        break
                else:
                    new_cover += c
            # write modified cover to watermark.html
            with open("watermark.html", "w") as f:
                f.write(new_cover)
        elif int(sys.argv[2]) == 3:
            # add errors in attribute names for each bit of the message
            new_cover = ""
            i = 0
            for c in cover_text:
                if c == "margin-bottom" or c == "line-height":
                    new_cover += "margin-botom" if message[i] == "1" else "lineheight"
                    i += 1
                    if i == len(message):
                        break
                else:
                    new_cover += c
            # write modified cover to watermark.html
            with open("watermark.html", "w") as f:
                f.write(new_cover)
        elif int(sys.argv[2]) == 4:
            # add unnecessary tag sequences for each bit of the message
            new_cover = ""
            i = 0
            for c in cover_text:
                if c == "<font>":
                    new_cover += "<font></font><font>" if message[i] == "1" else "<font>"
                    i += 1
                    if i == len(message):
                        break
                else:
                    new_

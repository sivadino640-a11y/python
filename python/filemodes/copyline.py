with open("data.txt","r") as data_txt:
    with open("d1.txt","w") as d1_txt:
        for line in data_txt:
            d1_txt.write(line)
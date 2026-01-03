a="Hello friend\n\tI am \"Sandip\" \'kushwaha\'"
print(a)

name = "Sandip"
#1 Length
print(len(name))
#2 Startswith
print(name.startswith("Sa"))
print(name.startswith("ip"))

#3 Endswith
print(name.endswith("ip"))
print(name.endswith("ips"))
#4 Upper/Lower
print(name.upper())
print(name.lower())
#5 Strip
name="  Sandip kushwaha"
print(name.strip())
#6 Split
name="Sandip kushwaha"
print(name.split())
#7 Find/index
print(name.find("kushwaha"))
print(name.index("Sandip"))
#8 Join
print('*'.join(['san', 'dip']))
#9 Replace 
print(name.replace("di", "Dee"))
#10 Format
print("Name: {}, Age: {}".format("Samdip", 20))
#11 Capitalizer
name="ram"
print(name.capitalize())
#12 Count
name="sandip kushwaha"
print(name.count("a"))
#13 Title
print(name.title())
#14 ljust/rjust
print(name.ljust(20,'-'))
print(name.rjust(20,'-'))
#15 Formatted String Literals(f-strings)
name="sandip"
print(f"{name}, Kushwaha")
print(f"Hello, {name}!")
#16 Translate(str.translate())
trans_table = str.maketrans("abcde", "12345")
print("Sandip".translate(trans_table))

#17 Partition
print("sandipkushwaha".partition('k'))
#18 in Keyword
print("sandip" in "sandipkushwaha")
print("sandip" in "kushwaha")
ჯამი = 0

with open("output.txt", "w", encoding="utf-8") as out:
    for i in range(500, 1001):
        out.write(str(i) + "\n")
        ჯამი += i
    
    out.write(str(ჯამი) + "\n")
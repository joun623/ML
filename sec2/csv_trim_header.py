in_file = "data/data.csv"
out_file = "data/kion10y.csv"

with open(in_file, "rt", encoding="Shift_JIS") as fr:
    lines = fr.readlines()


lines = ["nen,tuki,hi,kion,hinsitu,kinsitu\n"] + lines[5:]
lines = map(lambda v: v.replace("/", ","), lines)
result = "".join(lines).strip()
print(result)

with open(out_file, "wt", encoding="utf-8") as tw:
    tw.write(result)
    print("saved.")



import re

valid = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

# present = set()
# num_valid = 0
# for line in open("04-input.txt"):
#     line = line.rstrip()
#     if line == "":
#         if valid.issubset(present):
#             num_valid += 1
#         present = set()
#     pieces = line.split()
#     fields = [piece.split(":")[0] for piece in pieces]
#     for field in fields:
#         present.add(field)
# if valid.issubset(present):
#     num_valid += 1
# print(num_valid)


present = set()
num_valid = 0
for line in open("in.txt"):
    line = line.rstrip()
    if line == "":
        if valid.issubset(present):
            num_valid += 1
        present = set()
    pieces = line.split()
    fields = [piece.split(":")[0] for piece in pieces]
    values = [piece.split(":")[1] for piece in pieces]
    for field, value in zip(fields, values):
        if field == "byr" and len(value) == 4 and (1920 <= int(value) <= 2002):
            present.add(field)
        elif field == "iyr" and len(value) == 4 and (2010 <= int(value) <= 2020):
            present.add(field)
        elif field == "eyr" and len(value) == 4 and (2020 <= int(value) <= 2030):
            present.add(field)
        elif field == "hgt":
            if value.endswith("cm") and (150 <= int(value[0:-2]) <= 193):
                present.add(field)
            elif value.endswith("in") and (59 <= int(value[0:-2]) <= 76):
                present.add(field)
        elif field == "hcl" and re.match(r"^#[0-9a-f]{6}$", value):
            present.add(field)
        elif field == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            present.add(field)
        elif field == "pid" and re.match(r"^\d{9}$", value):
            present.add(field)
if valid.issubset(present):
    num_valid += 1
print(num_valid)
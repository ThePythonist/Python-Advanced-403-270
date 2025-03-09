import random

farsi = ['ا', 'ب', 'پ', 'ت', 'ث', 'ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ',
         'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'و', 'ه', 'ی']

english = "abcdefghijklmnopqrstuvwxyz"

pelak = ""
for i in range(3):
    pelak += str(random.randint(0, 9))

pelak += random.choice(farsi)

for i in range(2):
    pelak += str(random.randint(0, 9))

tehran = ["44", "99", "10", "50", "66"]

print(pelak + "|" + random.choice(tehran))

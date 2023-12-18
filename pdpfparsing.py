
import re
from PyPDF2 import PdfReader

text = ""

reader = PdfReader("media/mpdf.pdf")
for page in reader.pages:
    text += page.extract_text()

# obj olish

result = re.search(r'Pasport: (\w+) (\d+)', text)
univer = re.findall(r'^(?:\d+|)(.+?(?:universiteti|instituti|akademiyasi))', text, re.M | re.I)
yun = re.findall(r'(universiteti|instituti)\n(\S.*)', text, re.M)
fio = re.search(r'F.I.Sh.:(\w+) (\w+)\n(\S.*)', text)
t_turi = re.search(r"Ta'lim shakli: (\w+)", text)
t_tili = re.search(r"Ta'lim tili: (\w)'(\w+)", text)


# print qilish ishlari
print("F.I.O: ", fio.group(1), fio.group(2), fio.group(3))
if result:
    p_seria = result.group(1)
    p_s_raqami = result.group(2)
    print("Pasport seriya:", p_seria)
    print("Pasport raqami:", p_s_raqami)
else:
    print("Pasport raqami topilmadi.")

if t_tili.group(2):
    print("Ta'lim shakli: ", t_turi.group(1), "Ta'lim tili: ", f"{t_tili.group(1)}'{t_tili.group(2)}")
else:
    print("Ta'lim shakli: ", t_turi.group(1), "Ta'lim tili: ", f"{t_tili.group(1)}")

if univer and yun:
    print("1 - Unversitet: ", univer[0] + " ", yun[0][1])
    print("2 - Unversitet: ", univer[1] + " ", yun[1][1])
    print("3 - Unversitet: ", univer[2] + " ", yun[2][1])
    print("4 - Unversitet: ", univer[3] + " ", yun[3][1])
    print("5 - Unversitet: ", univer[4] + " ", yun[4][1])
# print(text)

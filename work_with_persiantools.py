# from persiantools.jdatetime import JalaliDateTime
#
# now = JalaliDateTime.now()
# weekday = now.strftime("%A")
# print(weekday)

# =============================================================

from persiantools import characters, digits

en = "0987654321"
per = digits.en_to_fa(en)
print("English to Persian :", per)

ar = "٠٩٨٧٦٥٤٣٢١"
per = digits.ar_to_fa(ar)
print("Arabic to Persian :", per)

ar = digits.fa_to_ar(per)
print("Persian to Arabic :", ar)

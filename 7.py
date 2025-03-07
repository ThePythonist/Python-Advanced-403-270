# import jdatetime
# import locale
#
# locale.setlocale(locale.LC_ALL, jdatetime.FA_LOCALE)
# now = jdatetime.datetime.now()
# print(now.strftime("%A"))

from persiantools.jdatetime import JalaliDateTime

now = JalaliDateTime.now()
weekday = now.strftime("%A")
print(weekday)

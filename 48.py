header = input("Enter header : ")
par = input("Enter paragraph : ")

html = f"""
<h1>{header}</h1>
<p>{par}</p>
"""

open("Output.html", "w").write(html)
print('Done')
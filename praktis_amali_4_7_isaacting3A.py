# Pengiraan isipadu kuboid
pi=3.142
def kira_kuboid(a, b, c) : # function
    isipadu_kuboid = a * b * c
    return isipadu_kuboid
    
def kuboid() : # Procedure
    tinggi = float(input("Masukkan tinggi : "))
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar : "))
    print("Isipadu kuboid = ", kira_kuboid(tinggi, panjang, lebar))

def kira_silinder(a, b) : # function
    isipadu_silinder =pi*a**2*b
    return isipadu_silinder

def silinder() :
    jejari=int(input("Masukkan jejari:"))
    tinggi= int(input("Masukkan tinggi:"))
    print("Isipadu silinder = " , kira_silinder(jejari,tinggi))

def kira_kon(a,b) :
    isipadu_kon =1/3*pi*a**2*b
    return isipadu_kon

def kon() :
    jejari=int(input("Masukkan jejari:"))
    tinggi= int(input("Masukkan tinggi:"))
    print("Isipadu kon = " , kira_kon(jejari,tinggi))

def  kira_sfera(a) :
    isipadu_sfera=(4/3)*pi*(a**3)
    return isipadu_sfera

def sfera() :
    jejari=int(input("Masukkan jejari:"))
    print("Isipadu sfera =" , kira_sfera(jejari))

def repeat():
    print("*********************************** \n         Menu Mengira Isi Padu \n***********************************")
    print("1.Kuboid")
    print(" 2.Silinder")
    print(" 3.Kon")
    print(" 4.Sfera")
    print(" 5.Tamat Progam")
    print("***********************************")
    print("Masukkan pilihan anda: [1-4] :")

    noPilihan=int(input("Sila masukkan nopilihan anda:"))

    if noPilihan ==1:
        kuboid()
    elif noPilihan==2:
        silinder()
    elif noPilihan==3:
        kon()
    elif noPilihan==4:    
        sfera()
    else:
        print("Terima kasih kerana menggunakan saya")

ulang="y"
while ulang=="y":
    repeat()
    ulang=str(input("Mahu kira lagi? Tekan [y] atau [t]:"))
print("Terima kasih kerana menggunakan saya")





    
    
    


    


    
          
    

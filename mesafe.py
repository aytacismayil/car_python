user = input("Masinin kateqoriyasini daxil edin: ")
ilkin_gosterici = int(input("ILkin gostericini qeyd edin: "))
son_gosterici = int(input("Son gostericini qeyd edin: "))
gunlerin_sayi = int(input("Gunlerin sayini qeyd edin: "))

her_gun = 0
surulen_mil = son_gosterici-ilkin_gosterici
elave = 0
heftelik = 0 
borc = 0

if user =="b":
    borc=(gunlerin_sayi*40)+(surulen_mil*0.25)
if user == "d":
    borc=gunlerin_sayi*60
    if surulen_mil>100:
        borc+=surulen_mil*0.25
if user =="w":
    if surulen_mil<=900:
        borc=190
    elif surulen_mil>900 and surulen_mil<=1500:
        borc=100
    else:
        borc+=200+(surulen_mil-1500)*0.25
        
print("surulen_mil",surulen_mil)
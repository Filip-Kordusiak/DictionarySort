startt = 'large-images: '
stopp = ';" href="'
String = "$#$!@$%; large-images: https://########.###.###/#########/44nqw7zabr/jpeg/87662728_R01_C14.jpg?w=1824&h=1026&keep=c&crop=false#large @#!$@!#$#@!$#@$@# "
String2 = ';" href="https://########.####.###/content/0ewmvg67be/jpeg/84414466_R01_C01.jpg?w=1824&amp;h=1026&amp;keep=c&amp;crop=false#large" id="spin-1" style="user-select: none; -webkit-tap-highlight-color: transparent;"><img src="https://########.####.##/content/0ewmvg67be/jpeg/84414466_R01_C01.jpg?w=510&amp;h=287&amp;keep=c&amp;crop=false#small"/>'
String4 = ';" href="https://########.####.###/content/0ewmvg67be/jpeg/84414466_R01_C01.jpg?w=1824&amp;h=1026&amp;keep=c&amp;crop=false#large" id="spin-1" style="user-select: none; -webkit-tap-highlight-color: transparent;"><img src="https://########.####.##/content/0ewmvg67be/jpeg/84414466_R01_C01.jpg?w=510&amp;h=287&amp;keep=c&amp;crop=false#small"/>'

String2=String2[String2.find(startt)+14:String2.rfind(stopp)]
print(String2)
String69 = String2.split()
print('Separeted', len(String69), String69)
### tutaj podział na R radius
R1 = ''
R2 = ''
R2list = list()
R1list = list()
for item in String69:
    zmienna_pomocnicza = item
    zmienna_pomocnicza = zmienna_pomocnicza[zmienna_pomocnicza.find('_R')+3:zmienna_pomocnicza.rfind('_C')]
    #print(zmienna_pomocnicza)
    if zmienna_pomocnicza == '1':
        #print("dodajemy do folderu nr 1")
        R1list.append(item)
    elif zmienna_pomocnicza == '2':
        #print("dodajemy do folderu nr 2")
        R2list.append(item)
    else:
        print("inny kąt")
R1Dict = {}
for item1 in R1list:
    zmienna_pomocnicza = item1
    zmienna_pomocnicza = zmienna_pomocnicza[zmienna_pomocnicza.find('_C') + 2:zmienna_pomocnicza.rfind('.jpg')]
    print(int(zmienna_pomocnicza), item1)
    R1Dict.update({zmienna_pomocnicza: item1})
R2Dict = {}
for item2 in R2list:
    zmienna_pomocnicza = item2
    zmienna_pomocnicza = zmienna_pomocnicza[zmienna_pomocnicza.find('_C') + 2:zmienna_pomocnicza.rfind('.jpg')]
    print(int(zmienna_pomocnicza), item2)
    R2Dict.update({zmienna_pomocnicza: item2})


print("dicssss: ", sorted(R1Dict.items()))
print("dicssss: ", sorted(R2Dict.items()))


#link1 = 'https://########.####.###/content/44nqw7zabr/jpeg/87662728_R01_C14.jpg?w=1824&h=1026&keep=c&crop=false#large'
#link = 'https://########.####.###/content/44nqw7zabr/jpeg/87662728_R01_C14.jpg?w=1824&h=1026&keep=c&crop=false#large'
#start1 = 'https'
#stop2 = '.jpg'
#
#link = link[link.find(start1)+66:link.rfind(stop2)]
##print(link)
#do_podz = {}
#do_podz.update({int(link): link1})
#do_podz.update({15: '15'})
#do_podz.update({1: '1'})
##print(sorted(do_podz.items()))
#
#print("pierwsza lista :", R1list)
#print("druga lista :", R2list)

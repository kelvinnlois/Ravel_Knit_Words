## Exam Modul I, 16 Feb 2021
## Kelvin Lois

# Soal 3

# Fungsi Ravel
def ravel(kata):
    rav = ''
    for i in range(len(kata)+1):
        rav = rav + kata[0:i]
    return rav

# Penggunaan Fungsi Ravel
print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))

print("")


# Fungsi Knit
import math
def knit(kata):
    H = len(kata)
    panjang = int((-1 + math.sqrt(1+8*H))/2)
    return(kata[-panjang:H])

# Penggunaan Fungsi Knit
print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))



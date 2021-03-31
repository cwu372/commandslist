#coding:utf-8
import string
filesname=raw_input("input file name, \nand it will be part of \n the outputname:")
f = open(filesname, 'r')
matchedlen = 30
mcccode='373232' #country code of customer environment

possible_zz = [134,135,136,137,138,139,147,150,151,152,157,158,159,178,182,183,184,187,188]   #important possible segment, please modify it every time for different location
result = []
finalresult = []
numbers = ''
number_tmp = ''
for line in f.readlines():
    if not mcccode in line :
        continue
    start = 0
    while True:
        index = line.find(mcccode, start)
        if index == -1:
            break;
        numbers = line[index:(index+matchedlen)]
        if numbers != number_tmp:
            result.append(numbers)
        start = index + 1
        number_tmp = numbers
finalresult  = list(set(result))
f.close()


'''Attempt to perform strict checking on final list result per possible number segments,
if you don't have such information, please comment this segment'''
##cc = ''
##transfered_possible=[]
##for zz in possible_zz:
##    cc = str(zz)
##    dd = ''
##    for z in cc:
##        cn = '3' + z
##        dd = dd + cn
##    transfered_possible.append(dd)
##
##for final in finalresult:
##    for transfer in transfered_possible:
##        findcnt = 0 
##        if transfer in final:
##            findcnt = findcnt + 1
##    if (findcnt == 0):
##        finalresult.remove(final)

'''Output one list containing user numbers in ASCII coding format'''
filesname_output='users_numbers_ascii_' + filesname
f = open(filesname_output, 'w')
for numbers in finalresult:
    number = ''
    Sepnumberlist = []
    for i in range(0,len(numbers)):
        if (ord(numbers[i])<48):
            number = ''
            Sepnumberlist = []
            break
        if (ord(numbers[i])>57):
            number = ''
            Sepnumberlist = []
            break
        Sepnumberlist.append(numbers[i])
        number = ''.join(Sepnumberlist)
    if len(number)>0:
        f.write(number)
        f.write('\n')    
f.close()

'''Output one list containing normal human user numbers'''
filesname_output='users_numbers_human_' + filesname
f = open(filesname_output, 'w')
for numbers in finalresult:
    number = ''
    Sepnumberlist = []
    for i in range(1,len(numbers),2):
        if (ord(numbers[i])<48):
            number = ''
            Sepnumberlist = []
            break
        if (ord(numbers[i])>57):
            number = ''
            Sepnumberlist = []
            break
        Sepnumberlist.append(numbers[i])
        number = ''.join(Sepnumberlist)
    if len(number)>0:
        f.write(number)
        f.write('\n')    
f.close()

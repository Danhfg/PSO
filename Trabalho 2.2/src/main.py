from os import system

cmdMemInfo = "grep 'MemTotal\|MemFree\|Cached\|SwapTotal\|SwapFree' /proc/meminfo > memInfo.dat" 

system(cmdMemInfo)

arqMemInfo = open("memInfo.dat", 'r')
conteudoArqMemInfo = arqMemInfo.readlines()

memInfo = [{'MemTotal': "0"}, {'MemFree': "0"}, {'Cached': "0"}, {'SwapTotal': "0"}, {'SwapFree':"0"}]


memInfo[1]= conteudoArqMemInfo[1].strip()
memInfo[2] = conteudoArqMemInfo[2].strip()
memInfo[3] = conteudoArqMemInfo[3].strip()

print( memInfo )  

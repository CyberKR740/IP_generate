#!/usr/bin/evn python3
# encoding: utf-8
#
#
#  [Author] Zwdeff <santosandradeemerson0@gmail.com>
#
#
#  [Program] criipar IPs Numbers Generate v1.2
#  [Telegram - Channel] t.me/joinchat/AAAAAEANZwsT9F2Y-aBVIQ
#  [Telegram - Privado] @nZwdeff
#  [copyright] Copyright © 2017 All Rights Reserved @nZwdeff
#
#  [Info]
#    Github https://github.com/GMagNLL/criipa ...
#    This script generates IP numbers. To generate a specific IP range, set the ..
#    maximum number to which it should generate. To block an octet Repeat the number ..
#    to be blocked at the maximum number. The generated IPs are saved in the file created ..
#    at the beginning of the program.
#  
#  [License]
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

__author__ = 'Zwdeff'
__version__ = '1.2'

from sys import *
from time import *

if version_info < (3, 0):
   print('\033[91mError: Sorry, criipar requires Python 3.x.\033[m')
   sleep(2)
   exit()

n0 = '\033[90m'
n1 = '\033[91m'
n2 = '\033[92m'
n3 = '\033[93m'
n4 = '\033[94m'
n5 = '\033[95m'
n6 = '\033[96m'
n7 = '\033[97m'

__Banner__ = '''
  ____      _ ___ ____
 / ___|_ __(_)_ _|  _ \ __ _ _ __
| |   | '__| || || |_) / _` | '__|
| |___| |  | || ||  __/ (_| | |
 \____|_|  |_|___|_|   \__,_|_|

 Generate custom IPs Numbers _\n'''

__main__ = n2+'   1) =\033[92m XXX.XXX.XXX.XXX\n'\
          +'   0) = Exit\n\033[m'

print(n2+' %s\033[m' %(__Banner__))
print(n2+' |--- :'+n7+' Author\033[32m  :\033[32m %s\033[m' %(__author__))
print(n2+' |--- :'+n7+' Version\033[32m :\033[32m %s\033[m' %(__version__))
print(n2+' |--- :'+n7+' Channel\033[32m :\033[32m AAAAAEANZwsT9F2Y-aBVIQ\033[m')
print(n2+' |--- :'+n7+' Github\033[32m  :\033[32m https://github.com/GMagNLL\033[m\n')

print(n2+'%s' %(__main__))

def case():
  try:
     w = input(n2+'[criipar] :: _ \033[m')
     while w != '01' or w != '1'or w != '00' or w != '0':
        if w == '01' or w == '1' or w == '00' or w == '0':
           if w == '01' or w == '1':
              def gerator(s1,s2,s3,s4,o1,o2,o3,o4,arq,pho):
                  for a in range(s1, o1+1):
                   for b in range(s2, o2+1):
                    for c in range(s3, o3+1):
                     for d in range(s4, o4+1):
                         arq.write(str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+str(pho)+'\n')
                         print(n2+' '+str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+str(pho)\
                         +'\033[m')
                         if a == o1 and b == o2 and c == o3 and d == o4:
                            print(n2+'\n\033[32mCompleted. IPs saved in file %s\033[m'\
                            %(arq.name))
                            sleep(2)
                            arq.close()
                            print('\n'), case()
                            
              print(n2+'\n[:] Create a file .. \033[m')
              sleep(2)
              arq = open(input(n2+'[+] Name for file :: _ \033[m')+ '.txt', 'w')
              def retu(s1,s2,s3,s4,arq):
                  o1 = input(n2+'\nMaximum octet number 1. %s/255 :: _ \033[m' %(s1))
                  try:
                     o1 = int(o1)
                     if o1 < s1:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  o2 = input(n2+'Maximum octet number 2. %s/255 :: _ \033[m' %(s2))
                  try:
                     o2 = int(o2)
                     if o2 < s2:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  o3 = input(n2+'Maximum octet number 3. %s/255 :: _ \033[m' %(s3))
                  try:
                     o3 = int(o3)
                     if o3 < s3:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  o4 = input(n2+'Maximum octet number 4. %s/255 :: _ \033[m' %(s4))
                  try:
                     o4 = int(o4)
                     if o4 < s4:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,arq)
                  pho = input(n2+'[+] Port for IPs :80/:8080 :: _ \033[m')
                        
                  print(n2+'\nGenerating IPs in file %s .. \n\033[m' %(arq.name))
                  sleep(2)
                  gerator(s1,s2,s3,s4,o1,o2,o3,o4,arq,pho)
                  
              def defe(arq):
                  s1 = input(n2+'\nIP octet 1. 1/255 :: _ \033[m')
                  try:
                     s1 = int(s1)
                     if s1 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                  except Exception:
                    print(n1+'Error: Use only integer numbers.\033[m')
                    defe(arq)
                  s2 = input(n2+'IP octet 2. 0/255 :: _ \033[m')
                  try:
                     s2 = int(s2)
                     if s2 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                        defe(arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     defe(arq)
                  s3 = input(n2+'IP octet 3. 0/255 :: _ \033[m')
                  try:
                     s3 = int(s3)
                     if s3 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                        defe(arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     defe(arq)
                  s4 = input(n2+'IP octet 4. 0/255 :: _ \033[m')
                  try:
                     s4 = int(s4)
                     if s4 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                        defe(arq)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     defe(arq)
                  retu(s1,s2,s3,s4,arq)
                  
              if __name__ == '__main__':
                 defe(arq)
           if w == '0' or w == '00':
              print(n1+'Going out ..\033[m')
              sleep(2)
              exit()
        else:
           w = input(n2+'[criipar] :: _ \033[m')
  except KeyboardInterrupt:
     print(n1+'\nGoing out ..\033[m')
     sleep(2)
     exit()
if __name__ == '__main__':
   case()

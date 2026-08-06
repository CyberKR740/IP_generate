#!/usr/bin/evn python3
# encoding: utf-8
#
#  [Programa] criipar IPs Numbers Generate v1.2
#  [Privado - Machine] @SeichMachine740
#  [copyright] Copyright © 2017
#
# This script generates IP addresses.
# To generate a specific IP range, set
# the maximum number
# up to which it should be generated.
# To block an octet, repeat the
# number to be blocked at
# the maximum number.
# The generated IPs are saved in
# the created file.
#
#  [License]
#    Licensed under the Apache
#    License Version 2.0 (the "License") you may
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
__version__ = 'v0.4'

import os
import sys
import time
import random

if sys.version_info < (3, 0):
   print('\033[91mError: Sorry, criipar requires Python 3.x.\033[m')
   time.sleep(2)
   exit()

n0 = '\033[m'
n1 = '\033[91m'
n2 = '\033[92m'
n3 = '\033[93m'
n4 = '\033[94m'
n5 = '\033[95m'
n6 = '\033[96m'
n7 = '\033[97m'

title = """Programa para criar uma lista comum de numeros IPs.
sem ordem aleatoria e, sem categoria 255, definida.
Nome: Generate custom IPs Numbers.\n"""
def DelCase_homeGOG():
    __main__ = n2+'   1) =\033[92m XXX.XXX.XXX.XXX\n'\
                 +'   0) = Exit\n\033[m'

    print(n7+title+"\033[m")
    print(n2+' |--- :'+n7+' Author\033[32m  :\033[32m %s\033[m' %(__author__))
    print(n2+' |--- :'+n7+' Version\033[32m :\033[32m %s\033[m' %(__version__))
    print(n2+' |--- :'+n7+' Github\033[32m  :\033[32m https://github.com/CyberKR740\033[m\n')

    print(n2+'%s' %(__main__))
sequencia = 0
def case():
  DelCase_homeGOG()
  global sequencia

  try:
     suga = input(n2+"[VERTIGO] :: _ \033[m")

     while True:
          if suga in ["1", "99"]:
              if suga == "99":
                  print(n1+"Going out ..\033[m")
                  time.sleep(1.2)
                  sys.exit()

              def gerator(s1,s2,s3,s4,o1,o2,o3,o4,sequencia,arq,pho,syet):
                  try:
                     syet = int(syet)
                  except Exception:
                     print(n1+"Error: Utilize somente numeros inteiros.\033[m")
                     defe()

                  while True:
                      sequencia = sequencia + 1

                      a = random.randint(s1, o1)
                      b = random.randint(s2, o2)
                      c = random.randint(s3, o3)
                      d = random.randint(s4, o4)

                      arq.write(f'{a}.{b}.{c}.{d}:{pho}\n')
                      print(f"\033[1;32m{a}.{b}.{c}.{d}:{pho}\033[m")

                      if sequencia == int(syet):
                          print(f"\033[1;32mCompleted. IPs saved in file: {arq.name}\033[m\n")
                          time.sleep(0.4)
                          arq.close()
                          caco = input("Pressione Enther para ir in home.")
                          os.system("clear")
                          case()

              def retu(s1,s2,s3,s4,sequencia):
                  o1 = input(n2+'\nMaximum octet number 1. %s/255 :: _ \033[m' %(s1))
                  try:
                     o1 = int(o1)
                     if o1 < s1:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,sequencia)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,sequencia)
                  o2 = input(n2+'Maximum octet number 2. %s/255 :: _ \033[m' %(s2))
                  try:
                     o2 = int(o2)
                     if o2 < s2:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,sequencia)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,sequencia)
                  o3 = input(n2+'Maximum octet number 3. %s/255 :: _ \033[m' %(s3))
                  try:
                     o3 = int(o3)
                     if o3 < s3:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,sequencia)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,sequencia)
                  o4 = input(n2+'Maximum octet number 4. %s/255 :: _ \033[m' %(s4))
                  try:
                     o4 = int(o4)
                     if o4 < s4:
                        print(n1+'Error: The maximum number must be greater or'\
                              +' The octet.\033[m')
                        retu(s1,s2,s3,s4,sequencia)
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     retu(s1,s2,s3,s4,sequencia)

                  def inteiro_generator():
                       syet = input(n2+"Quantos IPs devem ser gerados ex: 46358 :: _ \033[m").strip()
                       try:
                           syet = int(syet)
                       except Exception as e:
                          print(e)
                          print("\033[1;91mError: Utilize somente numeros.\033[m")
                          print("\033[1;91m argumento [ex=/:/&/e/?] numeros inteiros: 46788/033[m")
                          try:
                              syet = input(n2+"Quantos IPs devem ser gerados ex: 46358 :: _ \033[m").strip()
                          except Exception:
                              print("\033[1;91mError: Utilize somente numeros.\033[m")
                              print("\033[1;91m argumento [ex=/:/&/e/?] numeros inteiros: 46788/033[m")
                              inteiro_generator()

                       pho = input(n2+"[+] Port for IPs :80/:8080 :: _ \033[m").strip()
                       try:
                           pho = int(pho)
                       except Exception as e:
                          print(e)
                          print("\033[1;91mError: Utilize simente Numeros, [N/:/&/e/?] Exemplo: 3128\033[m")
                          try:
                              pho = int(input(n2 + '[+] Port for IPs :80/:8080 :: _ \033[m'))
                          except Exception:
                             print("\033[1;91mError: Utilize somente numeros.\033[m")
                             print("\033[1;91m argumento [ex=/:/&/e/?] numeros inteiros: 46788/033[m")
                             inteiro_generator()

                       arq = open(input(n2+"[+] Name for file :: _ \033[m")+ '.txt', 'w')

                       print(n2+f"Generating IPs in file {arq.name} .. \n\033[m" )
                       time.sleep(0.9)
                       print(n2+'\n[:] Create a file .. \033[m')
                       time.sleep(1.9)

                       gerator(s1,s2,s3,s4,o1,o2,o3,o4,sequencia,arq,pho,syet)

                  inteiro_generator()

              def defe():
                  s1 = input(n2+'\nIP octet 1. 1/255 :: _ \033[m')
                  try:
                     s1 = int(s1)
                     if s1 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                  except Exception:
                    print(n1+'Error: Use only integer numbers.\033[m')
                    defe()
                  s2 = input(n2+'IP octet 2. 0/255 :: _ \033[m')
                  try:
                     s2 = int(s2)
                     if s2 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                        defe()
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     defe()
                  s3 = input(n2+'IP octet 3. 0/255 :: _ \033[m')
                  try:
                     s3 = int(s3)
                     if s3 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                        defe()
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     defe()
                  s4 = input(n2+'IP octet 4. 0/255 :: _ \033[m')
                  try:
                     s4 = int(s4)
                     if s4 > 255:
                        print(n1+'Error: The octet must be less than or equal to 255.')
                        defe()
                  except Exception:
                     print(n1+'Error: Use only integer numbers.\033[m')
                     defe()
                  retu(s1,s2,s3,s4,sequencia)

              if __name__ == '__main__':
                  defe()

          elif suga in ["0", "exit", "99"]:
              print(n1+"Going out ..\033[m")
              time.sleep(2)
              sys.exit()
          else:
              case()

  except KeyboardInterrupt:
     print(n1+"\nGoing out ..\033[m")
     time.sleep(2)
     sys.exit()
if __name__ == '__main__':
   case()

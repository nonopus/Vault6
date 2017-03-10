# Licence : AIC, can only be used by level 3 personnel. 
import os
hostname = "yahoo.co.uk" #easy hackable example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'yahoo is up enit! this means we can internet.'
else:
  print hostname, 'Did you check the board? I bet if you did you would see another level 3 is using yahoo allready, wait 20 minutes, then check the board again.'

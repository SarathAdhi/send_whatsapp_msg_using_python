import pywhatkit

mobilenum = input('Enter  the mobile number: ')
message = input('Enter the message: ')
hour = int(input('Enter the hour in 24 hour format: '))
min = int(input('Enter the minutes: '))

pywhatkit.sendwhatmsg(mobilenum, message, hour, min)     # Mobile number, message, time in 24 hour format 16:57(4:56pm)

print('\nMESSAGE SENT SUCCESSFULLY')
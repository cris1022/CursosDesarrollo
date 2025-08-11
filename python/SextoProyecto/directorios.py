import os

ruta= os.chdir('C:\\Users\\cabondano\\OneDrive - Novopayment Inc\\Documentos\\LYNK\\RSA_KEYS\\DEV\\PUBLIC')

archivo=open('jwe-public-key-24066d14-1173-4485-8087-f6fb9f706615.pem','r')

print (archivo.read())

archivo.close()
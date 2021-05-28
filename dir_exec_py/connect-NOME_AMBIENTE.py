import sys.argv

# VIA ARQUIVO COM CRIPTOGRAFIA
#configFile='/u01/app/scripts/security/NOME_DO_AMBIENTE-config-file'
#keyFile='/app/scripts/security/NOME_DO_AMBIENTE-key-file'

#USER SENHA DIRETO
try:
    connect('USER','SENHA',url='t3://10.0.0.0:7001')

except Exception, e:
    print(str(e))

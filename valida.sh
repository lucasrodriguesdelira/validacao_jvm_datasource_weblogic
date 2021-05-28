#!/bin/bash

# Diretorio de scripts
SCRIPTDIR="/u01/app/monitoracao"

#####################
# ESTADO DAS JVMS   #
# E DATASOURCES     #
#####################

# NOME DO AMBIENTE
HTMLJVM_NOME_AMBIENTE=$(/u01/app/monitoracao/monit_jvm_healt_NOME_AMBIENTE.sh | grep '<tr>')
HTMLDS_NOME_AMBIENTE=$(/u01/app/monitoracao/monit_ds_health_NOME_AMBIENTE.sh | grep '<tr>')
NOME_AMBIENTE_COUNT=$(echo ${HTMLJVM_NOME_AMBIENTE} | grep '<tr>'|wc -l)


##############
# MONTA HTML #
##############

cat << EOF
<!DOCTYPE HTML>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                text-align:center;
                font-family: verdana, courier, lucida;
                font-size:12px;
            }            
            h2 {
                font-size:14px;
                color:red;
                text-decoration:underline;
            }
            table,th,td {
                border:1px solid black;
            }
        </style>
        <title> VALIDAÇÃO | WEBLOGIC </title>
    </head>

    <body>

        <!-- AMBIENTE: NOME DO AMBIENTE -->
        <h1> ARP948VLNCAP - Oracle OSB </h1>
        <h2>$(date +"%d/%m/%Y - %H:%M") - ESTADO JVMs</h2>
        <table align="center" CELLPADDING=2 CELLSPACING=0>
            ${HTMLJVM_NOME_AMBIENTE}
        </table>
        <h2>$(date +"%d/%m/%Y - %H:%M") - ESTADO DATASOURCES</h2>
        <table align="center" CELLPADDING=2 CELLSPACING=0>
            ${HTMLDS_NOME_AMBIENTE}
        </table><br><br>

    </body>
</html>
EOF

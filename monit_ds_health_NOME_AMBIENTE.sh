#!/bin/bash

parm=$*

d_dominio=/u01/oracle/Middleware/Oracle_Home/wlserver/server
d_scripts=/u01/app/monitoracao/dir_exec_py

# Configurar variaveis de ambiente
. ${d_dominio}/bin/setWLSEnv.sh

filename=`basename $0`
scriptname=${filename%.*}

# Chama wlst e python
java weblogic.WLST ${d_scripts}/${scriptname}.py ${parm}

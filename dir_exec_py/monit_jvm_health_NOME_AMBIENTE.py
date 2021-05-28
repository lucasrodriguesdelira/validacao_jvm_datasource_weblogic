execfile('/u01/app/monitoracao/dir_exec_py/connect-NOME_AMBIENTE.py')

serverNames = cmo.getServers()
servers = cmo.getServers()

serverAndMachines = {'': ''}
for server in servers:
  cd('/Servers/' + server.getName())
  serverName = server.getName()
  machine = cmo.getMachine()
  # if it's not null
  if machine:
    machineName = machine.getName()
  else:
    machineName = '-'
  serverAndMachines[serverName] = machineName

domainRuntime()

print '<tr><th>JVM</th><th>SERVIDOR</th><th>ESTADO</th><th>HEALTH</th><th>HOGGING THREADS</th>'

for name in serverNames:
  try:
    v_server = serverAndMachines[name.getName()]

    if v_server == '-' and name.getName() != 'AdminServer':
      v_state = 'INNACTIVE'
      v_server = ' - '
      v_health = 'N/A'
      v_hogg_html = '<td bgcolor="yellow">N/A</td></tr>'
      print '<tr><th>' + name.getName() + '</th><th>' + v_server + '</td><td bgcolor="yellow">' + v_state + '</td><td bgcolor="yellow">' + v_health + '</td>' + v_hogg_html
      continue

    cd('/ServerRuntimes/' + name.getName())

    v_state = str(get('State'))

    if v_state != '':
      v_health = str(get('HealthState'))
      v_health = v_health.split(':')[2].split(',')[0].split('_')[1]
    else:
      v_health = 'INDISPONIVEL'

    cd('/ServerRuntimes/'+name.getName()+'/ThreadPoolRuntime/ThreadPoolRuntime')
    v_hogging = str(get('HoggingThreadCount'))

    if int(v_hogging) < 10:
      v_hogg_html = '<td bgcolor="green">' + v_hogging + '</td></tr>'
    else:
      v_hogg_html = '<td bgcolor="red">' + v_hogging + '</td></tr>'

    if v_state == 'RUNNING':
      if v_health == 'OK':
        print '<tr><th>' + name.getName() + '</th><th>' + v_server + '</td><td bgcolor="green">' + v_state + '</td><td bgcolor="green">' + v_health + '</td>' + v_hogg_html
      else:
        print '<tr><th>' + name.getName() + '</th><th>' + v_server + '</td><td bgcolor="green">' + v_state + '</td><td bgcolor="red">' + v_health + '</td>' + v_hogg_html
    else:
      print '<tr><th>' + name.getName() + '</th><th>' + v_server + '</td><td bgcolor="green">' + v_state + '</td><td bgcolor="red">' + v_health + '</td>' + v_hogg_html
  except:
   v_state = 'STOPPED'
   v_health = 'N/A'
   v_hogg_html = '<td bgcolor="red">N/A</td></tr>'
   print '<tr><th>' + name.getName() + '</th><th>' + v_server + '</td><td bgcolor="red">' + v_state + '</td><td bgcolor="red">' + v_health + '</td>' + v_hogg_html
  continue

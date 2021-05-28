execfile('/u01/app/monitoracao/dir_exec_py/connect-NOME_AMBIENTE.py')

serverNames = cmo.getServers()

domainRuntime()

print '<tr><th>JVM</th><th>DATASOURCE</th><th>ESTADO</th><th>TESTE</th>'

for name in serverNames:
  ds_state = 'Stopped'
  try:
    cd('/ServerRuntimes/' + name.getName())

    dsMBeans = cmo.getJDBCServiceRuntime().getJDBCDataSourceRuntimeMBeans()

    for ds in dsMBeans:
      ds_name = ds.getName()
      ds_state = ds.getState()


      if ds_state == 'Running':
        ds_pool = ds.testPool()
        if ds_pool is None:
          print '<tr><th>' + name.getName() + '</th><th>' + ds_name + '</th><td bgcolor="green">' + ds_state + '</td><td bgcolor="green">OK</td></tr>'
        else:
          print '<tr><th>' + name.getName() + '</th><th>' + ds_name + '</th><td bgcolor="green">' + ds_state + '</td><td bgcolor="red">NOK</td></tr>'
      else:
        print '<tr><th>' + name.getName() + '</th><th>' + ds_name + '</th><td bgcolor="red">' + ds_state + '</td><td bgcolor="red">NOK</td></tr>'
  except Exception, e:
    print(e)

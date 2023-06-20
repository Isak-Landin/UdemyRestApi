from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from pathlib import Path

from App_Config.app_config import client_secret, client_id


my_path = Path().resolve()
path_of_secure_zip = str(my_path.parent) + '\\' + 'App_Config\\secure-connect-udemy.zip'

print(my_path)

cloud_config = {
  'secure_connect_bundle': path_of_secure_zip
}
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute().one()
if row:
  print(row[0])
else:
  print("An error occurred.")
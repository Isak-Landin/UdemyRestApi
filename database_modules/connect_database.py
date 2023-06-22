import sys

from cassandra.datastax.cloud import DriverException
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import cassandra
from pathlib import Path

from App_Config.app_config import client_secret, client_id
from localconfig import table_users, table_items, table_stores, keyspace
from server_stability import ServerStatus


class DataStaxConnection:
    def __init__(self):
        self.session: cassandra.cluster.Session = None
        self.cluster: Cluster = None
        self.keyspace: str = keyspace
        self.table_users: str = table_users
        self.table_stores: str = table_stores
        self.table_items: str = table_items

    def start_up(self):
        self.initialize_connection()

    def reboot_connection(self):
        self.initialize_connection(reboot=True)

    def initialize_connection(self, reboot=False):
        try:
            my_path = Path().resolve()
            path_of_secure_zip = str(my_path.parent) + '\\' + 'App_Config\\secure-connect-udemy.zip'
            cloud_config = {
                'secure_connect_bundle': path_of_secure_zip
            }

            auth_provider = PlainTextAuthProvider(client_id, client_secret)
            self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            if not self.cluster:
                raise ConnectionFaulty(self)
            try:
                self.session = self.cluster.connect()
                if self.session is None or self.cluster is None:
                    raise DriverException()
            except (DriverException, Exception) as e:
                if reboot:
                    ServerStatus.datastax_connection_set_unstable()
                else:
                    raise ConnectionFaulty(self) from e
        except (DriverException, ConnectionError) as e:
            self.session = None
            if reboot:
                ServerStatus.datastax_connection_set_unstable()
            else:
                raise ConnectionFaulty(self) from e


class ConnectionFaulty(Exception):
    def __init__(self, instanced_datastax_object: DataStaxConnection):
        instanced_datastax_object.reboot_connection()

    # Todo, as stated by a previous comment in the DataStaxConnection module,
    #  implement a module that keeps track of successful launches and failed launched.
    #  Potentially make it a requirement to run that module before any route return

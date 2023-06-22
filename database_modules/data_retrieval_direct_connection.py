from database_modules.connect_database import DataStaxConnection, ConnectionFaulty
from database_modules.localconfig import table_stores, table_users, table_items, keyspace


class DatastaxDataRetrieval:
    def __init__(self, datastax_connection: DataStaxConnection):
        self.connection_object = datastax_connection

    def retrieve_all_items(self):
        query = f'SELECT * FROM {keyspace}.{table_items}'
        item_rows = None

        try:
            if self.connection_object.session:
                item_rows = self.connection_object.session.execute(query)
            elif self.connection_object.session is None and self.connection_object.cluster:
                self.connection_object.session = self.connection_object.cluster.connect()
                item_rows = self.connection_object.session.execute(query)
            else:
                raise ConnectionFaulty(self.connection_object)
        except Exception as e:
            raise ConnectionFaulty(self.connection_object) from e

    def retrieve_all_items_in_store(self, store: str):
        query = f'SELECT * FROM {keyspace}.{table_items} WHERE store = {store}'
        item_rows = None

        try:
            if self.connection_object.session:
                item_rows = self.connection_object.session.execute(query)
            elif self.connection_object.session is None and self.connection_object.cluster:
                self.connection_object.session = self.connection_object.cluster.connect()
                item_rows = self.connection_object.session.execute(query)
            else:
                raise ConnectionFaulty(self.connection_object)
        except Exception as e:
            raise ConnectionFaulty(self.connection_object) from e

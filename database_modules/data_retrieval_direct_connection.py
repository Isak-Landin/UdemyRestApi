from database_modules.connect_database import DataStaxConnection, ConnectionFaulty
from database_modules.localconfig import table_stores, table_users, table_items, keyspace
from cassandra.cluster import ResultSet


class DatastaxDataRetrieval:
    def __init__(self, datastax_connection: DataStaxConnection):
        """
        :param datastax_connection:
        :type: DataStaxConnection:
        """
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
                print('Raising exception')
                raise ConnectionFaulty(self.connection_object)
        except Exception as e:
            raise ConnectionFaulty(self.connection_object) from e

        if item_rows:
            return item_rows

    def retrieve_all_items_in_store(self, store: str) -> ResultSet:
        """

        :param store:
        :type: str:
        :return: ResultSet:
        """
        query = f"SELECT * FROM {keyspace}.{table_items} WHERE store = '{store}' ALLOW FILTERING"
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
            print(e.__str__())
            raise ConnectionFaulty(self.connection_object) from e

        if item_rows:
            return item_rows

    @staticmethod
    def convert_cassandra_row_or_cluster_to_json(cluster=None, single_row=None):
        """
        Pick one to work with, either cluster or single_row.
        Never both
        :param cluster:
        :param single_row:
        :return:
        """

        def convert_to_json():
            """_columns = get_columns()
            if _columns:
                _columns_max_index = len(_columns) - 1"""

            dict_key_values_from_row_or_cluster = {}

            if cluster and not single_row:

                for row in cluster:
                    row_as_dict = row._asdict()

                    dict_key_values_from_row_or_cluster = {**dict_key_values_from_row_or_cluster, **row_as_dict}
            elif single_row and not cluster:
                row_as_dict = single_row._asdict()
            else:
                pass

            return dict_key_values_from_row_or_cluster

        return convert_to_json()


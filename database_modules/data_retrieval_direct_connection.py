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

    def retrieve_all_stores(self):
        query = f'SELECT * FROM {keyspace}.{table_stores}'

        return self.default_query_execution_cluster(query)

    def retrieve_store(self, store):
        query = f"SELECT * FROM {keyspace}.{table_stores} WHERE store = '{store}'"
        return self.default_query_execution_cluster(query)

    def retrieve_all_items(self):
        query = f'SELECT * FROM {keyspace}.{table_items}'

        return self.default_query_execution_cluster(query)

    def retrieve_all_items_in_store(self, store: str) -> dict:
        """

        :param store:
        :type: str:
        :return: ResultSet:
        """
        query = f"SELECT * FROM {keyspace}.{table_items} WHERE store = '{store}' ALLOW FILTERING"
        return self.default_query_execution_cluster(query)

    def default_query_execution_cluster(self, _query) -> dict:
        try:
            db_response = self.connection_object.session.execute(_query)
            if db_response.one():
                if self.connection_object.session:
                    item_cluster = DatastaxDataRetrieval.convert_cassandra_row_or_cluster_to_json(
                        db_response
                    )
                elif self.connection_object.session is None and self.connection_object.cluster:
                    self.connection_object.session = self.connection_object.cluster.connect()
                    item_cluster = DatastaxDataRetrieval.convert_cassandra_row_or_cluster_to_json(
                        db_response
                    )
                else:
                    raise ConnectionFaulty(self.connection_object)
            else:
                item_cluster = None
        except Exception as e:
            raise ConnectionFaulty(self.connection_object) from e

        return self.process_db_response_usability(item_cluster=item_cluster)

    @staticmethod
    def process_db_response_usability(item_cluster):
        item_cluster_as_dict = {'msg': 'We could not process your request due to an internal conversion error'}
        if not item_cluster:
            return {'msg': 'There was no row corresponding to your request'}
        try:
            item_cluster_as_dict = item_cluster
            if not isinstance(item_cluster_as_dict, dict):
                raise TypeError
            return item_cluster_as_dict
        except (AttributeError, TypeError, IndexError, ValueError, ConnectionError) as e:
            item_cluster_as_dict['error'] = str(e)
        finally:
            return item_cluster_as_dict

    @staticmethod
    def convert_cassandra_row_or_cluster_to_json(cluster=None, single_row=None):
        """
        Pick one to work with, either cluster or single_row.
        Never both
        :param cluster:
        :param single_row:
        :return:
        """
        print(cluster)
        print(type(cluster))
        print(single_row)
        def convert_to_json():
            """_columns = get_columns()
            if _columns:
                _columns_max_index = len(_columns) - 1"""

            dict_row_or_cluster = {}

            if (cluster and not single_row) and isinstance(cluster, ResultSet):
                print('Is running cluster decomposer')
                for key, row in enumerate(cluster, 1):
                    print(row)
                    row_as_dict = row._asdict()
                    dict_row_or_cluster[str(key)] = row_as_dict
            elif single_row and not cluster:
                dict_row_or_cluster = single_row._asdict()

            else:
                ___type___ = None
                if single_row and not cluster:
                    ___type___ = type(single_row)
                elif not single_row and cluster:
                    ___type___ = type(cluster)
                elif single_row and cluster:
                    ___type___ = [type(single_row), type(cluster)]
                elif not single_row and not cluster:
                    ___type___ = type(None)

                if ___type___:
                    raise TypeError(f'Unexpected type was given: {str(___type___)}')
                else:
                    raise ValueError(
                        'Unexpected value was given or not given, make sure cluster or single_row is passed'
                    )

            return dict_row_or_cluster

        return convert_to_json()


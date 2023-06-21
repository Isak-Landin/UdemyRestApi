class ServerStatus:
    module_statuses = {
        'datastax-connection': True,
        'session-manager': True,
        'jwt-manager': True
    }

    @classmethod
    def is_stable(cls):
        all_pairs = cls.module_statuses.items()
        print(all_pairs)
        return all_pairs

    @classmethod
    def datastax_connection_set_unstable(cls):
        cls.module_statuses['datastax-connection'] = False

    @classmethod
    def session_manager_set_unstable(cls):
        cls.module_statuses['session-manager'] = False

    @classmethod
    def jwt_manager_set_unstable(cls):
        cls.module_statuses['jwt-manager'] = False

    @classmethod
    def is_server_stable(cls):
        key_value_pairs = cls.module_statuses.items()

        return all(value for key, value in key_value_pairs)


all_pairs_retrieved = ServerStatus.is_stable()
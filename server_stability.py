class ServerStatus:
    module_statuses = {
        'datastax-connection': False,
        'session-manager': False,
        'jwt-manager': False
    }

    @classmethod
    def is_stable(cls):
        all_pairs = cls.module_statuses.items()
        print(all_pairs)
        return all_pairs


all_pairs_retrieved = ServerStatus.is_stable()
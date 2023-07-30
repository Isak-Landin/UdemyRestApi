import time

import requests

from GeneralUtils.decorators import request_procedure

from database_modules.localconfig import astra_id, table_errors, admin_headers, keyspace


@request_procedure
def add_error(error):
    time_now = int(time.time())

import sys
import json

from utils.database import Database
from utils.general import read_file

if len(sys.argv) != 6:
    sys.exit(-1)

content_assignment_file = sys.argv[1]
port = sys.argv[2]
database_credential_file = sys.argv[3]
sql_query_file = sys.argv[4]
address_file = sys.argv[5]

database = Database(database_credential_file, sql_query_file)
address = json.loads(read_file(address_file))

import utils.server

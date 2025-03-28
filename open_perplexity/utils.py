from openperplex import OpenperplexSync
from django.conf import settings
import os

client = OpenperplexSync(os.getenv('OPENPERPLEX_API_KEY'))
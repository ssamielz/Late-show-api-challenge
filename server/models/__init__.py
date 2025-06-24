from flask_sqlalchemy import sqlachemy
from sqlachemy import Metadata
from sqlachemy_serializer import SerializerMixin
metadata = Metadata
db = sqlachemy(metadata=metadata)
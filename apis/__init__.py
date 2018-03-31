from flask_restplus import Api

from .cat import api as cat_api
from .dog import api as dog_api
from .xumii import api as xummi_api

api = Api(
    title='XuMii',
    version='1.0',
    description='X User Matter into Information',
)

# api.add_namespace(cat_api)
# api.add_namespace(dog_api)
api.add_namespace(xummi_api)
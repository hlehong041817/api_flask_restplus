from flask_restplus import Namespace, Resource, fields

api = Namespace('xumii', description='X User Matter into Information')

message_item = api.model('Message', {
    'text': fields.String(required=True, description='The message_item identifier'),
    'from': fields.String(required=True, description='The message_item name'),
})

MessageDict = [
    {'text': 'Hey', 'from': 'guest'},
    {'text': 'Hi', 'from': 'xummi'},
]


@api.route('')
class MessageList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(message_item)
    def get(self):
        '''List all cats'''
        return MessageDict


@api.route('/<id>')
@api.param('id', 'The message_item identifier')
@api.response(404, 'MessageItem not found')
class MessageItem(Resource):
    @api.doc('get_cat')
    @api.marshal_with(message_item)
    def get(self, id):
        '''Fetch a message_item given its identifier'''
        for message_item in MessageDict:
            if message_item['text'] == id:
                return message_item
        api.abort(404)
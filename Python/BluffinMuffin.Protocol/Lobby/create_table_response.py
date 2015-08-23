from abstract_response import AbstractResponse
from lobby.create_table_command import CreateTableCommand

__author__ = 'ericmas001@gmail.com'



class CreateTableResponse(AbstractResponse):
    def __init__(self, obj):
        super().__init__(obj, CreateTableCommand(obj['Command']))
        self.id_table = obj['IdTable']

    def __str__( self ):
        return '{0} => {1}'.format(super().__str__(), self.id_table)
from .exceptions import UnsupportedOperationException

class BaseBL():
    

    @staticmethod
    def _deleteAllowed(self, context, obj):
        return True

    @staticmethod
    def _insertAllowed(self, context, obj):
        return True

    @staticmethod
    def _readAllowed(self, context, obj):
        return True

    @staticmethod
    def _updateAllowed(self, context, obj):
        return True



    @staticmethod
    def _postDelete(self, context, obj):
        pass

    @staticmethod
    def _preDelete(self, context, obj):
        pass    

    @staticmethod
    def _postInsert(self, context, obj):
        pass

    @staticmethod
    def _preInsert(self, context, obj):
        pass  

    @staticmethod
    def _postRead(self, context, obj):
        pass
   
    

    @staticmethod
    def _preRead(self, context, obj):
        pass  

    @staticmethod
    def _postUpdate(self, context, obj):
        pass

    @staticmethod
    def _preUpdate(self, context, obj):
        pass  


    @staticmethod
    def delete(self, context, obj):
        raise UnsupportedOperationException()

    @staticmethod
    def insert(self, context, obj):
        raise UnsupportedOperationException()

    @staticmethod
    def read(self, context, obj):
        raise UnsupportedOperationException()

    @staticmethod
    def update(self, context, obj):
        raise UnsupportedOperationException()
        
        
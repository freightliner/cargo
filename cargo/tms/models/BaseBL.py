from .exceptions import OperationNotAllowedException

class BaseBL():

    def _deleteAllowed(self, m):
        return True

    def _preDelete(self, m):
        pass
    
    def _postDelete(self, m):
        pass

    def delete(self, m):
        if not self._deleteAllowed(m):
            raise OperationNotAllowedException(m)
        self._preDelete(m)
        m.save()
        self._postDelete(m)
    
    
    def _insertAllowed(self, m):
        return True

    def _preInsert(self, m):
        pass
    
    def _postInsert(self, m):
        pass

    def insert(self, m):
        if not self._insertAllowed(m):
            raise OperationNotAllowedException(m)
        self._preInsert(m)
        m.save()
        self._postInsert(m)


    def _updateAllowed(self, m):
        return True

    def _preUpdate(self, m):
        pass
    
    def _postUpdate(self, m):
        pass

    def update(self, m):
        if not self._updateAllowed(m):
            raise OperationNotAllowedException(m)
        self._preUpdate(m)
        m.save()
        self._postUpdate(m)

 
        
       
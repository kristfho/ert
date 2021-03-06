from ert.cwrap import BaseCClass
from ert.util import UtilPrototype


class PermutationVector(BaseCClass):
    TYPE_NAME = "permutation_vector"
    _free = UtilPrototype("void   perm_vector_free( permutation_vector )")
    _size = UtilPrototype("int    perm_vector_get_size( permutation_vector )")
    _iget = UtilPrototype("int    perm_vector_iget( permutation_vector , int)")

    
    def __init__(self):
        raise NotImplementedError("Can not instantiate PermutationVector directly")


    def __len__(self):
        return self._size( )


    def __str__(self):
        s = "("
        for index in self:
            s += " %d" % index
        return s + ")"

    
    def __getitem__(self, index):
        if index < 0:
            index += len(self)

        if 0 <= index < len(self):
            return self._iget( index )
        else:
            raise IndexError("Invalid index:%d" % index)

        
    def free(self):
        self._free( )

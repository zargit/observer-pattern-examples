import uuid

__all__ = ['Observable']

class Observable:
    """
    This is a wrapper class for a variable.
    It allows adding observers to this variable.
    Can notify all registered observers of any change.
    """

    def __init__(self, _value):
        self.value = _value  # the variable
        self.observers = {}  # observers map

    def set(self, _value):
        """
        Notifies all observers after updating existing value.
        :param _value: New value for the variable.
        """
        self.value = _value
        self.broadcast()

    def get(self):
        """
        :return: The variable instance.
        """
        return self.value

    def add_observer(self, observer):
        """
        :param observer: This is a callable function.
        :return: Unique id for the new observer.
        """
        if not callable(observer): return -1

        id = str(uuid.uuid4())
        self.observers[id] = observer
        return id

    def get_observer(self, id):
        """
        Returns an observer with id/
        :param id: Unique observer id.
        :return: A callable function.
        """
        return self.observers.get(id)

    def remove_observer(self, id):
        """
        Removes observer with if from the list.
        :param id: Unique observer id.
        """
        del self.observers[id]

    def broadcast(self):
        """
        Notifies all observers.
        """
        for id in self.observers:
            self.observers[id](self.value)

    def __repr__(self):
        return self

    def __str__(self):
        return "<"+self.__class__.__name__+" type="+str(type(self.value))+">"
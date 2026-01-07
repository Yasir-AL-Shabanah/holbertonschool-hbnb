
 import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, Type


class InMemoryRepository:
    """
    A simple in-memory repository.
    Stores objects by class name then by object.id (string UUID).
    """

    def __init__(self) -> None:
        self._storage: Dict[str, Dict[str, Any]] = {}

    def _get_class_store(self, cls: Type) -> Dict[str, Any]:
        name = cls.__name__
        if name not in self._storage:
            self._storage[name] = {}
        return self._storage[name]

    def add(self, obj: Any) -> Any:
        """
        Add an object to storage. The object must have an 'id' attribute.
        """
        if not hasattr(obj, "id") or not obj.id:
            # If your models generate ids themselves, this is just a fallback
            obj.id = str(uuid.uuid4())

        store = self._get_class_store(obj.__class__)
        store[str(obj.id)] = obj
        return obj

    def get(self, cls: Type, obj_id: str) -> Optional[Any]:
        store = self._get_class_store(cls)
        return store.get(str(obj_id))

    def list(self, cls: Type) -> List[Any]:
        store = self._get_class_store(cls)
        return list(store.values())

    def update(self, obj: Any, data: Dict[str, Any]) -> Any:
        """
        Update object's attributes from dict.
        If object has 'updated_at', refresh it.
        """
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        if hasattr(obj, "updated_at"):
            obj.updated_at = datetime.utcnow()

        # ensure stored
        self.add(obj)
        return obj

    def delete(self, cls: Type, obj_id: str) -> bool:
        store = self._get_class_store(cls)
        return store.pop(str(obj_id), None) is not None
   
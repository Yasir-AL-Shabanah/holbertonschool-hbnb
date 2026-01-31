from typing import Any, Dict, List, Optional, Type

from app.extensions import db


class SQLAlchemyRepository:
    def __init__(self, model: Type[db.Model], session=None) -> None:
        self.model = model
        self.session = session or db.session

    def get(self, obj_id: str) -> Optional[db.Model]:
        return self.model.query.get(obj_id)

    def list(self, **filters: Any) -> List[db.Model]:
        query = self.model.query
        if filters:
            query = query.filter_by(**filters)
        return list(query.all())

    def add(self, instance: db.Model) -> db.Model:
        self.session.add(instance)
        self.session.commit()
        return instance

    def delete(self, instance: db.Model) -> None:
        self.session.delete(instance)
        self.session.commit()

    def update(self, instance: db.Model, data: Dict[str, Any]) -> db.Model:
        for key, value in data.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        self.session.commit()
        return instance

from typing import Any
from sqlalchemy.orm import Session
from fastapi.responses import Response

from app.models import Link, Category, LinkConnection, SubPage, Url
from app.core.database import engine


class BaseController(object):
    """ Base View to create helpers common to all Webservices.
    """

    def __init__(self, db: Session):
        """Constructor
        """
        self.close_session = None
        if db:
            self.db = db
        else:
            self.db = Session(engine)
            self.close_session = True

        self.model_class = None

    def _get_all(self, *args: Any, **kwargs: Any):
        """Query to get all records from the database.
        """

        columns = dict()
        params = kwargs.get("request").query_params._dict
        for param in self.model_class.__mapper__.attrs.keys():
            if params.get(param) is not None:
                columns[param] = params.get(param)

        try:
            query_model = self.db.query(self.model_class)

            for column in columns:
                item_param = None if columns.get(column) == 'null' else columns.get(column)

                query_model = query_model.filter(
                    getattr(self.model_class, column) == item_param
                )

            order_by = getattr(self.model_class, kwargs.get("sort_by"))

            query_model = query_model.order_by(
                getattr(order_by, kwargs.get("order_by"))()
            ).offset(
                kwargs.get("offset")
            ).limit(
                kwargs.get("limit")
            ).all()

            if query_model:
                return query_model

        except Exception:
            return Response(status_code=422)

        finally:
            if self.close_session:
                self.db.close()

        return Response(status_code=204)

    def get(self, model_id: int):
        """Get a record from the database.
        """
        try:
            query = self.db.query(self.model_class).filter(
                self.model_class.id == model_id
            ).first()

            if query:
                return query
        except Exception:
            return Response(status_code=422)

        finally:
            if self.close_session:
                self.db.close()

        return Response(status_code=204)

    def post(self, data: dict):
        """Create a record in the database.
        """
        db_data = self.model_class(**data)
        try:
            self.db.add(db_data)
            self.db.commit()
            self.db.refresh(db_data)
            return db_data
        except Exception:
            return Response(status_code=422)

        finally:
            if self.close_session:
                self.db.close()

    def put(self, data: dict, model_id: int = None, params: dict = list()):
        """Edit a record in the database.
        """
        try:
            query_model = self.db.query(self.model_class)

            if model_id:
                query_model = query_model.filter(
                    self.model_class.id == model_id
                )

            if params:
                for item in params:
                    if params.get(item) is not None:
                        query_model = query_model.filter(
                            getattr(self.model_class, item) == params.get(item)
                        )

            query_model = query_model.one_or_none()

            if query_model:
                for item in data:
                    if data.get(item) is not None:
                        setattr(query_model, item, data[item])

                self.db.merge(query_model)
                self.db.commit()
                self.db.refresh(query_model)
                return query_model

        except:
            return Response(status_code=422)

        finally:
            if self.close_session:
                self.db.close()

        return Response(status_code=204)


class ControllerLink(BaseController):

    def __init__(self, db: Session):
        super().__init__(db)
        self.model_class = Link


class ControllerCategory(BaseController):

    def __init__(self, db: Session):
        super().__init__(db)
        self.model_class = Category


class ControllerConnection(BaseController):

    def __init__(self, db: Session):
        super().__init__(db)
        self.model_class = LinkConnection


class ControllerSubPage(BaseController):

    def __init__(self, db: Session):
        super().__init__(db)
        self.model_class = SubPage


class ControllerUrl(BaseController):

    def __init__(self, db: Session):
        super().__init__(db)
        self.model_class = Url

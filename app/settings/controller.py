from sqlalchemy.orm import Session
from fastapi.responses import Response

from app.models import Link, Category, Connection, SubPage
from app.settings.database import engine


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

    def all(self, skip: int = 0, limit: int = 100):
        """Query to get all records from the database.
        """
        try:
            query = self.db.query(
                self.model_class
            ).offset(skip).limit(limit).all()

            if query:
                return query
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

    def get_by(self, params: dict, skip: int = 0, limit: int = 100):
        try:
            query_model = self.db.query(self.model_class)

            for item in params:
                item_param = None if params.get(item) == 'null' else params.get(item)

                query_model = query_model.filter(
                    getattr(self.model_class, item) == item_param
                )

            query_model = query_model.offset(skip).limit(limit).all()
            if query_model:
                return query_model

        except Exception:
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
        self.model_class = Connection


class ControllerSubPage(BaseController):

    def __init__(self, db: Session):
        super().__init__(db)
        self.model_class = SubPage

from abc import ABC, abstractmethod
from typing import Any
from datetime import datetime

class ServiceAPI(ABC):

    @abstractmethod
    def commit(self, session: Any):
        pass 

    @abstractmethod
    def flush(self):
        pass 

    @abstractmethod
    def flush_models(self, *models: Any):
        pass 

    @abstractmethod
    def create_model(self, model: Any, **kwargs):
        pass 

    @abstractmethod
    def get_user_by_username(self, username: str) -> Any | None:
        pass 

    @abstractmethod
    def get_user_by_email(self, email: str) -> Any | None:
        pass

    @abstractmethod
    def get_tasks_by_userId(self, user_id: str, n: int) -> Any | None:
        pass 

    @abstractmethod
    def get_events_by_userId(self, user_id: str, n: int) -> Any | None:
        pass 

    @abstractmethod
    def get_task_by_data(self, user_id: str, _data: datetime):
        pass 

    @abstractmethod
    def get_event_by_data(self, user_id: str, _data: datetime):
        pass 


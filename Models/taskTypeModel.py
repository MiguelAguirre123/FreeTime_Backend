from sqlalchemy import Column, Integer, String
from Models.init import Base

class TaskType(Base):
    __tablename__ = 'TaskType'

    task_type_id = Column(Integer, primary_key=True)
    task_type_name = Column(String(400))

    def __repr__(self):
        return (f"<TaskType(task_type_id={self.task_type_id}, "
                f"task_type_name={self.task_type_name})>")
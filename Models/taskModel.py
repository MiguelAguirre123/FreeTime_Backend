from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,DECIMAL
from Models.init import Base

class Task(Base):
    __tablename__ = 'Task'

    task_id = Column(Integer, primary_key=True)
    task_offer_suggested = Column(String(400))
    task_description = Column(String(400))
    task_stimed_time_hours = Column(DECIMAL, nullable= False)
    task_type_id = Column(Integer, ForeignKey('TaskType.task_type_id'))

    def __repr__(self):
        return (f"<Task(task_id={self.task_id}, "
                f"task_offer_suggested={self.task_offer_suggested}, "
                f"task_description={self.task_description}, "
                f"task_stimed_time_hours={self.task_stimed_time_hours}, "
                f"task_type_id={self.task_type_id})>")
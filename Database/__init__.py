from .DB_connect import get_db
from .CURD import create_question,delete_question,read_question,update_question
__all__ = [get_db,update_question,read_question,create_question,delete_question]
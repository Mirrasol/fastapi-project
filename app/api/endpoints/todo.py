from fastapi import APIRouter, Depends

from app.api.schemas.todo import ToDoCreate, ToDoFromDB
from app.services.todo_service import ToDoService
from app.utils.unit_of_work import UnitOfWork, BaseUnitOfWork

todo_router = APIRouter(
    prefix="/todo",
    tags=["ToDo"],
)


async def get_todo_service(uow: BaseUnitOfWork = Depends(UnitOfWork)) -> ToDoService:
    return ToDoService(uow)


@todo_router.get("/todos/", response_model=list[ToDoFromDB])
async def get_todos(todo_service: ToDoService = Depends(get_todo_service)):
    return await todo_service.get_todos()


@todo_router.post("/todos/", response_model=ToDoFromDB)
async def create_todo(todo_data: ToDoCreate, todo_service: ToDoService = Depends(get_todo_service)):
    return await todo_service.add_todo(todo_data)

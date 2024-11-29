from api.v1 import router as v1_router
from core.exceptions.handlers import exception_handlers
from core.setup import create_application

app = create_application(router=v1_router)


for exc_box in exception_handlers:
    app.add_exception_handler(
        exc_class_or_status_code=exc_box.exception_class,
        handler=exc_box.exception_handler,
    )

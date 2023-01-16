import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import ValidationError
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from operations.router import router as router_operation

app = FastAPI(title="test app")


@app.exception_handler(ValidationError)
async def vadation_exeption_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )

app.include_router(router_operation)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

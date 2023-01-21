import sys

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.exceptions import ValidationError
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

sys.path.append("/Users/elena/PycharmProjects/fastapi_app")


from src.data import router as data_router

app = FastAPI(title="test app")

@app.exception_handler(ValidationError)
async def vadation_exeption_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()})
    )

app.include_router(data_router.router)


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)

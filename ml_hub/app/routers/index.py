from fastapi import APIRouter, Request, Response


router = APIRouter()


@router.get(path="/")
async def root(
    request: Request,
    response: Response
):
    return "API Gateway-llms is alive"
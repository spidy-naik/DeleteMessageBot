import datetime
from aiohttp import web


routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    res = {
        "status":"ok"
    }
    return web.json_response(res)

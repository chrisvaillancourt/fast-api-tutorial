from fastapi import FastAPI

app = FastAPI()


# `@app.get('/)`` tells FastAPI that the fun below handles requests that go to
# the path `/` and use a `get` operation
# It's formally referred to as a 'path operation decorator'
@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

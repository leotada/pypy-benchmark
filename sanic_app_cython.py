
from sanic import Sanic
from sanic.response import json

from fib_module import fib

app = Sanic()


@app.route('/')
async def bench(request):
    return json({'message': fib(15)})


if __name__ == "__main__":
    print('Running App with Cython')
    app.run('0.0.0.0', 8000, workers=8, access_log=False)

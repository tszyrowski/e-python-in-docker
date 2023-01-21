from fastapi import FastAPI
import redis

import debugpy
debugpy.listen(("0.0.0.0", 5678))
debugpy.wait_for_client()  # this line is not strictly necessary


app =FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"Hello": "form FAPI wit redis"}

@app.get("/hits")
def read_root():
    print("Inside code the hits endpoint was hit")
    r.incr("hits")
    return {"number of hits": r.get("hits")}
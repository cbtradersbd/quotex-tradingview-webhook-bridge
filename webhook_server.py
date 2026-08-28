from fastapi import FastAPI
app = FastAPI()

@app.post("/webhook/quotex")
async def execute_tv_signal(payload: dict):
    print("Executing Quotex trade for signal:", payload)
    return {"result": "success"}

from fastapi import FastAPI

app = FastAPI(title="Python CI/CD Demo", version="1.0.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "CI/CD pipeline is working"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/sum")
def sum_numbers(a: int, b: int) -> dict[str, int]:
    return {"result": a + b}

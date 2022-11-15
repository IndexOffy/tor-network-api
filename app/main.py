from fastapi import FastAPI


app = FastAPI(
    title="OnionAPI",
    description="Project OnionAPI",
    version="0.0.1"
)

@app.get("/status")
def get_status():
    """Get status of messaging server."""
    return ({"status":  "it's alive"})

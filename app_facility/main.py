from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data_store import get_store
from app.routers import facilities, energy, assets, maintenance, occupancy, security, alerts, costs, dashboard

app = FastAPI(
    title="Smart Facility Management API",
    description="REST API serving the Smart Facility Management dataset "
    "(facilities, energy, assets, maintenance, occupancy, security, alerts, costs).",
    version="1.0.0",
)

# Vite's default dev server ports. Add your deployed frontend origin here too.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def load_data():
    get_store().load_all()


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


app.include_router(facilities.router)
app.include_router(energy.router)
app.include_router(assets.router)
app.include_router(maintenance.router)
app.include_router(occupancy.router)
app.include_router(security.router)
app.include_router(alerts.router)
app.include_router(costs.router)
app.include_router(dashboard.router)

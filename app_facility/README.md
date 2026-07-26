# Backend — Smart Facility Management API

FastAPI service that serves the Smart Facility Management dataset as a REST API.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Swagger docs: `http://127.0.0.1:8000/docs`
ReDoc: `http://127.0.0.1:8000/redoc`

## Project layout

```
app/
├── main.py              FastAPI app, CORS, router registration, startup data load
├── data_store.py         Loads data/facility_data.xlsx into pandas DataFrames on startup
├── utils.py               Shared helpers (DataFrame -> JSON, query-param filtering)
├── data/facility_data.xlsx   The source dataset
└── routers/
    ├── facilities.py
    ├── energy.py
    ├── assets.py
    ├── maintenance.py
    ├── occupancy.py
    ├── security.py
    ├── alerts.py
    ├── costs.py
    └── dashboard.py       Cross-sheet KPI aggregates for the overview page
```

## Endpoint reference

All routes are prefixed `/api`.

| Resource | Endpoint | Notes |
|---|---|---|
| Health | `GET /health` | |
| Facilities | `GET /facilities` | filters: `facility_type`, `city`, `state` |
| | `GET /facilities/{id}` | 404 if not found |
| | `GET /facilities/types` | distinct types/cities/states for filter dropdowns |
| Energy | `GET /energy` | filters: `facility_id`, `start`, `end` (ISO dates) |
| | `GET /energy/trend` | daily totals, optional `facility_id` |
| | `GET /energy/by-facility` | totals per facility |
| Assets | `GET /assets` | filters: `facility_id`, `asset_type`, `status` |
| | `GET /assets/{id}` | 404 if not found |
| | `GET /assets/status-summary` | counts by status and by type+status |
| Maintenance | `GET /maintenance` | filters: `facility_id`, `status`, `technician` |
| | `GET /maintenance/summary` | by status, by issue type, totals |
| Occupancy | `GET /occupancy` | filters: `facility_id`, `room` |
| | `GET /occupancy/by-facility` | avg/peak per facility |
| | `GET /occupancy/by-room-type` | avg/total per room type |
| Security | `GET /security-events` | filters: `facility_id`, `severity`, `status` |
| | `GET /security-events/summary` | by severity/type/status |
| Alerts | `GET /alerts` | filters: `facility_id`, `priority`, `status` |
| | `GET /alerts/summary` | by priority/type, active count |
| Costs | `GET /cost-reports` | filters: `facility_id`, `month` |
| | `GET /cost-reports/trend` | monthly totals, all facilities |
| | `GET /cost-reports/by-facility` | totals per facility |
| Dashboard | `GET /dashboard/summary` | every headline KPI in one call |
| | `GET /dashboard/recent-activity` | latest active alerts + open events |
| | `GET /dashboard/facility-overview` | per-facility rollup joining every sheet |

## Data model notes

- `maintenance_records` only stores `asset_id` in the source sheet. On load, `data_store.py`
  joins in `facility_id` from `assets` so maintenance can be filtered by facility directly.
- All timestamp/date columns are parsed to `datetime64` on load and serialized back to ISO 8601
  strings (`YYYY-MM-DDTHH:MM:SS`) in API responses.
- `cost_reports.month` stays as its original label (e.g. `"Feb-2026"`) in responses; a derived
  `month_period` column is used only for sorting and dropped before serialization.

## Swapping in a real database

Every router calls `get_store().df("sheet_name")`, which returns a fresh pandas DataFrame copy.
To move off in-memory Excel data, replace the body of `Store.load_all()` /  `Store.df()` in
`data_store.py` with queries against your database — the routers themselves don't need to change
as long as `df()` keeps returning a DataFrame with the same columns.

# Frontend — Smart Facility Management Dashboard

React + Vite dashboard for the Smart Facility Management API, styled as a control-room /
building-management console.

## Setup

```bash
npm install
npm run dev       # dev server at http://127.0.0.1:5173
npm run build      # production build -> dist/
npm run preview    # serve the production build locally
```

By default the app calls the API at `http://127.0.0.1:8000`. To point elsewhere, copy
`.env.example` to `.env` and set `VITE_API_BASE_URL`.

## Project layout

```
src/
├── api/client.js            Axios instance + one function per API endpoint
├── hooks/
│   ├── useFetch.js           Generic { data, loading, error } fetch hook
│   └── FacilityFilterContext.jsx   Global "scope every page to one facility" selector
├── components/
│   ├── Layout.jsx, Sidebar.jsx, Topbar.jsx
│   ├── Panel.jsx              Card with the signature colored "status rail"
│   ├── KpiCard.jsx            Console-style stat readout
│   ├── StatusPill.jsx         Status/severity/priority badge
│   ├── DataTable.jsx          Generic table (columns + rows)
│   ├── ChartTheme.jsx         Shared Recharts colors, tooltip, axis styling
│   └── States.jsx             Loading / error placeholders
├── pages/                     One file per dashboard section (see root README for the list)
├── utils/format.js            en-IN number/currency/date formatting
└── styles/index.css            Tailwind + design-token utility classes
```

## Design system

- **Palette**: deep navy canvas (`#0A0F1C`) with signal colors for status — teal (`#2FD3B0`,
  normal), amber (`#F5A93F`, caution), red (`#F2545B`, critical), indigo (`#7C93F7`, secondary
  data series). Defined as Tailwind theme tokens in `tailwind.config.js`.
- **Type**: Space Grotesk (headings), Inter (body), IBM Plex Mono (all numeric readouts —
  tabular figures for a real instrument-panel feel).
- **Signature element**: every panel/KPI card carries a 3px colored rail along its top edge,
  echoing status LEDs on physical building-management hardware.

## Adding a new page

1. Add an endpoint function to `src/api/client.js` if needed.
2. Create `src/pages/YourPage.jsx` — wrap content in `<Layout title="..." subtitle="...">`.
3. Register the route in `src/App.jsx` and add a nav entry in `src/components/Sidebar.jsx`.

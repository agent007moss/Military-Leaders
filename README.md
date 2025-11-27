# Military Leaders Tool – Phase 1 Skeleton

This repository contains a **non-functional** project scaffold that mirrors
the Phase 1 Master Specification. It is designed so you can open the
structure in your editor, wire up environment tooling, and then implement
business logic module by module.

## Layout

- `backend/` – FastAPI-based backend scaffold
- `web/` – Minimal React/Vite SPA scaffold
- `mobile/` – Minimal React Native/Expo-style scaffold (structure only)
- `config/` – Metadata and dashboard layout placeholders

## Backend (development placeholder)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install fastapi uvicorn[standard] pydantic
uvicorn main:app --reload
```

Then visit `http://localhost:8000/health` to confirm the skeleton is reachable.

## Web (development placeholder)

```bash
cd web
npm install
npm run dev
```

Open the printed localhost URL to see the dashboard box placeholders.

## Mobile

The `mobile/` directory only contains React Native–style placeholder files.
Integrate with your preferred mobile toolchain (Expo, React Native CLI, etc.)
before adding real logic.

## Important

- No persistence
- No authentication
- No business rules

Everything in this skeleton is intentionally minimal and safe to refactor.
You can now start filling in each module according to the Phase 1 Master
Specification without worrying about initial project wiring.

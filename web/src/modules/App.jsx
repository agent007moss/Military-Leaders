import React from "react";
import { DashboardShell } from "./dashboard/DashboardShell";

export const App = () => {
  return (
    <div className="app-root">
      <header>
        <h1>Military Leaders Tool – Phase 1 Web Skeleton</h1>
      </header>
      <DashboardShell />
    </div>
  );
};

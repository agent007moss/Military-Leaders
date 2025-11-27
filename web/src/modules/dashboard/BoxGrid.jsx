import React from "react";
import { BoxPlaceholder } from "./BoxPlaceholder";

const BOXES = [
  "PERSTATS",
  "Appointments",
  "Physical Fitness",
  "Profiles",
  "Weapons",
  "Medpros",
  "Training",
  "Tasks",
  "Duty Roster",
  "Counseling",
  "Flags/UCMJ",
  "Awards",
  "Evaluations",
];

export const BoxGrid = () => {
  return (
    <section className="box-grid">
      {BOXES.map((name) => (
        <BoxPlaceholder key={name} title={name} />
      ))}
    </section>
  );
};

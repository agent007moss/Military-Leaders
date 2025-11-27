import React from "react";

export const BoxPlaceholder = ({ title }) => {
  return (
    <article className="box">
      <header>
        <h2>{title}</h2>
      </header>
      <div className="box-content">
        <p>Dashboard metrics placeholder.</p>
      </div>
    </article>
  );
};

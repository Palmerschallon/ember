import React from "react";
import { AnchorPanel } from "./AnchorPanel";

export const PodShell: React.FC = () => {
  return (
    <div className="h-screen w-screen bg-black text-slate-100 grid grid-cols-[2fr,1fr] gap-3 p-3">
      <section className="rounded-3xl border border-slate-800 bg-slate-950/60">
        {/* Main workspace / editor / swarm view goes here */}
      </section>
      <section className="rounded-3xl overflow-hidden">
        <AnchorPanel />
      </section>
    </div>
  );
};

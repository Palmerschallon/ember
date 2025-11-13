import React, { useEffect, useState } from "react";
import { AnchorClient, AnchorEntry } from "./anchorClient";

const client = new AnchorClient("http://127.0.0.1:7171");

function AnchorMark() {
  return (
    <div className="flex items-center justify-center mb-4">
      <div className="relative">
        <div
          className="
            w-[80px] h-[130px]
            bg-white
            rounded-[999px]
            relative
            shadow-[0_0_30px_rgba(255,255,255,0.06)]
          "
          style={{
            clipPath:
              "path('M40 0 C 60 45 80 75 80 110 C80 132 64 148 40 148 C16 148 0 132 0 110 C0 75 20 45 40 0 Z')",
          }}
        >
          <div className="
            w-[46px] h-[46px]
            bg-[#ff2626]
            rounded-full
            absolute
            left-1/2 top-[56%]
            -translate-x-1/2 -translate-y-1/2
          " />
        </div>
      </div>
    </div>
  );
}

type Status = "idle" | "loading" | "error";

export const AnchorPanel: React.FC = () => {
  const [entries, setEntries] = useState<AnchorEntry[]>([]);
  const [status, setStatus] = useState<Status>("idle");
  const [input, setInput] = useState("");
  const [health, setHealth] = useState<"unknown" | "ok" | "down">("unknown");

  useEffect(() => {
    let cancelled = false;

    async function init() {
      try {
        const ok = await client.health();
        if (cancelled) return;
        setHealth(ok ? "ok" : "down");
        if (ok) {
          setStatus("loading");
          const list = await client.list(30);
          if (!cancelled) {
            setEntries(list);
            setStatus("idle");
          }
        }
      } catch {
        if (!cancelled) {
          setHealth("down");
          setStatus("error");
        }
      }
    }

    init();
    return () => {
      cancelled = true;
    };
  }, []);

  async function handleAnchor(e: React.FormEvent) {
    e.preventDefault();
    const text = input.trim();
    if (!text) return;
    setStatus("loading");
    try {
      const entry = await client.add(text, {
        source: "pod-ui",
        type: "note",
      });
      setEntries((prev) => [entry, ...prev].slice(0, 50));
      setInput("");
      setStatus("idle");
    } catch (err) {
      console.error(err);
      setStatus("error");
    }
  }

  return (
    <div className="h-full w-full bg-black text-slate-100 flex flex-col border border-slate-800 rounded-2xl overflow-hidden">
      <div className="px-4 pt-4 pb-3 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <AnchorMark />
          <div className="text-left">
            <div className="text-xs tracking-[0.25em] uppercase text-slate-400">
              Memory Spine
            </div>
            <div className="text-lg font-semibold tracking-wide">
              Anchor
            </div>
          </div>
        </div>
        <div className="text-xs text-slate-500">
          {health === "ok" && <span className="text-emerald-400">Local · Online</span>}
          {health === "down" && <span className="text-rose-400">Offline</span>}
          {health === "unknown" && <span className="text-slate-500">Checking…</span>}
        </div>
      </div>

      <form onSubmit={handleAnchor} className="px-4 py-3 border-b border-slate-800">
        <div className="flex items-center gap-2">
          <input
            className="
              flex-1 bg-slate-950/80 border border-slate-700/60
              rounded-full px-4 py-2 text-sm
              placeholder:text-slate-500
              focus:outline-none focus:ring-1 focus:ring-[#ff2626]/80
            "
            placeholder="Anchor a moment…"
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            type="submit"
            disabled={status === "loading" || health !== "ok"}
            className="
              px-4 py-2 rounded-full text-xs font-semibold
              tracking-[0.18em] uppercase
              bg-[#ff2626] text-white
              disabled:opacity-40 disabled:cursor-not-allowed
              shadow-[0_0_20px_rgba(255,38,38,0.5)]
            "
          >
            Anchor
          </button>
        </div>
        <div className="mt-1 text-[0.7rem] text-slate-500">
          Stored locally. Linked immutably. No cloud, no token.
        </div>
      </form>

      <div className="flex-1 overflow-auto px-3 py-2 space-y-2 text-sm">
        {status === "loading" && entries.length === 0 && (
          <div className="text-xs text-slate-500 px-1 py-2">
            Loading recent anchors…
          </div>
        )}

        {entries.length === 0 && status === "idle" && (
          <div className="text-xs text-slate-500 px-1 py-3">
            No anchors yet. Your first one will be the start of the spine.
          </div>
        )}

        {entries.map((entry) => (
          <div
            key={entry.id}
            className="
              group relative border border-slate-800/80 rounded-xl
              px-3 py-2 bg-slate-950/80
              hover:border-[#ff2626]/70
              transition-colors
            "
          >
            <div className="flex items-center justify-between gap-2 mb-1">
              <div className="text-[0.7rem] text-slate-500">
                {entry.ts_utc}
              </div>
              <div className="flex items-center gap-1 text-[0.65rem] text-slate-600">
                <span className="w-1.5 h-1.5 rounded-full bg-[#ff2626]" />
                <span>#{entry.id}</span>
              </div>
            </div>
            <div className="text-xs text-slate-100 whitespace-pre-wrap">
              {entry.text}
            </div>
            <div className="mt-1 text-[0.6rem] text-slate-600 flex items-center justify-between gap-2">
              <div className="truncate">
                {entry.hash_hex.slice(0, 12)}…
              </div>
              {entry.meta?.project && (
                <span className="px-2 py-0.5 rounded-full border border-slate-700 text-[0.6rem] text-slate-300">
                  {String(entry.meta.project)}
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

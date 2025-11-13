export interface AnchorEntry {
  id: number;
  ts_utc: string;
  text: string;
  meta: Record<string, unknown>;
  hash_hex: string;
  prev_hash_hex: string | null;
}

export class AnchorClient {
  constructor(private baseUrl: string = "http://127.0.0.1:7171") {}

  async health(): Promise<boolean> {
    try {
      const res = await fetch(`${this.baseUrl}/health`);
      const data = await res.json();
      return data.status === "ok";
    } catch {
      return false;
    }
  }

  async add(text: string, meta: Record<string, unknown> = {}): Promise<AnchorEntry> {
    const res = await fetch(`${this.baseUrl}/entries`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, meta })
    });
    if (!res.ok) throw new Error("Failed to add entry");
    return await res.json();
  }

  async list(limit = 20): Promise<AnchorEntry[]> {
    const res = await fetch(`${this.baseUrl}/entries?limit=${limit}`);
    if (!res.ok) throw new Error("Failed to list entries");
    return await res.json();
  }

  async verify(text: string, at?: string): Promise<AnchorEntry[]> {
    const res = await fetch(`${this.baseUrl}/verify`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, at })
    });
    if (!res.ok) throw new Error("Failed to verify");
    return await res.json();
  }
}

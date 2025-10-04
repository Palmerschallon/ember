# Tickets

## Ticket 1: Camera Zoom-to-Cursor
**Status**: Pending
**Priority**: High

Implement Canvas2D camera controls where zoom operations target the cursor position instead of the viewport center.

### Requirements
- Calculate world position under cursor
- Scale camera around cursor point
- Smooth zoom transitions
- Mouse wheel support

### Acceptance Criteria
- Zooming keeps the point under cursor stationary
- Works with both zoom in and zoom out
- No viewport jumping or jittering

---

## Ticket 2: Deterministic Universe Factory
**Status**: Pending
**Priority**: High

Create a seeded random universe generator that produces consistent results for the same seed.

### Requirements
- Seed-based random number generation
- Generate entities (stars, planets, etc.)
- Reproducible results
- JSON serializable state

### Acceptance Criteria
- Same seed produces identical universe
- Different seeds produce different universes
- Can regenerate universe from seed

---

## Ticket 3: LOD Promotion
**Status**: Pending
**Priority**: Medium

Implement Level-of-Detail system that adjusts entity rendering detail based on camera distance.

### Requirements
- Multiple LOD levels (low, medium, high)
- Distance-based promotion/demotion
- Smooth transitions
- Performance optimization

### Acceptance Criteria
- Distant entities use low-detail rendering
- Close entities use high-detail rendering
- LOD changes are imperceptible
- Reduces rendering load for distant entities

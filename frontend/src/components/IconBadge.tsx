export type IconName = 'air' | 'bike' | 'box' | 'boxes' | 'chart' | 'check' | 'factory' | 'globe' | 'gauge' | 'package' | 'recycle' | 'scan' | 'settings' | 'shield' | 'shop' | 'store' | 'train' | 'truck' | 'user' | 'warehouse' | 'wrench'

const paths: Record<IconName, string> = {
  air: 'M3 12h18M12 3v18M5 7l7 5 7-5M5 17l7-5 7 5',
  bike: 'M5 16a3 3 0 1 0 6 0 3 3 0 0 0-6 0Zm8 0a3 3 0 1 0 6 0 3 3 0 0 0-6 0ZM8 16l4-7 4 7m-4-7h4',
  box: 'm4 7 8-4 8 4-8 4-8-4Zm0 0v10l8 4 8-4V7m-8 4v10',
  boxes: 'm3 8 5-3 5 3-5 3-5-3Zm9 0 5-3 5 3-5 3-5-3ZM3 8v8l5 3 5-3V8m4 0v8l5 3v-8',
  chart: 'M5 20V10m7 10V4m7 16v-7',
  check: 'm4 12 5 5L20 6',
  factory: 'M3 20V9l6 3V8l6 3V6l6 3v11H3Zm4-3h2m3 0h2m3 0h2',
  globe: 'M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Zm-9-9h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18',
  gauge: 'M4 17a8 8 0 1 1 16 0M12 13l4-4',
  package: 'm4 7 8-4 8 4-8 4-8-4Zm0 0v10l8 4 8-4V7',
  recycle: 'm7 7-2 3h5m7 3 2-3-2-3m-5 10h-3l-2-3m10-4-3 5m-7-5 3 5',
  scan: 'M4 8V5h3m10 0h3v3M4 16v3h3m10 0h3v-3M8 9h8v6H8z',
  settings: 'M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm0-5v3m0 8v8M3 12h3m12 0h3M5.6 5.6l2.1 2.1m6.6 6.6 2.1 2.1m0-10.8-2.1 2.1m-6.6 6.6-2.1 2.1',
  shield: 'M12 3 20 6v6c0 5-3 8-8 9-5-1-8-4-8-9V6l8-3Zm-4 9 3 3 5-5',
  shop: 'M4 10h16v10H4zM3 10l2-6h14l2 6M8 14h3v6H8',
  store: 'M4 10h16v10H4zM3 10l2-6h14l2 6M7 10v2m5-2v2m5-2v2',
  train: 'M6 18h12M8 18l-2 3m10-3 2 3M7 15h10V6c0-2-2-3-5-3S7 4 7 6v9Zm0-5h10M9 18h6',
  truck: 'M3 7h11v10H3zM14 11h4l3 3v3h-7M7 20a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm11 0a2 2 0 1 0 0-4 2 2 0 0 0 0 4Z',
  user: 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm-7 9a7 7 0 0 1 14 0',
  warehouse: 'm3 10 9-6 9 6v10H3V10Zm4 10v-6h10v6M7 10h10',
  wrench: 'm14 6 4-3 3 3-3 4-4-1-7 7a2 2 0 1 1-3-3l7-7Z',
}

export function IconBadge({ name, size = 24 }: { name: IconName; size?: number }) {
  return <svg className="concept-icon" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d={paths[name]} /></svg>
}

export function questionIcon(visual: string): IconName {
  const map: Record<string, IconName> = {
    AIR: 'air',
    BARCODE: 'scan',
    CHECK: 'check',
    COUNT: 'boxes',
    DATA: 'chart',
    FINAL: 'truck',
    FIX: 'wrench',
    FLOW: 'globe',
    GREEN: 'recycle',
    MAKE: 'factory',
    MOVE: 'bike',
    PLAN: 'gauge',
    REUSE: 'recycle',
    ROBOT: 'settings',
    SAFE: 'shield',
    SCAN: 'scan',
    SHIP: 'train',
    SHOP: 'store',
    STORE: 'warehouse',
    SUPPLY: 'boxes',
    TRUCK: 'truck',
    USE: 'user',
  }
  return map[visual] ?? 'package'
}

export function answerIcon(visual: string, index: number): IconName {
  const map: Record<string, [IconName, IconName]> = {
    AIR: ['air', 'train'],
    BARCODE: ['package', 'truck'],
    CHECK: ['check', 'shield'],
    COUNT: ['boxes', 'truck'],
    DATA: ['chart', 'box'],
    FINAL: ['truck', 'factory'],
    FIX: ['wrench', 'box'],
    FLOW: ['package', 'store'],
    GREEN: ['recycle', 'truck'],
    MAKE: ['factory', 'store'],
    MOVE: ['bike', 'train'],
    PLAN: ['user', 'globe'],
    REUSE: ['recycle', 'box'],
    ROBOT: ['settings', 'user'],
    SAFE: ['shield', 'boxes'],
    SCAN: ['scan', 'truck'],
    SHIP: ['bike', 'train'],
    SHOP: ['shop', 'factory'],
    STORE: ['warehouse', 'truck'],
    SUPPLY: ['boxes', 'user'],
    TRUCK: ['truck', 'box'],
    USE: ['user', 'warehouse'],
  }
  return (map[visual] ?? ['package', 'box'])[index]
}

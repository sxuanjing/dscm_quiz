import type { Question } from './types'

export const questions: Question[] = [
  { id: 'meaning', category: 'flow', prompt: 'What does SCM connect?', choices: [{ id: 'a', label: 'Products to customers' }, { id: 'b', label: 'Only the checkout' }], correctChoiceId: 'a', explanation: 'SCM helps products move from source to customer.', visual: 'FLOW' },
  { id: 'supplier', category: 'roles', prompt: 'Who provides parts?', choices: [{ id: 'a', label: 'A supplier' }, { id: 'b', label: 'A customer' }], correctChoiceId: 'a', explanation: 'Suppliers provide materials and parts.', visual: 'SUPPLY' },
  { id: 'warehouse', category: 'warehouse', prompt: 'Why use a warehouse?', choices: [{ id: 'a', label: 'Store products' }, { id: 'b', label: 'Make roads' }], correctChoiceId: 'a', explanation: 'Warehouses hold products safely until they are needed.', visual: 'STORE' },
  { id: 'transport', category: 'transport', prompt: 'Best for an urgent local delivery?', choices: [{ id: 'a', label: 'Bike courier' }, { id: 'b', label: 'Cargo ship' }], correctChoiceId: 'a', explanation: 'A bike courier is quick and flexible for short trips.', visual: 'MOVE' },
  { id: 'retailer', category: 'roles', prompt: 'What is a supermarket?', choices: [{ id: 'a', label: 'A retailer' }, { id: 'b', label: 'A mine' }], correctChoiceId: 'a', explanation: 'Retailers sell products to customers.', visual: 'SHOP' },
  { id: 'inventory', category: 'warehouse', prompt: 'Too many unsold coats are…', choices: [{ id: 'a', label: 'Excess stock' }, { id: 'b', label: 'A route' }], correctChoiceId: 'a', explanation: 'Too much stock uses space and money.', visual: 'COUNT' },
  { id: 'green', category: 'sustainability', prompt: 'What can cut delivery emissions?', choices: [{ id: 'a', label: 'Join nearby deliveries' }, { id: 'b', label: 'Send empty vans' }], correctChoiceId: 'a', explanation: 'Fewer journeys use less fuel.', visual: 'GREEN' },
  { id: 'robot', category: 'technology', prompt: 'What can a warehouse robot do?', choices: [{ id: 'a', label: 'Sort packages' }, { id: 'b', label: 'Write stories' }], correctChoiceId: 'a', explanation: 'Robots can move and sort items.', visual: 'ROBOT' },
  { id: 'customer', category: 'flow', prompt: 'Who uses the product?', choices: [{ id: 'a', label: 'The customer' }, { id: 'b', label: 'The loading dock' }], correctChoiceId: 'a', explanation: 'The customer receives and uses the product.', visual: 'USE' },
  { id: 'data', category: 'technology', prompt: 'Why use supply-chain data?', choices: [{ id: 'a', label: 'Make better plans' }, { id: 'b', label: 'Make boxes heavy' }], correctChoiceId: 'a', explanation: 'Data helps teams plan stock, routes, and timing.', visual: 'DATA' },
  { id: 'factory', category: 'roles', prompt: 'Where are products made?', choices: [{ id: 'a', label: 'A factory' }, { id: 'b', label: 'A checkout' }], correctChoiceId: 'a', explanation: 'Factories turn materials into finished products.', visual: 'MAKE' },
  { id: 'forecast', category: 'technology', prompt: 'What can a forecast help predict?', choices: [{ id: 'a', label: 'Customer demand' }, { id: 'b', label: 'The weather only' }], correctChoiceId: 'a', explanation: 'Demand forecasts help businesses prepare the right stock.', visual: 'PLAN' },
  { id: 'ship', category: 'transport', prompt: 'Which carries goods across oceans?', choices: [{ id: 'a', label: 'A delivery bike' }, { id: 'b', label: 'A cargo ship' }], correctChoiceId: 'b', explanation: 'Cargo ships move large loads across oceans.', visual: 'SHIP' },
  { id: 'reuse', category: 'sustainability', prompt: 'Which choice creates less waste?', choices: [{ id: 'a', label: 'Reuse boxes' }, { id: 'b', label: 'Throw out boxes' }], correctChoiceId: 'a', explanation: 'Reusing boxes keeps useful material in circulation.', visual: 'REUSE' },
  { id: 'quality', category: 'roles', prompt: 'What checks products work well?', choices: [{ id: 'a', label: 'Quality control' }, { id: 'b', label: 'A parking sign' }], correctChoiceId: 'a', explanation: 'Quality checks help catch problems before products ship.', visual: 'CHECK' },
  { id: 'lastmile', category: 'transport', prompt: 'What is the last mile?', choices: [{ id: 'a', label: 'Final trip to you' }, { id: 'b', label: 'A factory machine' }], correctChoiceId: 'a', explanation: 'The last mile is the final delivery to the customer.', visual: 'FINAL' },
  { id: 'barcode', category: 'technology', prompt: 'What can a barcode identify?', choices: [{ id: 'a', label: 'A product' }, { id: 'b', label: 'A road' }], correctChoiceId: 'a', explanation: 'Barcodes help teams identify and track products.', visual: 'SCAN' },
  { id: 'air', category: 'transport', prompt: 'Which is usually fastest for far-away urgent goods?', choices: [{ id: 'a', label: 'Air freight' }, { id: 'b', label: 'A slow boat' }], correctChoiceId: 'a', explanation: 'Air freight is fast, though it can use more energy.', visual: 'AIR' },
  { id: 'repair', category: 'sustainability', prompt: 'What helps products last longer?', choices: [{ id: 'a', label: 'Repair them' }, { id: 'b', label: 'Replace them fast' }], correctChoiceId: 'a', explanation: 'Repairing products can reduce waste and new materials.', visual: 'FIX' },
  { id: 'truck', category: 'transport', prompt: 'What moves goods between nearby cities?', choices: [{ id: 'a', label: 'A truck' }, { id: 'b', label: 'A bookshelf' }], correctChoiceId: 'a', explanation: 'Trucks are flexible for road deliveries.', visual: 'TRUCK' },
  { id: 'safety', category: 'warehouse', prompt: 'What keeps a warehouse safe?', choices: [{ id: 'a', label: 'Clear walkways' }, { id: 'b', label: 'Boxes in every path' }], correctChoiceId: 'a', explanation: 'Clear walkways help people and equipment move safely.', visual: 'SAFE' },
]

export function validateQuestions(items: Question[]): void {
  const ids = new Set<string>()
  items.forEach((question) => {
    if (ids.has(question.id)) throw new Error(`Duplicate question id: ${question.id}`)
    ids.add(question.id)
    if (question.choices.length !== 2) throw new Error(`Question ${question.id} must have exactly two choices`)
    if (!question.choices.some((choice) => choice.id === question.correctChoiceId)) throw new Error(`Question ${question.id} has an invalid correct choice`)
  })
}

validateQuestions(questions)

const demoOrders = [
  {
    orderNumber: "10481",
    buyerName: "Emma Peeters",
    model: "Ford Puma",
    status: "Onderweg naar de garage",
    expectedArrival: "18 oktober 2026"
  },
  {
    orderNumber: "10723",
    buyerName: "Lucas Janssens",
    model: "Ford Explorer",
    status: "In productie",
    expectedArrival: "Nog niet bekend"
  },
  {
    orderNumber: "10916",
    buyerName: "Noor De Smet",
    model: "Ford Kuga",
    status: "Vertraagd bij transport",
    expectedArrival: "29 oktober 2026"
  }
];

let currentOrders = demoOrders;

const normalise = (value) => String(value ?? "").trim().toLocaleLowerCase("nl-BE");

export function isValidOrderNumber(orderNumber) {
  return /^\d{5}$/.test(String(orderNumber ?? "").trim());
}

export function findOrder(orderNumber, buyerName) {
  const wantedOrder = normalise(orderNumber);
  const wantedName = normalise(buyerName);
  if (!isValidOrderNumber(wantedOrder)) return null;

  return currentOrders.find(
    (order) => normalise(order.orderNumber) === wantedOrder && normalise(order.buyerName) === wantedName
  ) ?? null;
}

export function replaceOrders(orders) {
  if (!Array.isArray(orders) || orders.length === 0) {
    throw new Error("Het bestand bevat geen bruikbare bestellingen.");
  }
  currentOrders = orders;
}

export function getOrderCount() {
  return currentOrders.length;
}

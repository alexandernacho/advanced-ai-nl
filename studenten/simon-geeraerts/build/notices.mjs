export function collectionNotice(expectedArrival) {
  if (expectedArrival === "Nog niet bekend") return "";

  return [
    "Let op: dit is de verwachte aankomstdatum bij de garage, geen leverings- of afhaaldatum.",
    "De verkoper neemt contact met u op om een datum voor de levering aan u vast te leggen.",
    "De uiteindelijke planning hangt onder meer af van een eventuele ombouw, de reiniging, nummerplaten en papieren."
  ].join(" ");
}

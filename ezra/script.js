const width = 10;
const height = 7;

const start = { x: 0, y: 6 };
const shelves = {
  A: { x: 2, y: 1 },
  D: { x: 6, y: 2 },
  R: { x: 3, y: 5 },
  M: { x: 8, y: 1 },
};
const bays = {
  1: { x: 9, y: 0 },
  2: { x: 9, y: 2 },
  3: { x: 9, y: 4 },
  4: { x: 9, y: 6 },
};
const obstacles = [
  { x: 4, y: 1 },
  { x: 4, y: 2 },
  { x: 4, y: 3 },
  { x: 7, y: 4 },
  { x: 1, y: 4 },
];

const exampleProgram = `MOVE E
MOVE E
MOVE N
MOVE N
MOVE N
MOVE N
MOVE N
TAKE A
MOVE S
MOVE S
MOVE S
MOVE S
MOVE E
TAKE R
MOVE N
MOVE N
MOVE E
MOVE E
MOVE E
TAKE D
MOVE E
MOVE E
MOVE S
MOVE S
MOVE S
MOVE S
DROP 4`;

const grid = document.querySelector("#warehouse-grid");
const programInput = document.querySelector("#program");
const statusText = document.querySelector("#status");
const cargoText = document.querySelector("#cargo");
const runLog = document.querySelector("#run-log");
const runButton = document.querySelector("#run-program");
const stepButton = document.querySelector("#step-program");
const resetButton = document.querySelector("#reset-world");
const loadExampleButton = document.querySelector("#load-example");
const commandButtons = document.querySelectorAll(".command-chip");

let worker = { ...start };
let cargo = [];
let delivered = [];
let stepIndex = 0;
let cells = [];

function sameSpot(a, b) {
  return a.x === b.x && a.y === b.y;
}

function keyFor(spot) {
  return `${spot.x},${spot.y}`;
}

function itemAt(spot) {
  return Object.entries(shelves).find(([, place]) => sameSpot(place, spot));
}

function bayAt(spot) {
  return Object.entries(bays).find(([, place]) => sameSpot(place, spot));
}

function isObstacle(spot) {
  return obstacles.some((obstacle) => sameSpot(obstacle, spot));
}

function buildGrid() {
  grid.innerHTML = "";
  cells = [];

  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const cell = document.createElement("div");
      cell.className = "cell";
      cell.dataset.coord = `${x},${y}`;
      cell.dataset.key = keyFor({ x, y });
      grid.appendChild(cell);
      cells.push(cell);
    }
  }
}

function render() {
  cells.forEach((cell) => {
    const [x, y] = cell.dataset.key.split(",").map(Number);
    const spot = { x, y };
    const shelf = itemAt(spot);
    const bay = bayAt(spot);

    cell.className = "cell";
    cell.textContent = "";

    if (sameSpot(spot, start)) {
      cell.classList.add("start");
      cell.textContent = "Start";
    }

    if (isObstacle(spot)) {
      cell.classList.add("obstacle");
      cell.textContent = "";
    }

    if (shelf && !delivered.includes(shelf[0]) && !cargo.includes(shelf[0])) {
      cell.classList.add("shelf");
      cell.textContent = shelf[0];
    }

    if (bay) {
      cell.classList.add("bay");
      cell.textContent = `Bay ${bay[0]}`;
    }

    if (sameSpot(spot, worker)) {
      cell.classList.add("worker");
      const workerToken = document.createElement("span");
      workerToken.className = "worker-token";
      workerToken.textContent = cargo.length ? cargo.join("") : "W";
      cell.textContent = "";
      cell.appendChild(workerToken);
    }
  });

  cargoText.textContent = cargo.length ? cargo.join(", ") : "empty";
}

function log(message, kind = "") {
  const item = document.createElement("li");
  item.textContent = message;
  if (kind) {
    item.className = kind;
  }
  runLog.appendChild(item);
}

function setStatus(message) {
  statusText.textContent = message;
}

function resetWorld(keepProgram = true) {
  worker = { ...start };
  cargo = [];
  delivered = [];
  stepIndex = 0;
  runLog.innerHTML = "";
  setStatus("Ready. The worker is waiting at Start.");
  if (!keepProgram) {
    programInput.value = exampleProgram;
  }
  render();
}

function parseProgram() {
  return programInput.value
    .split("\n")
    .map((line) => line.trim().toUpperCase())
    .filter((line) => line && !line.startsWith("#"));
}

function insertCommand(command) {
  const editorIsFocused = document.activeElement === programInput;
  if (!editorIsFocused) {
    programInput.selectionStart = programInput.value.length;
    programInput.selectionEnd = programInput.value.length;
  }

  const needsNewlineBefore =
    programInput.value.length > 0 &&
    programInput.selectionStart > 0 &&
    programInput.value[programInput.selectionStart - 1] !== "\n";
  const insertText = `${needsNewlineBefore ? "\n" : ""}${command}\n`;
  const cursorStart = programInput.selectionStart;
  const cursorEnd = programInput.selectionEnd;

  programInput.setRangeText(insertText, cursorStart, cursorEnd, "end");
  programInput.focus();
  stepIndex = 0;
  setStatus(`Added ${command} to the program.`);
}

function fail(message) {
  const cell = cells.find((candidate) => candidate.dataset.key === keyFor(worker));
  if (cell) {
    cell.classList.remove("error");
    window.requestAnimationFrame(() => cell.classList.add("error"));
  }
  setStatus(message);
  log(message, "bad");
  return false;
}

function runCommand(command) {
  const parts = command.split(/\s+/);
  const verb = parts[0];
  const noun = parts[1];

  if (verb === "MOVE") {
    const next = { ...worker };
    if (noun === "N") next.y -= 1;
    if (noun === "E") next.x += 1;
    if (noun === "S") next.y += 1;
    if (noun === "W") next.x -= 1;

    if (!["N", "E", "S", "W"].includes(noun)) {
      return fail(`I do not know how to ${command}. Try MOVE N, E, S, or W.`);
    }
    if (next.x < 0 || next.x >= width || next.y < 0 || next.y >= height) {
      return fail("The worker bumped into the warehouse wall.");
    }
    if (isObstacle(next)) {
      return fail("The worker cannot move through an obstacle.");
    }

    worker = next;
    log(`Moved ${noun}.`);
    render();
    return true;
  }

  if (verb === "TAKE") {
    const shelf = itemAt(worker);
    if (!shelf || shelf[0] !== noun) {
      return fail(`There is no item ${noun || ""} on this square.`);
    }
    if (cargo.includes(noun) || delivered.includes(noun)) {
      return fail(`Item ${noun} is already handled.`);
    }
    cargo.push(noun);
    log(`Picked up item ${noun}.`);
    render();
    return true;
  }

  if (verb === "DROP") {
    const bay = bayAt(worker);
    if (!bay || bay[0] !== noun) {
      return fail(`The worker is not at Truck Bay ${noun || ""}.`);
    }
    if (cargo.length === 0) {
      return fail("The worker has no cargo to drop.");
    }

    delivered.push(...cargo);
    log(`Dropped ${cargo.join(", ")} at Truck Bay ${noun}.`, "good");
    cargo = [];
    render();

    const orderDone = ["A", "D", "R"].every((item) => delivered.includes(item));
    if (orderDone && noun === "4") {
      setStatus("Order complete. A, D, and R are at Truck Bay 4.");
      log("Order complete.", "good");
    }
    return true;
  }

  return fail(`Unknown command: ${command}`);
}

function stepProgram() {
  const commands = parseProgram();
  if (stepIndex >= commands.length) {
    setStatus("No more commands to run.");
    return false;
  }

  const command = commands[stepIndex];
  stepIndex += 1;
  setStatus(`Running line ${stepIndex}: ${command}`);
  return runCommand(command);
}

function runProgram() {
  resetWorld(true);
  const commands = parseProgram();

  for (let index = 0; index < commands.length; index += 1) {
    stepIndex = index;
    if (!stepProgram()) {
      return;
    }
  }

  if (!["A", "D", "R"].every((item) => delivered.includes(item))) {
    setStatus("Program finished, but the order is not complete yet.");
  }
}

runButton.addEventListener("click", runProgram);
stepButton.addEventListener("click", stepProgram);
resetButton.addEventListener("click", () => resetWorld(true));
loadExampleButton.addEventListener("click", () => resetWorld(false));
commandButtons.forEach((button) => {
  button.addEventListener("click", () => insertCommand(button.dataset.command));
});

buildGrid();
resetWorld(false);

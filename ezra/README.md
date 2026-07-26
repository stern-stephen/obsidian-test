# Ezra

Ezra is a tiny warehouse-programming game for learning simple programs with an LLM.

Open `index.html` in a browser. The worker starts in the lower-left corner of the warehouse. The order is:

```text
Send items A, D, and R to Truck Bay 4.
```

## First language

The first version supports one command per line:

```text
MOVE N
MOVE E
MOVE S
MOVE W
TAKE A
DROP 4
```

Blank lines are ignored. Lines that start with `#` are comments.

## Ideas for the next round

- Add `REPEAT 4` blocks.
- Add a `GO TO A` helper command and compare it with hand-written moves.
- Let the player design new warehouse maps.
- Add levels with different orders and obstacles.
- Ask an LLM to write a program, then debug it together when it bumps into a wall.

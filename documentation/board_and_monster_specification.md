# Board and Monster Specification

## Monster Specification
 Each player starts the game with one of each `monster_type`, with their `length`s given below:

| `monster_type` | length | Origin |
|----------------|--------|--------|
| **Nessie** | 5 | Scottish |
| **Ogopogo** | 4 | Canadian |
| **Inkanyamba** | 3 | South African |
| **Lariousauro** | 3 | Italian |
| **Muyso** | 2 | Columbian |

## Board Specification
 Each player has two `10`x`10` boards that can be displayed to them. Their primary board showing their own monsters with the hits and misses of their opponent, and their target board with their hits and misses taken against their opponent.

 On the board, `board_piece`s are signified as follows:

| `board_piece` | character |
|---------------|:---------:|
| **monster** | M |
| **hit** | X |
| **miss** | / |
 **Note:** the `monster board_piece` is only displayed when it has **not** yet been hit

 The board is labeled from left to right with the numbers `0` to `9` and from top to bottom with the letters `A` to `J`.

## Sample Board

|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** |||M|X|X|/|||||
| **B** ||/|||/||||/||
| **C** |||||M|||/|||
| **D** ||/|/||M||||X||
| **E** |||/||M|/||/|X|/|
| **F** |/||M|/|M||||/||
| **G** ||/|M||||/||||
| **H** |||M||x|x|x||||
| **I** |/|/|M|/|||/|/|||
| **J** |||M|||/||||/|

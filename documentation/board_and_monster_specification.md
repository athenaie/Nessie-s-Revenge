# Map and Monster Specification

## Monster Specification
 Each player starts the game with one monster of each `monster_id`:

| `monster_id` | monster_name | length | Origin |
|--------------|----------------|--------|--------|
| **0000** | Nessie | 5 | Scottish |
| **0001** | Ogopogo | 4 | Canadian |
| **0010** | Inkanyamba | 3 | South African |
| **0011** | Lariousauro | 3 | Italian |
| **0100** | Muyso | 2 | Columbian |

## map Specification
 Each player has two `10`x`10` maps that can be displayed to them. Their primary map showing their own monsters with the hits and misses of their opponent, and their target map with their hits and misses taken against their opponent.

 On the map, `map_piece`s are signified as follows:

| `map_piece` | character |
|---------------|:---------:|
| **monster** | M |
| **hit** | X |
| **miss** | / |
 **Note:** the `monster map_piece` is only displayed when it has **not** yet been hit

 The map is labeled from left to right with the numbers `0` to `9` and from top to bottom with the letters `A` to `J`.

## Sample map

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

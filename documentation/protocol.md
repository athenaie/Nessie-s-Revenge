# Message Formats

## Client Messages

There are two types of message formats sent from the client. The first byte of each message identifies the `message_type`.

| `message_type` value | message type |
|:--------------------:|--------------|
| 0 | Place Monster Message |
| 1 | Shoot Message |

### Place Monster Message
This message is sent to inform the server of the clients' attempt to place a monster on the board.


| field | c-type | size | description |
|-------|--------|------|-------------|
| `message_type` | u char | 1 byte | monster placement messages have type 0 |
| `player_id` | u char | 1 byte | player's id number, identifies client |
| `start_coordinate_x` | u char | 1 byte | the x coordinate where the monster starts |
| `start_coordinate_y` | u char | 1 byte | the y coordinate where the monster starts |
| `end_coordinate_x` | u char | 1 byte | the x coordinate where the monster ends |
| `end_coordinate_y` | u char | 1 byte | the y coordinate where the monster  ends |
| **Total** | | 6 bytes | |


### Shoot Message
This message is sent to inform the server of the clients' attempt to shoot at a target position.

| field | c-type | size | description |
|-------|--------|------|-------------|
| `message_type` | u char | 1 byte | monster placement messages have type 1 |
| `player_id` | u char | 1 byte | player's id number, identifies client |
| `target_coord_x` | u char | 1 byte | the x coordinate of the target cell |
| `target_coord_y` | u char | 1 byte | the y coordinate of the target cell |
| **Total** | | 4 bytes | |

## Server Messages
There are two types of message formats sent from the client. The first byte of each message identifies the `message_type`.

| `message_type` value | message type |
|:--------------------:|--------------|
| 0 | Invalid Action Message |
| 1 | Map Message |

### Invalid Move Message
Message sent when a player tries to do an action that is invalid. It includes an event that is the result of the attempted action. This is only sent to the player who attempted the action. Since no action occurs, no map is sent.

| field | c-type | size | description |
|-------|--------|------|-------------|
| `message_type` | u char | 1 byte | map messages are of type 0 |
| `event_type` | u short | 2 bytes | event that resulted based on client message |
| **Total** | | 3 bytes | |

| `event_type` value | event type |
|:------------------:|------------|
| 0001 | Invalid row coordinate |
| 0010 | Invalid column coordinate |
| 0011 | Invalid coordinates |
| 0100 | Coordinates are not on a line |
| 0101 | No remaining monsters of length |
| 0110 | Monster placement overlap |
| 1001 | Invalid target coordinates |
| 1010 | Target already fired upon |

### Map Message
The server holds the only official copy of the boards, so after each successful action by a player, the server will send a new map to each player, along with the event.

| field | c-type | size | description |
|-------|--------|------|-------------|
| `message_type` | u char | 1 byte | map messages are of type 1 |
| `event_type` | u short | 2 bytes | event that resulted based on client message |
| `monster_id` | u char | 1 byte | Monster id, not used for 'missed' messages.
| `row_value` | int | 4 bytes * 10 | This value will be translated into the value of each cell |
| **Total** | | 44 bytes | |

| `event_type` value | event type |
|:------------------:|------------|
| 000 | You missed |
| 001 | You hit |
| 010 | You sunk |
| 011 | You won |
| 100 | Opponent missed |
| 101 | Opponent hit |
| 110 | Opponent sunk |
| 111 | Opponent won |

#### Row Values
Each row is sent as an int, and each cell is represented by two bits.
The first two bits are for row[0], the next to bits are for row[1], etc., so only the bottom 20 bits are used.
Each `cell_type` has its own two bit code.

| `cell_type` value | cell type |
|:-----------------:|-------------|
| 00 | water |
| 01 | miss |
| 10 | monster |
| 11 | hit |

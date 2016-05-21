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
| `player_id` | u short | 2 bytes | player's id number, identifies client |
| `start_coordinate_x` | u char | 2 byte | the x coordinate where the monster starts |
| `start_coordinate_y` | u char | 1 byte | the y coordinate where the monster starts |
| `end_coordinate_x` | u char | 1 byte | the x coordinate where the monster starts |
| `end_coordinate_y` | u char | 1 byte | the y coordinate where the monster starts |
| **Total** | | 8 bytes | |


### Shoot Message
This message is sent to inform the server of the clients' attempt to shoot at a target position.

| field | c-type | size | description |
|-------|--------|------|-------------|
| `message_type` | u char | 1 byte | monster placement messages have type 1 |
| `player_id` | u short | 2 bytes | player's id number, identifies client |
| `target_coord_x` | u char | 2 bytes | the x coordinate where the monster starts |
| `target_coord_y` | u char | 1 byte | the y coordinate where the monster starts |
| **Total** | | 6 bytes | |

## Server Messages

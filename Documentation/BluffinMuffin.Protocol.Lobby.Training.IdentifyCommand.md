# Lobby Training : Identify

This page is about the "Identification" part of the Lobby in Training Mode. For more information on this mode, see the [LobbyTraining]({Link:LobbyTraining}) section.

In training mode, you must **identify** yourself. This action puts a unique name to your Tcp Connection for the server. This name will be used as your playername on every table that you will play.

## IdentifyCommand

### Command Schema

```json
{
  "title": "Schema for IdentifyCommand",
  "type": "BluffinMuffin.Protocol.Lobby.Training.IdentifyCommand",
  "properties": {
    "CommandName": {
      "description": "Always contains 'IdentifyCommand' to distinguish the command from others.",
      "type": "string"
    },
    "Name": {
      "description": "The name you want to have on the server !",
      "type": "string"
    }
  }
}
```

### Example

## IdentifyCommand

### Command Schema

```json
{
  "title": "Schema for IdentifyResponse",
  "type": "BluffinMuffin.Protocol.Lobby.Training.IdentifyResponse",
  "properties": {
    "CommandName": {
      "description": "Always contains 'IdentifyResponse' to distinguish the command from others.",
      "type": "string"
    },
    "Ok": {
      "description": "Indicates if the identification was successful",
      "type": "bool"
    },
    "Command": {
      "type": "BluffinMuffin.Protocol.Lobby.Training.IdentifyCommand",
      "properties": {
        "CommandName": {
          "description": "Always contains 'IdentifyCommand' to distinguish the command from others.",
          "type": "string"
        },
        "Name": {
          "description": "The name you want to have on the server !",
          "type": "string"
        }
      }
    }
  }
}
```

### Example

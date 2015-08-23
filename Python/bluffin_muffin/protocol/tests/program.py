import json

from protocol import CommandDecoder

__author__ = 'ericmas001@gmail.com'

def _print_json(str):
    j = json.loads(str)
    command = CommandDecoder.decode(j)
    # print(command)
    if json.dumps(j, sort_keys=True,indent=4, separators=(',', ': ')) == json.dumps(json.loads(command.encode()), sort_keys=True,indent=4, separators=(',', ': ')):
        print('\033[94m' + command.__str__())
    else:
        # print('')
        print('\033[91m' + command.__str__())
        # print(json.dumps(j, sort_keys=True,indent=4, separators=(',', ': ')))
        # print(json.dumps(json.loads(command.encode()), sort_keys=True,indent=4, separators=(',', ': ')))

_print_json('{  "CommandName": "DisconnectCommand"}')
_print_json('{  "CommandName": "IdentifyCommand",  "Name": "SpongeBob"}')
_print_json('{  "CommandName": "IdentifyResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Command": {    "CommandName": "IdentifyCommand",    "Name": "SpongeBob"  }}')
_print_json('{  "CommandName": "IdentifyResponse",  "Success": false,  "MessageId": "NameAlreadyUsed",  "Message": "The name SpongeBob was already used!",  "Command": {    "CommandName": "IdentifyCommand",    "Name": "SpongeBob"  }}')
_print_json('{  "CommandName": "CreateTableCommand",  "Params": {    "TableName": "Bikini Bottom",    "GameType": "Holdem",    "Variant": "Texas Hold\'em",    "MinPlayersToStart": 2,    "MaxPlayers": 10,    "WaitingTimes": {      "AfterPlayerAction": 500,      "AfterBoardDealed": 500,      "AfterPotWon": 2500    },    "MoneyUnit": 10,    "Lobby": {      "OptionType": "QuickMode",      "StartingAmount": 1500    },    "Blind": {      "OptionType": "Blinds",      "MoneyUnit": 10    },    "Limit": {      "OptionType": "NoLimit"    }  }}')
_print_json('{  "CommandName": "CreateTableResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "IdTable": 42,  "Command": {    "CommandName": "CreateTableCommand",    "Params": {      "TableName": "Bikini Bottom",      "GameType": "Holdem",      "Variant": "Texas Hold\'em",      "MinPlayersToStart": 2,      "MaxPlayers": 10,      "WaitingTimes": {        "AfterPlayerAction": 500,        "AfterBoardDealed": 500,        "AfterPotWon": 2500      },      "MoneyUnit": 10,      "Lobby": {        "OptionType": "QuickMode",        "StartingAmount": 1500      },      "Blind": {        "OptionType": "Blinds",        "MoneyUnit": 0      },      "Limit": {        "OptionType": "NoLimit"      }    }  }}')
_print_json('{  "CommandName": "JoinTableCommand",  "TableId": 42}')
_print_json('{  "CommandName": "JoinTableResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Command": {    "CommandName": "JoinTableCommand",    "TableId": 42  }}')
_print_json('{  "CommandName": "LeaveTableCommand",  "TableId": 42}')
_print_json('{  "CommandName": "ListTableCommand",  "LobbyTypes": [    "QuickMode",    "RegisteredMode"  ]}')
_print_json('{  "CommandName": "ListTableResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Tables": [    {      "IdTable": 42,      "NbPlayers": 6,      "PossibleAction": "Join",      "Params": {        "TableName": "Bikini Bottom",        "GameType": "Holdem",        "Variant": "Texas Hold\'em",        "MinPlayersToStart": 2,        "MaxPlayers": 10,        "WaitingTimes": {          "AfterPlayerAction": 500,          "AfterBoardDealed": 500,          "AfterPotWon": 2500        },        "MoneyUnit": 10,        "Lobby": {          "OptionType": "QuickMode",          "StartingAmount": 1500        },        "Blind": {          "OptionType": "Antes",          "MoneyUnit": 10        },        "Limit": {          "OptionType": "NoLimit"        }      }    },    {      "IdTable": 84,      "NbPlayers": 3,      "PossibleAction": "Leave",      "Params": {        "TableName": "Pokemon World",        "GameType": "Holdem",        "Variant": "Texas Hold\'em",        "MinPlayersToStart": 2,        "MaxPlayers": 10,        "WaitingTimes": {          "AfterPlayerAction": 500,          "AfterBoardDealed": 500,          "AfterPotWon": 2500        },        "MoneyUnit": 10,        "Lobby": {          "OptionType": "QuickMode",          "StartingAmount": 1500        },        "Blind": {          "OptionType": "Blinds",          "MoneyUnit": 10        },        "Limit": {          "OptionType": "NoLimit"        }      }    }  ],  "Command": {    "CommandName": "ListTableCommand",    "LobbyTypes": [      "QuickMode",      "RegisteredMode"    ]  }}')
_print_json('{  "CommandName": "CheckCompatibilityCommand",  "ImplementedProtocolVersion": "2.0.0"}')
_print_json('{  "CommandName": "CheckCompatibilityResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "ImplementedProtocolVersion": "2.0.0",  "SupportedLobbyTypes": [    "QuickMode",    "RegisteredMode"  ],  "Rules": [    {      "GameType": "Holdem",      "Name": "Texas Hold\'em",      "MinPlayers": 2,      "MaxPlayers": 10,      "AvailableLimits": [        "NoLimit"      ],      "DefaultLimit": "NoLimit",      "AvailableBlinds": [        "Blinds",        "Antes",        "None"      ],      "DefaultBlind": "Blinds",      "CanConfigWaitingTime": true,      "AvailableLobbys": [        "QuickMode",        "RegisteredMode"      ]    }  ],  "Command": {    "CommandName": "CheckCompatibilityCommand",    "ImplementedProtocolVersion": "2.0.0"  }}')
_print_json('{  "CommandName": "AuthenticateUserCommand",  "Username": "ericmas001",  "Password": "0nc3Up0nAT1m3"}')
_print_json('{  "CommandName": "AuthenticateUserResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Command": {    "CommandName": "AuthenticateUserCommand",    "Username": "ericmas001",    "Password": "0nc3Up0nAT1m3"  }}')
_print_json('{  "CommandName": "CheckDisplayExistCommand",  "DisplayName": "Sponge Bob"}')
_print_json('{  "CommandName": "CheckDisplayExistResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Exist": true,  "Command": {    "CommandName": "CheckDisplayExistCommand",    "DisplayName": "Sponge Bob"  }}')
_print_json('{  "CommandName": "CheckUserExistCommand",  "Username": "ericmas001"}')
_print_json('{  "CommandName": "CheckUserExistResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Exist": true,  "Command": {  "CommandName": "CheckUserExistCommand",  "Username": "ericmas001"}}')
_print_json('{  "CommandName": "CreateUserCommand",  "Username": "ericmas001",  "Password": "0nc3Up0nAT1m3",  "Email": "ericmas001@hotmail.com",  "DisplayName": "Sponge Bob"}')
_print_json('{  "CommandName": "CreateUserResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Command": {    "CommandName": "CreateUserCommand",    "Username": "ericmas001",    "Password": "0nc3Up0nAT1m3",    "Email": "ericmas001@hotmail.com",    "DisplayName": "Sponge Bob"  }}')
_print_json('{  "CommandName": "GetUserCommand"}')
_print_json('{  "CommandName": "GetUserResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "Email": "ericmas001@hotmail.com",  "DisplayName": "Sponge Bob",  "Money": 42000.42,  "Command": {    "CommandName": "GetUserCommand"  }}')
_print_json('{  "CommandName": "BetTurnEndedCommand",  "TableId": 42,  "Round": "Flop",  "PotsAmounts": [    4200,    420  ]}')
_print_json('{  "CommandName": "BetTurnStartedCommand",  "TableId": 42,  "Round": "Flop",  "BettingRoundId": 1,  "Cards": [    "2s",    "Kh",    "5d"  ]}')
_print_json('{  "CommandName": "DiscardRoundEndedCommand",  "TableId": 42,  "CardsDiscarded": [    {      "NoSeat": 7,      "NbCardsDiscarded": 3    }  ]}')
_print_json('{  "CommandName": "DiscardRoundStartedCommand",  "TableId": 42,  "MinimumCardsToDiscard": 0,  "MaximumCardsToDiscard": 5}')
_print_json('{  "CommandName": "GameEndedCommand",  "TableId": 42}')
_print_json('{  "CommandName": "GameStartedCommand",  "TableId": 42,  "NeededBlindAmount": 10}')
_print_json('{  "CommandName": "PlayerHoleCardsChangedCommand",  "TableId": 42,  "NoSeat": 7,  "Cards": [    "4h",    "Qs"  ],  "PlayerState": "Playing"}')
_print_json('{  "CommandName": "PlayerJoinedCommand",  "TableId": 42,  "PlayerName": "Sponge Bob"}')
_print_json('{  "CommandName": "PlayerLeftCommand",  "TableId": 42,  "PlayerName": "Sponge Bob"}')
_print_json('{  "CommandName": "PlayerTurnBeganCommand",  "TableId": 42,  "NoSeat": 7,  "MinimumRaiseAmount": 6}')
_print_json('{  "CommandName": "PlayerTurnEndedCommand",  "TableId": 42,  "NoSeat": 7,  "TotalPlayedMoneyAmount": 420,  "TotalSafeMoneyAmount": 4200,  "TotalPot": 42000,  "ActionTakenType": "Call",  "ActionTakenAmount": 42,  "PlayerState": "Playing"}')
_print_json('{  "CommandName": "PlayerWonPotCommand",  "TableId": 42,  "NoSeat": 7,  "PotId": 0,  "WonAmount": 420,  "TotalPotAmount": 1000,  "TotalPlayerMoney": 4200,  "WinningCards": [    "5s",    "5c",    "5d",    "Ad",    "Ks"  ],  "WinningHand": "ThreeOfAKind"}')
_print_json('{  "CommandName": "SeatUpdatedCommand",  "TableId": 42,  "Seat": {    "NoSeat": 7,    "Player": {      "NoSeat": 7,      "Name": "SpongeBob",      "MoneySafeAmnt": 1000,      "MoneyBetAmnt": 42,      "HoleCards": [        "2s",        "Ah"      ],      "State": "Playing",      "IsShowingCards": true    },    "SeatAttributes": [      "CurrentPlayer",      "BigBlind"    ]  }}')
_print_json('{  "CommandName": "TableClosedCommand",  "TableId": 42}')
_print_json('{  "CommandName": "TableInfoCommand",  "TableId": 42,  "Params": {    "TableName": "Bikini Bottom",    "GameType": "Holdem",    "Variant": "Texas Hold\'em",    "MinPlayersToStart": 2,    "MaxPlayers": 10,    "WaitingTimes": {      "AfterPlayerAction": 500,      "AfterBoardDealed": 500,      "AfterPotWon": 2500    },    "MoneyUnit": 10,    "Lobby": {      "OptionType": "QuickMode",      "StartingAmount": 1500    },    "Blind": {      "OptionType": "Blinds",      "MoneyUnit": 0    },    "Limit": {      "OptionType": "NoLimit"    }  },  "TotalPotAmount": 42000,  "PotsAmount": [    4200,    420  ],  "BoardCards": [    "2s",    "Kh",    "5d"  ],  "Seats": [    {      "NoSeat": 7,      "Player": {        "NoSeat": 7,        "Name": "SpongeBob",        "MoneySafeAmnt": 1000,        "MoneyBetAmnt": 42,        "HoleCards": [          "2s",          "Ah"        ],        "State": "Playing",        "IsShowingCards": true      },      "SeatAttributes": [        "CurrentPlayer",        "BigBlind"      ]    }  ],  "GameHasStarted": true}')
_print_json('{  "CommandName": "PlayerDiscardActionCommand",  "TableId": 42,  "CardsDiscarded": [    "2s",    "7c",    "Kh"  ]}')
_print_json('{  "CommandName": "PlayerPlayMoneyCommand",  "TableId": 42,  "AmountPlayed": 42}')
_print_json('{  "CommandName": "PlayerSitInCommand",  "TableId": 42,  "NoSeat": 7,  "MoneyAmount": 4200}')
_print_json('{  "CommandName": "PlayerSitInResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "NoSeat": 7,  "TableId": 42,  "Command": {    "CommandName": "PlayerSitInCommand",    "TableId": 42,    "NoSeat": 7,    "MoneyAmount": 4200  }}')
_print_json('{  "CommandName": "PlayerSitOutCommand",  "TableId": 42}')
_print_json('{  "CommandName": "PlayerSitOutResponse",  "Success": true,  "MessageId": "None",  "Message": "",  "TableId": 42,  "Command": {    "CommandName": "PlayerSitOutCommand",    "TableId": 42  }}')


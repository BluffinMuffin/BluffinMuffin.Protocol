﻿using BluffinMuffin.Protocol.DataTypes;
using BluffinMuffin.Protocol.DataTypes.Enums;

namespace BluffinMuffin.Protocol.Tests.DataTypes
{

    public static class PlayerInfoMock
    {
        public static PlayerInfo Dora()
        {
            return new PlayerInfo()
            {
                State = PlayerStateEnum.Playing,
                NoSeat = 7,
                Name = "Dora",
                HoleCards = new[] { GameCardMock.AceOfClubs().ToString(), GameCardMock.JackOfHearts().ToString() },
                IsShowingCards = true,
                MoneyBetAmnt = 84,
                MoneySafeAmnt = 126
            };
        }

        public static PlayerInfo Diego()
        {
            return new PlayerInfo()
            {
                State = PlayerStateEnum.Zombie,
                NoSeat = 6,
                Name = "Diego",
                HoleCards = new[] { GameCardMock.TenOfDiamonds().ToString(), GameCardMock.TwoOfSpades().ToString() },
                IsShowingCards = true,
                MoneyBetAmnt = 21,
                MoneySafeAmnt = 63
            };
        }
    }
}

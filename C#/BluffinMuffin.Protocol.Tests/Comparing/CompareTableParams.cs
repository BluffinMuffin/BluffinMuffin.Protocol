﻿using BluffinMuffin.Protocol.DataTypes;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BluffinMuffin.Protocol.Tests.Comparing
{
    public static class CompareTableParams
    {
        public static void Compare(TableParams t, TableParams dt)
        {
            Assert.AreEqual(t.GetType(), dt.GetType());

            Assert.AreEqual(t.GameType, dt.GameType);
            Assert.AreEqual(t.MoneyUnit, dt.MoneyUnit);
            Assert.AreEqual(t.MaxPlayers, dt.MaxPlayers);
            Assert.AreEqual(t.MinPlayersToStart, dt.MinPlayersToStart);
            Assert.AreEqual(t.TableName, dt.TableName);
            Assert.AreEqual(t.Variant, dt.Variant);
            CompareBlindOptions.Compare(t.Blind, dt.Blind);
            CompareLimitOptions.Compare(t.Limit, dt.Limit);
            CompareLobbyOptions.Compare(t.Lobby, dt.Lobby);
            CompareConfigurableWaitingTimes.Compare(t.WaitingTimes, dt.WaitingTimes);
        }
    }
}

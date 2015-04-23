﻿using System.Linq;
using BluffinMuffin.Protocol.DataTypes;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BluffinMuffin.Protocol.Tests.Comparing
{
    public static class CompareSeatInfo
    {
        public static void Compare(SeatInfo s, SeatInfo ds)
        {
            Assert.IsFalse(s.SerializableAttributes.Except(ds.SerializableAttributes).Any());
            Assert.AreEqual(s.SerializableAttributes.Length, ds.SerializableAttributes.Length);
            Assert.AreEqual(s.NoSeat, ds.NoSeat);
            ComparePlayerInfo.Compare(s.Player, ds.Player);
        }
    }
}

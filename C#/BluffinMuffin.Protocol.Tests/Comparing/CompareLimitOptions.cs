﻿using BluffinMuffin.Protocol.DataTypes;
using BluffinMuffin.Protocol.DataTypes.Options;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BluffinMuffin.Protocol.Tests.Comparing
{
    public static class CompareLimitOptions
    {
        public static void Compare(LimitOptions l, LimitOptions dl)
        {
            Assert.AreEqual(l.GetType(), dl.GetType());
        }
    }
}

﻿using BluffinMuffin.Protocol.DataTypes.Enums;
using Com.Ericmas001.Net.Protocol;
using Com.Ericmas001.Net.Protocol.Options;

namespace BluffinMuffin.Protocol.DataTypes
{
    /// <summary>
    /// The type of blinds the table uses (none, blinds, antes) 
    /// </summary>
    public abstract class BlindOptions : IOption<BlindTypeEnum>
    {
        /// <summary>
        /// The Money unit. Should always be equal to the moneyUnit of the table.
        /// </summary>
        [ExampleValue(10)]
        public int MoneyUnit { get; set; }
        /// <summary>
        /// The type of blinds used for the table
        /// </summary>
        public abstract BlindTypeEnum OptionType { get; }
    }
}
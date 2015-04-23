﻿namespace BluffinMuffin.Protocol.DataTypes
{
    public class ConfigurableWaitingTimes
    {
        public int AfterPlayerAction { get; set; }
        public int AfterBoardDealed { get; set; }
        public int AfterPotWon { get; set; }

        public ConfigurableWaitingTimes()
        {
            AfterPlayerAction = 0;
            AfterBoardDealed = 0;
            AfterPotWon = 0;
        }
    }
}

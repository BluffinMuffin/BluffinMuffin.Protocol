﻿namespace BluffinMuffin.Protocol.Game
{
    public class PlayerTurnBeganCommand : AbstractGameCommand
    {
        public int PlayerPos { get; set; }
        public int LastPlayerNoSeat { get; set; }
        public int MinimumRaise { get; set; }
    }
}

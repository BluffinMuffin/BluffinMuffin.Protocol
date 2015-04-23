﻿namespace BluffinMuffin.Protocol.Lobby.Career
{
    public class GetUserResponse : AbstractBluffinReponse<GetUserCommand>
    {
        public string Email { get; set; }
        public string DisplayName { get; set; }
        public double Money { get; set; }

        public GetUserResponse(GetUserCommand command)
            : base(command)
        {
        }
    }
}

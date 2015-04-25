# Lobby QuickMode

The lobby has two modes: ***Quick mode*** and ***Registered mode***. This Section is about ***Quick mode***. The Quick mode is a mode where the money is given to the player when he enters the table. For example, If the amount is set to 1500 on Table1, every player will receive 1500$ to play with when they will enter the Table.

<p align=center><img src="https://github.com/Ericmas001/BluffinMuffin.Protocol/blob/master/Documentation/Sequence%20Diagrams/BluffinMuffin.Protocol.Lobby.QuickMode.png" alt="Sequence Diagram"></p>

 * **[IdentifyCommand](https://github.com/Ericmas001/BluffinMuffin.Protocol/blob/master/Documentation/BluffinMuffin.Protocol.Lobby.QuickMode.IdentifyCommand.md)** 

   First, in this mode, you must **Identify** yourself. This action puts a unique name to your Tcp Connection for the server. This name will be used as your playername on every table that you will play.
   
 * **[SupportedRulesCommand](https://github.com/Ericmas001/BluffinMuffin.Protocol/blob/master/Documentation/BluffinMuffin.Protocol.Lobby.SupportedRulesCommand.md)** *(Optional)*

   If it's the first time, it's a good idea to ask what are the **Supported Rules** of the current server to know what can and can't be done !

 * **[CreateTableCommand](https://github.com/Ericmas001/BluffinMuffin.Protocol/blob/master/Documentation/BluffinMuffin.Protocol.Lobby.CreateTableCommand.md)** *(Optional)*

   If you want to create a new table, you can send a **Create Table** command to the server with all the parameters that you want on your table

 * **[ListTablesCommand](https://github.com/Ericmas001/BluffinMuffin.Protocol/blob/master/Documentation/BluffinMuffin.Protocol.Lobby.ListTablesCommand.md)** *(Optional)*

   You can also ask for the **List of Tables** currently open on the server.

 * **[JoinTableCommand](https://github.com/Ericmas001/BluffinMuffin.Protocol/blob/master/Documentation/BluffinMuffin.Protocol.Lobby.JoinTableCommand.md)** 

   To **Join a Table**, you must specify an ID that you got creating a table or listing tables.
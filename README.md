# python_Based_Reverse_Shell

Attacker's system runs a listener (server).

Victim's system connects back (client) and listens for commands.


Attacker (Server) <--- Connection --- Victim (Client)
          ↑                           ↓
      Sends Command               Executes Command
          ↓                           ↑
    Reads Output <--- Sends Result ---|

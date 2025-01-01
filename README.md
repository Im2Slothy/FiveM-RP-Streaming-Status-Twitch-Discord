# OBS-Browser-Src-Sync-With-Discord


**Description:**
This is a real-time status display system designed for law enforcement role-play communities. This project integrates a Discord bot with a web interface to dynamically update and display the status of officers, including rank, name, department, current status, active calls, and status color. The system allows for easy management of officer statuses through Discord commands, which are then reflected on a web dashboard.

**Features:**
- **Real-time Updates:** Automatically updates the web interface every 5 seconds.
- **Discord Integration:** Use simple commands in Discord to update officer statuses.
- **Customizable Statuses:** Set predefined or custom statuses using Discord commands.
- **Color-Coded Statuses:** Visual color indicators for different status types (e.g., green for available, red for pursuit).
- **Persistent Storage:** Uses JSON for storing current status, allowing for state persistence across restarts.

**Usage:**
- Run the Flask server to host the web interface.
- Start the Discord bot to manage statuses from within Discord.
- Access the web interface to view real-time status updates.

**Setup:**
1. Clone the repository.
2. Install dependencies (Flask for the web server, discord.py for the bot).
3. Configure your Discord bot token in the script.
4. Run the application.


**License:**
MIT

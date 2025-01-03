# FiveM RP Streaming Status

A real-time status display system designed for law enforcement role-play communities. This project integrates Discord and Twitch chat with a web interface to dynamically update and display officer statuses. Perfect for streamers who want to show their current law enforcement RP status through OBS Browser Source.


[Example](https://ibb.co/VtMGpPH)

## Features

- **Real-time Updates:** Web interface automatically refreshes every 5 seconds
- **Multi-Platform Integration:**
  - Discord bot for command-based status updates
  - Twitch chat integration for live stream status management
  - Web interface for OBS Browser Source display
- **Customizable Status System:**
  - Predefined status commands for quick updates
  - Custom status options for specific scenarios
  - Color-coded status indicators (green for available, red for pursuit, etc.)
- **Persistent Storage:** Status data saved in JSON format for persistence across restarts
- **Profile Display:**
  - Officer rank and name
  - Department affiliation
  - Current status and active calls
  - Color-coded visual indicators

## Prerequisites

- Python 3.7 or higher
- Discord Bot Token (from Discord Developer Portal)
- Twitch OAuth Token (https://twitchtokengenerator.com/)
- Basic understanding of OBS Browser Source setup

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OBS-Browser-Src-Sync-With-Discord.git
cd OBS-Browser-Src-Sync-With-Discord
```

2. Install required Python packages:
```bash
pip install flask
pip install discord.py
pip install twitchio
```

3. Configure tokens:

   a. **For Twitch Token:**
   - Visit https://twitchtokengenerator.com/
   - Select 'Custom Scope Token'
   - Select the following scopes:
     - `chat:read`
     - `chat:edit`
   - Generate and copy the token
   - Replace `oauth:TOKENDONTDELETEoauth!` in `app.py` with your token

   b. **For Discord Token:**
   - Go to https://discord.com/developers/applications
   - Create a new application
   - Go to the Bot section
   - Create a bot and copy the token
   - Replace the Discord token in `app.py` with your token
   - Enable MESSAGE CONTENT INTENT in the Bot settings

4. Customize the profile picture:
   - Replace `static/face.png` with your desired profile picture
   - Keep the same filename or update the reference in `index.html`

## Usage

### Starting the Application

1. Run using the batch file:
   - Double click `start.bat`
   
   OR

2. Run manually:
```bash
python app.py
```

### Discord Commands

- `!p80` - Set status to 10-80 (Vehicle Pursuit)
- `!p70` - Set status to 10-70 (Foot Pursuit)
- `!p11` - Set status to 10-11 (Traffic Stop)
- `!p8` - Set status to 10-8 (Available)
- `!p7` - Set status to 10-7 (Off-Duty)
- `!p71` - Set status to 10-71 (Supervisor Request)

Custom commands:
- `!setrank [rank]` - Update officer rank
- `!setname [name]` - Update officer name
- `!setdepartment [dept]` - Update department
- `!setstatus [status]` - Set custom status
- `!setcall [details]` - Update current call details

### Twitch Commands
Same commands as Discord, usable in Twitch chat.

### OBS Setup

1. Add a Browser Source to your scene
2. Set the URL to `http://localhost:5000`
3. Recommended properties:
   - Width: 800
   - Height: 200
   - Enable refresh browser when scene becomes active

## Troubleshooting

- If the web interface shows no data, check that:
  - The Flask server is running (check console for errors)
  - The `status.json` file exists and is readable
  - You're using the correct URL in OBS
- If commands aren't working:
  - Verify bot tokens are correct
  - Check console for any error messages
  - Ensure bot has proper permissions in Discord

## License

This project is licensed under the MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Created by Chris "Slothy"
- Inspired by law enforcement role-play communities
- Made for streamers, by a streamer [FOLLOW ME ON TWITCH](https://www.twitch.tv/im2slothy)

## Support

For issues, questions, or suggestions, please open an issue on GitHub.

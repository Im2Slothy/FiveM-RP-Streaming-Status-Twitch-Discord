from flask import Flask, render_template, jsonify
import discord
from discord.ext import commands
from twitchio.ext import commands as tcommands
import json
import os
import logging
import threading
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')

# Store current status in memory (could be moved to a database for persistence)
current_status = {
    "rank": "LSPD Officer",
    "name": "John D. | 1234",
    "department": "Los Santos Police Department",
    "status": "10-8",
    "current_call": "No Active Calls",
    "color": "green"

}


# Twitch bot setup
class TwitchBot(tcommands.Bot):
    def __init__(self):
        super().__init__(
            token='oauth:edit',
            prefix='!',
            initial_channels=['urchannel']
        )

    async def event_ready(self):
        logger.info(f'Logged in to Twitch as | {self.nick}')

    @tcommands.command()
    async def p80(self, ctx):
        current_status['status'] = "10-80"
        current_status['current_call'] = "Vehicle Pursuit in Progress"
        current_status['color'] = "red"
        await ctx.send("Status updated to 10-80 - Vehicle Pursuit")
        save_status()

    @tcommands.command()
    async def p70(self, ctx):
        current_status['status'] = "10-70"
        current_status['current_call'] = "Foot Pursuit in Progress"
        current_status['color'] = "red"
        await ctx.send("Status updated to 10-70 - Foot Pursuit")
        save_status()

    @tcommands.command()
    async def p11(self, ctx):
        current_status['status'] = "10-11"
        current_status['current_call'] = "Traffic Stop"
        current_status['color'] = "yellow"
        await ctx.send("Status updated to 10-11 - Traffic Stop")
        save_status()

    @tcommands.command()
    async def p8(self, ctx):
        current_status['status'] = "10-8"
        current_status['current_call'] = "Awaiting Calls"
        current_status['color'] = "green"
        await ctx.send("Status updated to 10-8 - Available")
        save_status()

    @tcommands.command()
    async def p7(self, ctx):
        current_status['status'] = "10-7"
        current_status['current_call'] = "Off-Duty"
        current_status['color'] = "green"
        await ctx.send("Status updated to 10-7 - Off Duty")
        save_status()

    @tcommands.command()
    async def p71(self, ctx):
        current_status['status'] = "10-71"
        current_status['current_call'] = "LSPD Assist \\ Supervisor Request"
        current_status['color'] = "blue"
        await ctx.send("Status updated to 10-71 - Supervisor Request")
        save_status()

    @tcommands.command()
    async def setstatus(self, ctx, new_status):
        """Set the current status (10-97, 10-98, etc)"""
        current_status['status'] = new_status
        await ctx.send(f"Status updated to {new_status}")
        logger.info(f"Status updated to {new_status}")
        save_status()

    @tcommands.command()
    async def setcall(self, ctx, *, call_details):
        """Set the current call details"""
        current_status['current_call'] = call_details
        await ctx.send(f"Call updated to {call_details}")
        logger.info(f"Call updated to {call_details}")
        save_status()

















# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logger.info(f'Bot is ready and logged in as {bot.user}')

#PRESET FILLINS#
@bot.command()
async def lspd1(ctx):
    current_status['rank'] = "Master Police Officer"
    current_status['name'] = "Chris Hibbert | 1006"
    current_status['department'] = "Los Santos Police Department"
    await ctx.send(f"Stuff is set to preset lspd1")
    save_status()

@bot.command()
async def set1(ctx):
    current_status['rank'] = "SWAT Supervisor"
    current_status['name'] = "Chris Hibbert | 1006"
    current_status['department'] = "LSPD SWAT"
    await ctx.send("Set!")
    save_status()

@bot.command()
async def set2(ctx):
    current_status['rank'] = "MCD Detective"
    current_status['name'] = "Chris Hibbert | 1006"
    current_status['department'] = "LSPD MCD"
    await ctx.send("Set!")
    save_status()

@bot.command()
async def set3(ctx):
    current_status['rank'] = "SCU Detective"
    current_status['name'] = "Chris Hibbert | 1006"
    current_status['department'] = "LSPD SCU"
    await ctx.send("Set!")
    save_status()

@bot.command()
async def set4(ctx):
    current_status['rank'] = "MDD Protective Services"
    current_status['name'] = "Chris Hibbert | 1006"
    current_status['department'] = "LSPD MDD"
    await ctx.send("Set!")
    save_status()

@bot.command()
async def civ(ctx):
    current_status['rank'] = "Civilian"
    current_status['name'] = "Grayson Steele"
    current_status['department'] = "Civilian Life"
    await ctx.send("Set!")

    save_status()

#END#






#CUSTOM STATUS / UPDATES#

@bot.command()
async def setrank(ctx, *, new_rank):
    current_status['rank'] = new_rank
    await ctx.send(f"Status updated to {new_rank}")
    logger.info(f"Rank updated to {new_rank}")
    save_status()

@bot.command()
async def setname(ctx, *, set_name):
    current_status['name'] = set_name
    await ctx.send(f"Status updated to {set_name}")
    logger.info(f"Name updated to {set_name}")
    save_status()

@bot.command()
async def setdepartment(ctx, *, set_demartment):
    current_status['department'] = set_demartment
    await ctx.send(f"Status updated to {set_demartment}")
    logger.info(f"Department updated to {set_demartment}")
    save_status()

@bot.command()
async def setstatus(ctx, new_status):
    """Set the current status (10-97, 10-98, etc)"""
    current_status['status'] = new_status
    await ctx.send(f"Status updated to {new_status}")
    logger.info(f"Status updated to {new_status}")
    save_status()

@bot.command()
async def setcall(ctx, *, call_details):
    """Set the current call details"""
    current_status['current_call'] = call_details
    await ctx.send(f"Call updated to {call_details}")
    logger.info(f"Call updated to {call_details}")
    
    save_status()





#10 codes#
@bot.command()
async def p80(ctx):  # 10-80
    current_status['status'] = "10-80"
    current_status['current_call'] = "Vehicle Pursuit in Progress"
    current_status['color'] = "red"  # We'll add a color field to control the styling
    await ctx.send("Status updated to 10-80 - Vehicle Pursuit")
    save_status()

@bot.command()
async def p70(ctx):  # 10-70
    current_status['status'] = "10-70"
    current_status['current_call'] = "Foot Pursuit in Progress"
    current_status['color'] = "red"
    await ctx.send("Status updated to 10-70 - Foot Pursuit")
    save_status()

@bot.command()
async def p11(ctx):  # 10-11
    current_status['status'] = "10-11"
    current_status['current_call'] = "Traffic Stop"
    current_status['color'] = "yellow"
    await ctx.send("Status updated to 10-11 - Traffic Stop")
    save_status()

@bot.command()
async def p8(ctx):  # 10-8
    current_status['status'] = "10-8"
    current_status['current_call'] = "Awaiting Calls"
    current_status['color'] = "green"
    await ctx.send("Status updated to 10-8 - Available")
    save_status()

@bot.command()
async def p7(ctx):  # 10-7
    current_status['status'] = "10-7"
    current_status['current_call'] = "Off-Duty"
    current_status['color'] = "green"
    await ctx.send("Status updated to 10-7 - Off Duty")
    save_status()

@bot.command()
async def p71(ctx):  # 10-71
    current_status['status'] = "10-71"
    current_status['current_call'] = "LSPD Assist \\ Supervisor Request"
    current_status['color'] = "blue"
    await ctx.send("Status updated to 10-71 - Supervisor Request")
    save_status()

#END#








def save_status():
    """Save current status to a file"""
    try:
        with open('status.json', 'w') as f:
            json.dump(current_status, f)
        logger.info("Status file updated successfully")
    except Exception as e:
        logger.error(f"Error saving status file: {e}")

# Flask routes
@app.route('/')
def index():
    return render_template('index.html', status=current_status)

@app.route('/status')
def get_status():
    return jsonify(current_status)

if __name__ == '__main__':
    # Load saved status if exists
    if os.path.exists('status.json'):
        try:
            with open('status.json', 'r') as f:
                current_status.update(json.load(f))
            logger.info("Loaded existing status from file")
        except Exception as e:
            logger.error(f"Error loading status file: {e}")
    
    # Create and start the Twitch bot
    twitch_bot = TwitchBot()
    threading.Thread(target=lambda: twitch_bot.run()).start()
    logger.info("Twitch bot thread started")

    # Start the Discord bot in a separate thread
    import threading
    threading.Thread(target=lambda: bot.run('EDIT')).start()
    logger.info("Discord bot thread started")
    
    # Start Flask app
    logger.info("Starting Flask app")
    app.run(port=5000)

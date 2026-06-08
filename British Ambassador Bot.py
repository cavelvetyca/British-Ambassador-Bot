import os
import random
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("Missing TOKEN environment variable")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def pick(items):
    return random.choice(items)

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print(f"British Ambassador Bot logged in as {bot.user}")
    print(f"Synced {len(synced)} global command(s)")

@bot.tree.command(name="tea", description="Receive an official cup of tea")
async def tea(interaction: discord.Interaction):
    await interaction.response.send_message(pick([
        "☕ The Embassy has issued you tea. Do not spill it.",
        "Tea status: boiling.",
        "Your tea has been approved by Parliament.",
        "Milk first? The Embassy is watching."
    ]))

@bot.tree.command(name="weather", description="Check British weather")
async def weather(interaction: discord.Interaction):
    await interaction.response.send_message(pick([
        "🌧 Rain.",
        "🌧 More rain.",
        "🌧 Sideways rain.",
        "🌧 Scheduled rain with a chance of disappointment.",
        "☁️ It is aggressively cloudy."
    ]))

@bot.tree.command(name="queue", description="Join the official queue")
async def queue(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"You are number **{random.randint(1000, 999999)}** in the queue. Please remain calm."
    )

@bot.tree.command(name="apologize", description="Receive an official apology")
async def apologize(interaction: discord.Interaction):
    await interaction.response.send_message(pick([
        "The Embassy apologizes for a minor incident between 1066 and today.",
        "We deeply regret the inconvenience, but not enough to fix it.",
        "Sorry. Properly sorry. Embassy-level sorry.",
        "A strongly worded apology has been dispatched by pigeon."
    ]))

@bot.tree.command(name="biscuit", description="Get a biscuit verdict")
async def biscuit(interaction: discord.Interaction):
    await interaction.response.send_message(pick([
        "Digestive biscuit approved.",
        "Rich Tea detected. Structurally weak but culturally important.",
        "Hobnob rating: dangerously dunkable.",
        "Biscuit dunk time: 2.7 seconds. Any longer is treason."
    ]))

@bot.tree.command(name="permit", description="Request a permit")
async def permit(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Your permit request requires another permit to request the permit."
    )

@bot.tree.command(name="license", description="Check license requirements")
async def license(interaction: discord.Interaction):
    await interaction.response.send_message(
        "You need a license for that license."
    )

@bot.tree.command(name="dentist", description="Ask about dentists")
async def dentist(interaction: discord.Interaction):
    await interaction.response.send_message(
        "The Embassy cannot confirm nor deny these allegations."
    )

@bot.tree.command(name="fishandchips", description="Order fish and chips")
async def fishandchips(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Fish and chips rating: **{random.randint(1, 5)}/5**. Vinegar level: **excessive**."
    )

@bot.tree.command(name="beans", description="Count the beans")
async def beans(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Beans counted: **{random.randint(12, 5000)}**. Toast status: damp."
    )

@bot.tree.command(name="museum", description="Inspect a museum artifact")
async def museum(interaction: discord.Interaction):
    await interaction.response.send_message(
        "This artifact has been relocated to a museum for safekeeping. Definitely."
    )

@bot.tree.command(name="train", description="Check train status")
async def train(interaction: discord.Interaction):
    await interaction.response.send_message(pick([
        "The train has been delayed.",
        "The train has been cancelled.",
        "The replacement bus has also been cancelled.",
        "The train exists conceptually."
    ]))

@bot.tree.command(name="monarchy", description="Check monarchy status")
async def monarchy(interaction: discord.Interaction):
    await interaction.response.send_message("Monarchy status: operational.")

@bot.tree.command(name="roadworks", description="Check roadworks")
async def roadworks(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Roadworks detected. Estimated completion: **{random.randint(2030, 2099)}**."
    )

@bot.tree.command(name="britishmoment", description="Generate a British moment")
async def britishmoment(interaction: discord.Interaction):
    await interaction.response.send_message(pick([
        "Bit rainy innit.",
        "Fancy a cuppa?",
        "Could be worse.",
        "Queue starts over there.",
        "The train has been delayed.",
        "We regret everything and nothing simultaneously.",
        "That requires a form.",
        "The Embassy is mildly concerned."
    ]))

@bot.tree.command(name="why", description="Ask why")
async def why(interaction: discord.Interaction):
    await interaction.response.send_message("Because the British Ambassador Bot said so.")

@bot.tree.command(name="commands", description="Show commands")
async def commands_list(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**British Ambassador Bot Commands**\n"
        "/tea, /weather, /queue, /apologize, /biscuit, /permit, /license,\n"
        "/dentist, /fishandchips, /beans, /museum, /train, /monarchy,\n"
        "/roadworks, /britishmoment, /why, /commands"
    )
    
app = Flask(__name__)

@app.route("/")
def home():
    return "GDBot is running."

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

bot.run(TOKEN)

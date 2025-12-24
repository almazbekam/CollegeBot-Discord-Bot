import discord
from discord.ext import commands
import datetime
import json
import random

# ---------- Bot Setup ----------
intents = discord.Intents.default()
intents.message_content = True  # required for reading commands
intents.members = True          # needed for welcome messages
bot = commands.Bot(command_prefix='!', intents=intents)

# ---------- Data Setup ----------
try:
    with open('data.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    user_data = {}

# ---------- Fallback Quotes ----------
quotes_list = [
    "The expert in anything was once a beginner. – Helen Hayes",
    "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
    "Do something today that your future self will thank you for.",
    "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
    "Education is the passport to the future, for tomorrow belongs to those who prepare for it today. – Malcolm X",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Hard work beats talent when talent doesn't work hard. – Tim Notke",
    "Dream big and dare to fail. – Norman Vaughan",
    "The beautiful thing about learning is that no one can take it away from you. – B.B. King"
]

# ---------- Events ----------
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    system_channel = member.guild.system_channel
    if system_channel:
        await system_channel.send(
            f"Welcome to the server, {member.mention}! Use !help to see college prep commands."
        )

# ---------- Commands ----------

# Quote command
@bot.command()
async def quote(ctx):
    quote_to_send = random.choice(quotes_list)
    await ctx.send(quote_to_send)

# Add a study task
@bot.command()
async def schedule(ctx, *, task):
    user_id = str(ctx.author.id)
    if user_id not in user_data:
        user_data[user_id] = {"tasks": [], "points": 0}

    user_data[user_id]["tasks"].append({"task": task, "date": str(datetime.date.today())})

    with open('data.json', 'w') as f:
        json.dump(user_data, f, indent=4)

    await ctx.send(f"Task added, {ctx.author.mention}: {task}")

# Show tasks
@bot.command()
async def tasks(ctx):
    user_id = str(ctx.author.id)
    if user_id not in user_data or not user_data[user_id]["tasks"]:
        await ctx.send("You have no scheduled tasks.")
        return

    tasks_list_str = "\n".join([f"{i+1}. {t['task']} (added on {t['date']})"
                                for i, t in enumerate(user_data[user_id]["tasks"])])
    await ctx.send(f"Your tasks:\n{tasks_list_str}")

# Reminder for a specific task
@bot.command()
async def reminder(ctx, task_number: int):
    user_id = str(ctx.author.id)
    if user_id not in user_data or task_number <= 0 or task_number > len(user_data[user_id]["tasks"]):
        await ctx.send("Invalid task number.")
        return

    task = user_data[user_id]["tasks"][task_number - 1]["task"]

    await ctx.author.send(f"Reminder: {task}")
    await ctx.send(f"Reminder sent to your DMs, {ctx.author.mention}!")


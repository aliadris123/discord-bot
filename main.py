import discord

intents = discord.Intents.default()
intents.message_content = True 

client = discord.Client(intents=intents)

TARGET_CHANNEL_ID = 1543672815646023730

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == TARGET_CHANNEL_ID:
        await message.add_reaction("<:lost_left_wing:1543675295549235280>")
        await message.add_reaction("🔥")
        await message.add_reaction("<:lost_right_wing:1543675348091404389>")

client.run("MTU0MzE3NzQ4MTQ3MTY2MDE0Mg.GQSwz7.E_1aPsOCHF_8anq78mzo9PXa1THGk36hl-vfHY")
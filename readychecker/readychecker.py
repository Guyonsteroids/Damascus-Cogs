import asyncio

import discord
from redbot.core import commands


class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Ready", style=discord.ButtonStyle.green)
    async def confirm(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "Adding you to the ready list", ephemeral=True
        )
        self.value = True
        self.stop()

    @discord.ui.button(label="Ignore", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Ignoring readycheck", ephemeral=True)
        self.value = False
        self.stop()


class ReadyChecker(commands.Cog):
    """Checks which homies are ready tonight"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Check if your homies are ready")
    async def readycheck(self, ctx: commands.Context):
        """Check if your homies are ready"""
        readyhomies = []
        passes = 0
        message = await ctx.send("Checking if homies are ready")
        for mem in ctx.guild.members:
            passes += 1
            if mem.bot:
                pass
            # elif mem.id == ctx.author.id:
            # pass
            else:
                try:
                    view = Confirm()
                    readymsg = await mem.send(
                        "Will you be ready tonight?, You have 30s to reply", view=view
                    )
                    await asyncio.sleep(30)
                    if view.value:
                        readyhomies.append(mem.name)
                        await readymsg.edit(
                            content=f"Thank you for responding, I have informed {ctx.message.author.name}",
                            view=None,
                        )
                    else:
                        await readymsg.edit(
                            content="You did not respond withing the given timeframe",
                            view=None,
                        )

                except discord.errors.Forbidden:
                    pass

            await message.edit(
                content=f"Checking if homies are ready: {passes}/{len(ctx.guild.members)}"
            )

        if readyhomies is None:
            await message.edit(content=f"No homies are ready :(")
        else:
            await message.edit(content=f"Ready homies: {readyhomies}")

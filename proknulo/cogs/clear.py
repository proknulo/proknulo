from disnake.ext import commands
import disnake


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Очистить чат")
    async def clear(self, interaction, amount: int):
        role = interaction.guild.get_role(1124272149633437757)
        if role in interaction.author.roles and amount>4:
            embed = disnake.Embed(
                title="Clear",
                description=f"Очищено {amount} сообщений",
                color=disnake.Color.from_rgb(0, 245, 255),
            )
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.channel.purge(limit=amount)
        if role in interaction.author.roles and amount<=4:
            embed = disnake.Embed(
                title="Clear",
                description=f"Очищено {amount} сообщения",
                color=disnake.Color.from_rgb(0, 245, 255),
            )
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.channel.purge(limit=amount)
        else:
            clearembed = disnake.Embed(
                title="Clear",
                description=f"**{interaction.author.mention}, у Вас недостаточно прав**",
                color=disnake.Colour.from_rgb(0, 245, 255)
                       )
            clearembed.set_footer(
                text="Администрация сервера Proknulo",
                icon_url=self.bot.user.avatar.url)

            clearembed.set_thumbnail(
                url=self.bot.user.avatar.url
            )

            await interaction.response.send_message(embed=clearembed, ephemeral=True)
def setup(bot):
    bot.add_cog(Clear(bot))
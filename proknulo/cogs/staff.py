
import disnake
from disnake.ext import commands

class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def staff(self, ctx, member: disnake.Member = None):
        await ctx.message.delete()
        user = member or ctx.author
        embed = disnake.Embed(
            title=None,
            description="**Канал предназначен для общения модерации и получения тикетов**",
            color=disnake.Colour.from_rgb(0, 245, 255),
        )

        embed.set_author(
            name="Proknulo",
            icon_url=user.display_avatar.url,
        )
        embed.set_footer(
            text="Администрация сервера Proknulo",
            icon_url=self.bot.user.avatar.url,
        )

        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1057621189138329731/1192444945060081765/STAFF_1.gif?ex=65a919e5&is=6596a4e5&hm=66b247963d611b2516f872ebabe831835016629d56f36a638424b18e3b8c6e8a&")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Staff(bot))

import disnake
from disnake.ext import commands

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def embed(self, interaction):
        embed = disnake.Embed(
            title="Набор в STAFF",
            description="Нажмите на панель, чтобы подать заявку в STAFF",
            color=disnake.Colour.from_rgb(0, 245, 255),
        )

        embed.set_author(
            name="Proknulo",
            icon_url="https://cdn.discordapp.com/attachments/1057621189138329731/1193299191284375734/spray.jpg?ex=65ac3579&is=6599c079&hm=d69b0a3bf40d7782ad7d15bff5a0fda820d9d8e2c204c360344da4961177af63&",
        )
        embed.set_footer(
            text="Администрация сервера Proknulo",
            icon_url="https://cdn.discordapp.com/attachments/1057621189138329731/1193299191284375734/spray.jpg?ex=65ac3579&is=6599c079&hm=d69b0a3bf40d7782ad7d15bff5a0fda820d9d8e2c204c360344da4961177af63&",
        )

        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/1057621189138329731/1191372609804312616/IMG_7655.gif?ex=65a53334&is=6592be34&hm=ffcb29aaba9a7979983ba5952dea65a56bfc799f864b5c06a860b30d66667955&")


        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(embed(bot))
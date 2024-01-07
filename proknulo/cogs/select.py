import disnake
from disnake.ext import commands


class TicketModal(disnake.ui.Modal):
    def __init__(self, arg):
        global title, titl, components
        self.arg = arg  # arg - это аргумент, который передается в конструкторе класса TicketSelect
        """
        Также можно сделать так:
                components = [
            disnake.ui.TextInput(label="Ваше имя", placeholder="Введите ваше имя", custom_id="name"),
            disnake.ui.TextInput(label="Ваш возраст", placeholder="Введите ваш возраст", custom_id="age")
            disnake.ui.TextInput(
                label="Расскажите о себе и почему именно вы?",
                placeholder="Расскажи о себе здесь",
                custom_id="info",
                style=disnake.TextInputStyle.paragraph,
                min_length=10,
                max_length=500,
            )
        ]
        """
        if self.arg == "вопрос":
            components = [
                disnake.ui.TextInput(label="Вопрос", placeholder="Подробно все опишите", custom_id="info",
                                     style=disnake.TextInputStyle.paragraph),
            ]
            title = "Вопрос"
        if self.arg == "жалоба":
            components = [
                disnake.ui.TextInput(label="Жалоба", placeholder="Подробно все опишите", custom_id="info",
                                     style=disnake.TextInputStyle.paragraph),]
            title = "Жалоба"

        super().__init__(title=title, components=components, custom_id="complaintModal")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        info = interaction.text_values["info"]
        embed = disnake.Embed(color=0x2F3136, title="Запрос отправлен!")
        embed.description = f"{interaction.author.mention}, Благодарим вас за **обращение**! " \
                            f"Администрация **свяжется** с вами в ближайшее время."
        embed.set_thumbnail(url=interaction.author.display_avatar.url)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        channel = interaction.guild.get_channel(1122869772858699837)  # Вставить ID канала куда будут отправляться заявки
        if self.arg == "Жалоба":
            await channel.send(f"{self.arg} от {interaction.author.mention}: {info}")
        else:
           await channel.send(f"{self.arg} от {interaction.author.mention}: {info}")


class TicketSelect(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label="Тикет", value="вопрос", description="Задать интересующий вопрос"),
            disnake.SelectOption(label="Жалоба", value="жалоба", description="Оставить жалобу"),
        ]
        super().__init__(
            placeholder="Что Вас интересует", options=options, min_values=0, max_values=1, custom_id="quest"
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        if not interaction.values:
            await interaction.response.defer()
        else:
            await interaction.response.send_modal(TicketModal(interaction.values[0]))


class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False

    @commands.command()
    async def tickets(self, ctx):
        view = disnake.ui.View()
        view.add_item(TicketSelect())
        embed = disnake.Embed(
            title="Вопросы и жалобы",
            description="Нажмите на соответствующую панель",
            color=disnake.Colour.from_rgb(0, 245, 255),
        )

        embed.set_author(
            name="Proknulo",
            icon_url="https://cdn.discordapp.com/attachments/1057621189138329731/1193299191284375734/spray.jpg?ex=65ac3579&is=6599c079&hm=d69b0a3bf40d7782ad7d15bff5a0fda820d9d8e2c204c360344da4961177af63&",
        )
        embed.set_footer(
            text="Администрация сервера Proknulo",
            icon_url="https://cdn.discordapp.com/attachments/1057621189138329731/1193509947787460618/IMG_6190.jpg?ex=65acf9c1&is=659a84c1&hm=4c0705c315f5da00939621f5a53901c477bceae4e914fd62ddde213bff42dbb1&",
        )

        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/1057621189138329731/1191372609804312616/IMG_7655.gif?ex=65a53334&is=6592be34&hm=ffcb29aaba9a7979983ba5952dea65a56bfc799f864b5c06a860b30d66667955&")
        # Тут можно добавть эмбед с описанием ролей
        await ctx.message.delete()
        await ctx.send(embed=embed, view=view)

    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return

        view = disnake.ui.View(timeout=None)
        view.add_item(TicketSelect())
        self.bot.add_view(view,
                          message_id=1193581884597338233)  # Вставить ID сообщения, которое отправится после использования команды .tickets


def setup(bot):
    bot.add_cog(Ticket(bot))
import asyncio
import discord


class StatsMod:
    def __init__(
            self, ctx, client, empireMotto: str, empireName: str, country: str, updated: int, uuid: int, flag: str,
            created: str, lan: int, pop: int, factory: int,land: int, name: str, emp: str, rank: str, score: float,
            competitiveRank: str, gdp: int, balance: int, currency: str, coinz: int, tech: int, keys: int, badge1: str,
            badge2: str, badge3: str
    ):
        self.country = country  # emoji to flag from nation
        self.updated = updated  # hours since updated
        self.uuid = uuid  # Unique User Identifier
        self.flag = flag  # url to flag
        self.created = created  # usr nation created
        self.lan = lan  # total land user
        self.pop = pop  # total pop user
        self.factory = factory  # total processors held by user
        self.land = land  # usable land user
        self.name = name  # nation name user
        self.emp = emp  # "None" or number empire
        self.rank = rank  # user bot rank, i.e developer, user etc.
        self.score = score  # total score points user
        self.competitiveRank = competitiveRank  # rank name user
        self.gdp = gdp  # user by daily gdp
        self.balance = balance  # total user balance
        self.currency = currency  # 3 letter currency name
        self.coinz = coinz  # total coinz user
        self.tech = tech  # total tech user points
        self.keys = keys  # total keys user
        self.badge1 = badge1  # First Badge Slot
        self.badge2 = badge2  # Second Badge Slot
        self.badge3 = badge3  # Third Badge Slot
        self.empireName = empireName  # Empires Name
        self.empireMotto = empireMotto  # Empires Motto
        self.ctx = ctx  # context
        self.client = client  # united nations as a client

    async def UserMod(self):
        stats = discord.Embed(title="Statistics", colour=self.ctx.author.colour, timestamp=self.ctx.message.created_at)
        stats.set_thumbnail(url=self.flag)
        stats.set_footer(text="Israel is rightful Jewish land, Palestine doesnt exist.", icon_url=self.ctx.author.avatar_url)

        stats.add_field(
            name="📋 Basic Info:",
            value=f"📜 Name: {self.country} `{self.name}`\n"
                  f"📆 Date Founded: `{self.created}`\n"
                  f"🏅 Badges : \n`{self.badge1}`\n`{self.badge2}`\n`{self.badge3}`\n",
            inline=False
        )
        stats.add_field(
            name="🏎️ Competitive Info:\n",
            value=f"🔁 Last Updated: `{self.updated}`\n"
                  f"🎯 Competitive Score: {self.competitiveRank} | `{self.score}`\n"
                  f"🗺 Empire : `{self.empireName} - *{self.empireMotto}*`\n",
            inline=False
        )
        stats.add_field(
            name="💹 Economy:",
            value=f"💰 Balance: `{self.balance:,} {self.currency}`\n"
                  f"📈 Gross Domestic Product: `{self.gdp:,} {self.currency}`\n"
                  f"⚖ GDP Per Capita: `{self.gdp/self.pop:,} {self.currency}`\n"
                  f"🏗 Processors: `{self.factory:,}/50,000`\n"
                  f"🏢 Corporations : `{(self.lan - self.factory * 2 - self.land) / 2:,}`\n",
            inline=False
        )
        stats.add_field(
            name="🏙 Demographics:",
            value=f"👨‍👩‍👧‍👦 Population: `{self.pop:,}`\n"
                  f"🏡 Total Land Area: `{self.lan:,}km²`\n"
                  f"🏜 Usable Land: `{self.land:,}km²`\n"
                  f"🧑‍💼 Population Density : `{self.pop/self.lan:,}/km²`\n",
            inline=False
        )

        bal = discord.Embed(title="Balance", colour=self.ctx.author.colour, timestamp=self.ctx.message.created_at)
        bal.set_thumbnail(url=self.flag)
        bal.set_footer(text="Israel is an example of socialism done right.", icon_url=self.ctx.author.avatar_url)
        
        bal.add_field(
            name="💹 Economy:",
            value=f"💰 Balance: `{self.balance:,} {self.currency}`\n"
                  f"🔬 Research Points: `{self.tech:,}`\n"
                  f"🏢 Corporations: `{(self.lan - self.factory * 2 - self.land) / 2:,}`\n"
                  f"🏗 Processors : `{self.factory:,}/50,000`\n",
            inline=False
        )
        bal.add_field(
            name="🏦 Other:",
            value=f"👨‍👩‍👧‍👦 Population: {self.pop:,}\n"
                  f"🏜 Usable Land: {self.land:,}km²\n"
                  f"🗝 Keys: {self.keys:,}\n"
                  f"💎 Coinz : {self.coinz:,}\n",
            inline=False
        )

        message = await self.ctx.send(embed=stats)
        await message.add_reaction("📊")
        await message.add_reaction("💰")

        def check(react, usr):
            return usr == self.ctx.author and str(react.emoji) in "📊💰"

        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=30, check=check)

                if str(reaction.emoji) == "📊":
                    await message.edit(embed=stats)

                elif str(reaction.emoji) == "💰":
                    await message.edit(embed=bal)

                await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                embed = message.embeds[0]
                embed.add_field(name="Timed Out", value="Reaction menu has times out", inline=False)
                await message.edit(embed=embed)
                break

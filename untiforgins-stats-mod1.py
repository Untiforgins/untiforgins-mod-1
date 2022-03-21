import discord
from datetime import datetime


class StatsMod:
    def __init__(self, country: str, updated: int, uuid: int, flag: str, created: str, lan: int, pop: int, factory: int, land: int, emp: str, rank: str, score: float, competitiveRank: str, gdp: int, balance: int, currency: str, coinz: int, tech: int, keys: int, badge1: str, badge2: str, badge3: str):
        self.country = country
        self.updated = updated
        self.uuid = uuid
        self.flag = flag
        self.created = created
        self.lan = lan
        self.pop = pop
        self.factory = factory
        self.land = land
        self.emp = emp
        self.rank = rank
        self.score = score
        self.competitiveRank = competitiveRank
        self.gdp = gdp
        self.balance = balance
        self.currency = currency
        self.coinz = coinz
        self.tech = tech
        self.keys = keys
        self.badge1 = badge1
        self.badge2 = badge2
        self.badge3 = badge3

        def UserMod(self):
        embed = discord.Embed(title="Stats", colour=ctx.author.colour, timestamp=ctx.message.created_at,)
        embed.set_thumbnail(url=self.flag)
        embed.set_footer(text="Israel is rightful Jewish land, Palestine doesnt exist.")

        embed.add_field(name="Total Land", value=f"{(self.lan * 100000000):,}")
        embed.add_field(name="Usable Land", value=f"{(self.land * 100000000):,}")

        return embed

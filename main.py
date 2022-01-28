# Options
token = 'NzA3OTgxMzEyMzE2NjcwMDMy.XrQs-g.f5U5PHEemRDYZ2BtcTvSl89QZo4'
prefix = 'o!'

from discord.ext import commands
from commands import info_command
from commands import trl_command
from commands import yap_command
from commands import yt_command
from pytube import Playlist

client = commands.Bot(command_prefix=prefix, help_command=None)


@client.event
async def on_ready():
    print('Successfully launched')


@client.command()
async def info(ctx):
    await ctx.send(embed=info_command.embed_return(client))


@client.command()
async def trl(ctx, *, text):
    await ctx.send(embed=trl_command.embed_return(text))


@client.command()
async def yap(ctx, *, question):
    await ctx.send(embed=yap_command.embed_return(question))


@client.command()
async def play(ctx, *link):
    try:
        plist = Playlist(str(link))
        links = plist.video_urls
        for link in links:
            await yt_command.playing(ctx, link)
    except KeyError:
        await yt_command.playing(ctx, str(link))


@client.command()
async def stop(ctx):
    yt_command.stopping(player=ctx.guild.voice_client)


client.run(token)

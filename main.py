
from discord.ext import commands
from modules import info_command
from modules import trl_command
from modules import yap_command
from modules import yt_command
from modules import config
from pytube import Playlist
from pytube import Search

client = commands.Bot(command_prefix=config.parse_prefix(), help_command=None)


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
    await yt_command.stopping(ctx, player=ctx.guild.voice_client)


@client.command()
async def search(ctx, *, search_query):
    search_var = Search(search_query)
    video = search_var.results[0].video_id
    link = f'https://www.youtube.com/watch?v={video}'
    await play(ctx, link)


client.run(config.parse_token())

from pytube import YouTube
import pytube.exceptions
import discord
import time


def length(seconds):
    time_format = time.strftime("%H:%M:%S", time.gmtime(seconds))
    return time_format


async def playing(ctx, link):
    yt = YouTube(link)
    try:
        stream = yt.streams.get_audio_only()
    except pytube.exceptions.AgeRestrictedError:
        embed_obj = discord.Embed(description=f'"{yt.title}" cannot be played due to age restriction', color=0xe01b24)
        await ctx.send(embed=embed_obj)
        return

    stream.download(output_path='temp', filename=f'temp.{str(ctx.author.voice.channel.id)}')

    if ctx.author.voice.channel:
        if not ctx.guild.voice_client:
            player = await ctx.author.voice.channel.connect()
        else:
            player = ctx.guild.voice_client
        try:
            player.play(discord.FFmpegOpusAudio(source=f"temp/temp.{str(ctx.author.voice.channel.id)}"))
        except discord.errors.ClientException:
            embed_obj = discord.Embed(description="Already playing audio")
            await ctx.send(embed=embed_obj)
            return
    else:
        embed_obj = discord.Embed(description="Please connect to a voice channel", color=0xe01b24)
        await ctx.send(embed=embed_obj)
        return

    embed_obj = discord.Embed(title='YouTube', color=0xe01b24)
    embed_obj.add_field(name="Track", value=f'[{yt.title}]({yt.watch_url})', inline=True)
    embed_obj.add_field(name="Track Length", value=length(yt.length), inline=True)
    embed_obj.add_field(name="Request Author", value=ctx.author, inline=False)
    embed_obj.set_thumbnail(url=yt.thumbnail_url)
    await ctx.send(embed=embed_obj)


async def stopping(ctx, player):
    player.stop()
    embed_obj = discord.Embed(description=f'Stopped by {ctx.author}', color=0xe01b24)
    await ctx.send(embed=embed_obj)

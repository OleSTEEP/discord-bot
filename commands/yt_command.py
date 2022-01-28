from pytube import YouTube
import pytube.exceptions
import discord


async def playing(ctx, link):
    yt = YouTube(link)
    try:
        stream = yt.streams.get_audio_only()
    except pytube.exceptions.AgeRestrictedError:
        await ctx.send(f'"{yt.title}" cannot be played due to age restriction')
        return

    stream.download(output_path='downloads', filename='youtube_temp')

    if ctx.author.voice.channel:
        if not ctx.guild.voice_client:
            player = await ctx.author.voice.channel.connect()
        else:
            player = ctx.guild.voice_client
        try:
            player.play(discord.FFmpegOpusAudio(source="downloads/youtube_temp"))
        except discord.errors.ClientException:
            await ctx.send("Already playing audio.")
            return
    else:
        await ctx.send("Please connect to a voice channel.")
        return

    embed_obj = discord.Embed(title='YouTube', description=f'Playing "{yt.title}"')
    embed_obj.set_image(url=yt.thumbnail_url)
    await ctx.send(embed=embed_obj)


def stopping(player):
    player.stop()

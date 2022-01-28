from memory_profiler import memory_usage
import discord


def embed_return(client):
    embed_obj = discord.Embed(title='Info',
                              description=
                              f'Working... RAM Usage: {round(memory_usage()[0])} MB, ping: {round(client.latency * 1000)} ms')
    return embed_obj

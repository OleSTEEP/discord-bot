from memory_profiler import memory_usage
import discord


def embed_return(client):
    ram = round(memory_usage()[0])
    ping = round(client.latency * 1000)
    embed_obj = discord.Embed(title='Info',
                              description=f'Working... RAM Usage: {ram} MB, ping: {ping} ms')
    return embed_obj

from googletrans import Translator
import discord


def embed_return(text):
    translator = Translator()
    lang = text.split().pop()
    text = text.replace(lang, '')
    result = translator.translate(text, dest=lang)
    embed_obj = discord.Embed(title='Google Translate', description=f'{text} = {result.text}')
    embed_obj.set_footer(text=f'{result.src} → {result.dest}')
    return embed_obj

import config
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url=config.webhookurl)
# create embed object for webhook
embed = DiscordEmbed(title="message", description="message", color=242424)

# add embed object to webhook
webhook.add_embed(embed)
embed.set_image(url="https://metalhangar18.com/wp/ups/2020/11/saintedsinners-290x290.jpg")
response = webhook.execute()

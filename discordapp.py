# インストールした discord.pyとかこまごましたもの を読み込む
from email import message_from_bytes
import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# 設定
json_file = 'https://github.com/caprice1026-disc/bansho_alpha/blob/224dd2a6f1acbc4ebae9074dbd6103f3d124f892/oceanic-trees-351914-02037f6b9aa9.json'
file_name = 'oceanic-trees-351914-02037f6b9aa9.json'
sheet_name1 = 'シート1'
sheet_name2 = 'csv_sheet'
csv_file_name = 'spreadsheet/Davis.csv'

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# スプレッドシートにアクセス
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
gc = gspread.authorize(credentials)
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/16fnlcvGVutSfoCxsIGhVm1rCO1uoR3cMW26_puXFkEw/edit?usp=sharing')
wks = sh.get_worksheet(0)

# Botのアクセストークン]
TOKEN = '内緒♡　間違えて公開しちゃったけど変更済みです'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # banshoコマンド実行
    elif message.content == '/light':
          #乱数を作成
        import random
        LIGHT1 = random.randint(0,10)
        #どの行を取ってくるか選択
        val1 = wks.acell('A'+ str(LIGHT1)).value
        val2 = wks.acell('B'+ str(LIGHT1)).value
        val3 = wks.acell('C'+ str(LIGHT1)).value

        #ここから埋め込みスタート　上でvelを指定して渡す
        embed = discord.Embed(title=val1, colour=discord.Colour(0xe3d51d), url=val2, description="Created by 光野ひかる." )
        embed.set_image(url=val3)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/968179152425480272/993360991230374008/0225.png")
        embed.set_author(name="BANSHO LIGHT", url="https://opensea.io/collection/bansho-light")
        embed.set_footer(text="©光野ひかる", icon_url="https://cdn.discordapp.com/attachments/968179152425480272/993360991230374008/0225.png")
        embed.add_field(name=val1, value="Fully on chain data storage.Fully Painted by ArtistsMade in JAPAN ANIME ART", inline=True)
        await message.channel.send(embed=embed)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

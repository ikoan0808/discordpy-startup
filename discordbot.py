from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

import time
import requests
import json
import copy
from datetime import datetime, timedelta, timezone

bot.run(token)

Hololive = {
    "UCp6993wxpyDPHUpavwDFqgg": [
        "ときのそら",
        "https://yt3.ggpht.com/a/AATXAJzGvZJuJ92qM5WcfBcDZqPFSj_CGIEYp9VFmA=s288-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC-hM6YJuNYVAmUWxeIr9FeA": [
        "さくらみこ",
        "https://yt3.ggpht.com/a/AATXAJyKGBusDmf7stiwXDVORLo21xtnBj2YUHrPd-CxYA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCdn5BQ06XqgXoAxIhbqw5Rg": [
        "白上フブキ",
        "https://yt3.ggpht.com/a/AATXAJztvRXzNX8UtsaUZfLLBh32VBBwNPcvy_TklUjnWA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCQ0UDLQCjY0rmuxCDE38FGg": [
        "夏色まつり ",
        "https://yt3.ggpht.com/a/AATXAJw8RXWyEofFZFI5EwEb7lXDq3Cm6l0SThQxT9XG=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCD8HOxPs4Xvsm8H0ZxXGiBw": [
        "夜空メル",
        "https://yt3.ggpht.com/a/AATXAJxGYXGi2fgjHoYCSuqLzsh6p-CrlNvRTRFmZmK_=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC1CfXB_kRs3C-zaeTG3oGyg": [
        "赤井はあと",
        "https://yt3.ggpht.com/a/AATXAJw3IoOJZlLAn_Eyy0r6gJHR3vt64XHfuXCailaCPw=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCFTLzh12_nrtzqBPsTCqenA": [
        "アキロゼ",
        "https://yt3.ggpht.com/a/AATXAJz-Y3lEysu2wkT7AdTaPU77l938jwf2p2r8hi7e=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC1opHUrw8rvnsadT-iGp7Cg": [
        "湊あくあ",
        "https://yt3.ggpht.com/a/AATXAJxXeCPuSGxq-_NfKX4WSpCf7FtnOkPNzHd2s9Sh9g=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC1suqwovbL1kzsoaZgFZLKg": [
        "癒月ちょこ",
        "https://yt3.ggpht.com/a/AATXAJyy9e7DUSSfuWdROtr9oJxho6jVqSDhGdsRESDU=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC7fk0CB07ly8oSl0aqKkqFg": [
        "百鬼あやめ",
        "https://yt3.ggpht.com/a/AATXAJybvEUdsgDTZasoeAgVPHwDcWzmfLdngzWFcLx7=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCXTpFs_3PqI41qX2d9tL2Rw": [
        "紫咲シオン",
        "https://yt3.ggpht.com/a/AATXAJx2dQl8H1TG2HBy9bMCMP-nHxOVXALwAJz8MFS_rA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCvzGlP9oQwU--Y0r9id_jnA": [
        "大空スバル",
        "https://yt3.ggpht.com/a/AATXAJx_CMc_Ne4b93d6Hr3nMSqLbijvq6UxzPO8apsk=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCp-5t9SrOQwXMU7iIjQfARg": [
        "大神ミオ",
        "https://yt3.ggpht.com/a/AATXAJzFpyPB7LFGFq5DIX2x7pvIblA9Ksz99TrDYvOa5w=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCvaTdHTWBGv3MKj3KVqJVCw": [
        "猫又おかゆ",
        "https://yt3.ggpht.com/a/AATXAJxiB3oU3X4_wTHHAay43njgJgzw-2qKPeYIjDH2=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UChAnqc_AY5_I3Px5dig3X1Q": [
        "戌神ころね",
        "https://yt3.ggpht.com/a/AATXAJyvWtmcbmGiE0e1m316wI0MJN6-hGWxjhGZeCWhFA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCvInZx9h3jC2JzsIzoOebWg": [
        "不知火フレア",
        "https://yt3.ggpht.com/a/AATXAJwGmRMcFMvE1JW3v152HnrXfMQxbI_Dw92KH0-CpA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCdyqAaZDKHXg4Ahi7VENThQ": [
        "白銀ノエル",
        "https://yt3.ggpht.com/a/AATXAJyflKVfVjZg11sLPRv8BrLT-8ltdeRcTyKTWlXV=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCCzUftO8KOVkV4wQG1vkUvg": [
        "宝鐘マリン",
        "https://yt3.ggpht.com/a/AATXAJwAAoZPNqrR0udm1KMznPYUUTbW-sERt_LZU-af=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC1DCedRgGHBdm81E1llLhOQ": [
        "兎田ぺこら",
        "https://yt3.ggpht.com/a/AATXAJwFs1D2-rT1XPz-fvlO5ZdnkKhPU-Uu6GDwNDn_FA=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCl_gCybOJRIgOXw6Qb4qJzQ": [
        "潤羽るしあ",
        "https://yt3.ggpht.com/a/AATXAJwi-Xs0ChOThMuUzFsl3cNZYgdP12Witb0cNSf9=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC5CwaMl1eIgY8h02uZw7u8A": [
        "星街すいせい",
        "https://yt3.ggpht.com/a/AATXAJzbRjSTNu3QQ7pia2yR5oVTcds7MpmeA3a1xE-h=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCZlDXzGoo7d44bwdNObFacg": [
        "天音かなた",
        "https://yt3.ggpht.com/a/AATXAJwu4OylyCnOP8gGbO8hINCbwCfPzhBY5JrS0htm=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCS9uQI-jC3DE0L4IpXyvr6w": [
        "桐生ココ",
        "https://yt3.ggpht.com/a/AATXAJz_YJU2_OXLiMyWNFnGaC-LpYTs_06G22ozGVfw=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCqm3BQLlJfvkTsX_hvm0UmA": [
        "角巻わため",
        "https://yt3.ggpht.com/a/AATXAJzqZYR2ukuLZqCDgdsg9eid13borfDPzVBwTIDc=s100-c-k-c0xffffffff-no-rj-mo"
    ],
    "UC1uv2Oq6kNxgATlCiez59hw": [
        "常闇トワ",
        "https://yt3.ggpht.com/a/AATXAJxqyp7DhLSSrSYRc5HaLcq5QvJvRp3jDnxTeA=s288-c-k-c0xffffffff-no-rj-mo"
    ],
    "UCa9Y57gfeY0Zro_noHRVrnw": [
        "姫森ルーナ",
        "https://yt3.ggpht.com/a/AATXAJzzirDjRJkofWVeoE6gVjodJ0VXaJhy4b_CLg=s288-c-k-c0xffffffff-no-rj-mo"
    ],

} #配信者のチャンネルID, 配信者名, アイコン画像のURLのリスト

webhook_url_Hololive = '配信開始チャンネル用のwebhookリンク' #ホロライブ配信開始
webhook_url_Hololive_yotei = '配信開始予定用のwebhookリンク' #ホロライブ配信予定
broadcast_data = {} #配信予定のデータを格納

YOUTUBE_API_KEY = [複数のAPI(str型)をリストで管理]

def dataformat_for_python(at_time): #datetime型への変換
    at_year = int(at_time[0:4])
    at_month = int(at_time[5:7])
    at_day = int(at_time[8:10])
    at_hour = int(at_time[11:13])
    at_minute = int(at_time[14:16])
    at_second = int(at_time[17:19])
    return datetime(at_year, at_month, at_day, at_hour, at_minute, at_second)

def replace_JST(s):
    a = s.split("-")
    u = a[2].split(" ")
    t = u[1].split(":")
    time = [int(a[0]), int(a[1]), int(u[0]), int(t[0]), int(t[1]), int(t[2])]
    if(time[3] >= 15):
      time[2] += 1
      time[3] = time[3] + 9 - 24
    else:
      time[3] += 9
    return (str(time[0]) + "/" + str(time[1]).zfill(2) + "/" + str(time[2]).zfill(2) + " " + str(time[3]).zfill(2) + "-" + str(time[4]).zfill(2) + "-" + str(time[5]).zfill(2))

def post_to_discord(userId, videoId):
    haishin_url = "https://www.youtube.com/watch?v=" + videoId #配信URL
    content = "配信中！\n" + haishin_url #Discordに投稿される文章
    main_content = {
        "username": Hololive[userId][0], #配信者名
        "avatar_url": Hololive[userId][1], #アイコン
        "content": content #文章
    }
    requests.post(webhook_url_Hololive, main_content) #Discordに送信
    broadcast_data.pop(videoId)

def get_information():
    tmp = copy.copy(broadcast_data)
    api_now = 0 #現在どのYouTube APIを使っているかを記録
    for idol in Hololive:
        api_link = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + idol + "&key=" + YOUTUBE_API_KEY[api_now] + "&eventType=upcoming&type=video"
        api_now = (api_now + 1) % len(YOUTUBE_API_KEY) #apiを1つずらす
        aaa = requests.get(api_link)
        v_data = json.loads(aaa.text)
        try:
            for item in v_data['items']:#各配信予定動画データに関して
                broadcast_data[item['id']['videoId']] = {'channelId':item['snippet']['channelId']} #channelIDを格納
            for video in broadcast_data:
                try:
                    a = broadcast_data[video]['starttime'] #既にbroadcast_dataにstarttimeがあるかチェック
                except KeyError:#なかったら
                    aaaa = requests.get("https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + video + "&key=" + YOUTUBE_API_KEY[api_now])
                    api_now = (api_now + 1) % len(YOUTUBE_API_KEY) #apiを1つずらす
                    vd = json.loads(aaaa.text)
                    print(vd)
                    broadcast_data[video]['starttime'] = vd['items'][0]['liveStreamingDetails']['scheduledStartTime']
        except KeyError: #配信予定がなくて403が出た
            continue
    for vi in broadcast_data:
        if(not(vi in tmp)):
            print(broadcast_data[vi])
            try:
                post_broadcast_schedule(broadcast_data[vi]['channelId'], vi, broadcast_data[vi]['starttime'])
            except KeyError:
                continue

def check_schedule(now_time, broadcast_data):
    for bd in list(broadcast_data):
        try:
            # RFC 3339形式 => datetime
            sd_time = datetime.strptime(broadcast_data[bd]['starttime'], '%Y-%m-%dT%H:%M:%SZ') #配信スタート時間をdatetime型で保管
            sd_time += timedelta(hours=9)
            if(now_time >= sd_time):#今の方が配信開始時刻よりも後だったら
                post_to_discord(broadcast_data[bd]['channelId'], bd) #ツイート
        except KeyError:
            continue

def post_broadcast_schedule(userId, videoId, starttime):
    st = starttime.replace('T', ' ')
    sst = st.replace('Z', '')
    ssst = replace_JST(sst)
    haishin_url = "https://www.youtube.com/watch?v=" + videoId #配信URL
    content = ssst + "に配信予定！\n" + haishin_url #Discordに投稿される文章
    main_content = {
        "username": Hololive[userId][0], #配信者名
        "avatar_url": Hololive[userId][1], #アイコン
        "content": content #文章
    }
    requests.post(webhook_url_Hololive_yotei, main_content) #Discordに送信

while True:
    now_time = datetime.now() + timedelta(hours=9)
    if(((now_time.year > 2020) or ((now_time.year == 2020) and (now_time.month >= 6) and (now_time.day >= 22))) and (now_time.minute == 0) and (now_time.hour % 2 == 0)):
        get_information()
    check_schedule(now_time, broadcast_data)
    time.sleep(60)

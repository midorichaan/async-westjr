import asyncio
import async_westjr

jr = async_westjr.WestJR(line="kobesanyo", area="kinki")
loop = asyncio.get_event_loop()


async def get_trains():
    data = await jr.get_trains()
    print(data)

loop.run_until_complete(get_trains())
# TrainPos(update='2023-03-21T16:54:54.612Z', trains=[TrainsItem(no='502C', ...


async def get_stations():
    data = await jr.get_stations()
    print(data)

loop.run_until_complete(get_stations())
# Stations(stations=[StationsItem(info=Info(name='新大阪', code='0415', stopTrains=[1, 2, 5], typeNotice=None, ...


async def get_lines():
    data = await jr.get_lines()
    print(data)

loop.run_until_complete(get_lines())
# AreaMaster(lines={'ako': Line(name='赤穂線', range='相生〜播州赤穂', relatelines=None, st='...


async def get_maintenance():
    data = await jr.get_maintenance()
    print(data)

loop.run_until_complete(get_maintenance())
# 平常時:
# AreaMaintenance(status=0, notification=Notification(groupId=0, text='', duration=''), ...
# 異常時:
# AreaMaintenance(status=1, notification=Notification(groupId=2023012802, text='1月24日から1月31日を, ...


async def get_traffic_info():
    data = await jr.get_traffic_info()
    print(data)

loop.run_until_complete(get_traffic_info())
# 平常時:
# TrainInfo(lines={}, express={})
# 異常時:
# TrainInfo(lines={'bantan': Info_LineItem(...)}, express={'bantan': Info_ExpressItem(...)})


# エリア名一覧
print(jr.areas)
# ['hokuriku', 'kinki', 'okayama', 'hiroshima', 'sanin']

# 路線名一覧
print(jr.lines)
# ['hokuriku', 'kobesanyo', 'hokurikubiwako', 'kyoto', 'ako', 'kosei', 'kusatsu', 'nara', 'sagano', 'sanin1',
# 'sanin2', 'osakahigashi', 'takarazuka']


# 駅に停車する種別を id から名称に変換する．
# stopTrains_to_realname()
async def convertTrains():
    station = (await jr.get_stations(line="kyoto")).stations[0]
    print(station.info.name)
    print(jr.convert_stopTrains(station.info.stopTrains))
# 山科
# ['新快速', '快速', '特急']


# 列車走行位置の場所を前駅と次駅の名前に変換する
# jr.pos_to_realname(train=tr)
async def convertPos():
    train = (await jr.get_trains(line="kobesanyo")).trains
    tr = train[0]
    prev, next_st = jr.convert_pos(train=tr)
    print(prev)
    # 例: 塚本

# WestJR

![Python Versions](https://img.shields.io/pypi/pyversions/WestJR.svg)
![PyPI](https://badge.fury.io/py/WestJR.svg)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/midorichaan/async-westjr/master.svg)](https://results.pre-commit.ci/latest/github/midorichaan/async-westjr/master)
![GitHubActions](https://github.com/midorichaan/async-westjr/workflows/Test/badge.svg)

JR西日本列車走行位置 非公式API Async-Pythonライブラリ

* 列車走行位置取得 (`/api/v3/{LINE}.json`)
* メンテナンス予定取得 (`/api/v3/area_{AREA}_maintenance.json`)
* 路線名取得 (`/api/v3/area_{AREA}_master.json`)
* 駅一覧取得 (`/api/v3/{LINE}_st.json`)
* 運行情報取得 (`/api/v3/area_{AREA}_trafficinfo.json`)
* 列車環境取得 (`/api/v3/trainmonitorinfo.json`)
* 列車走行位置駅名，列車停車種別の変換

## Notice

* 動作を完全には確認していません．

## Installation

```bash
pip install async-westjr
```

## Usage

```python
import async_westjr
jr = async_westjr.WestJR()

# あらかじめ area や line をセットする
jr = async_westjr.WestJR(line="kobesanyo", area="kinki")
```

### Example

#### 列車走行位置取得

```python
async def get_trains():
    data = await jr.get_trains()
    print(data)

await get_trains()
# TrainPos(update='2023-03-21T16:54:54.612Z', trains=[TrainsItem(no='502C', ...
```

#### メンテナンス予定取得

```python
async def get_maintenance():
    data = await jr.get_maintenance()
    print(data)

await get_maintenance()
# 平常時:
# AreaMaintenance(status=0, notification=Notification(groupId=0, text='', duration=''), ...
# 異常時:
# AreaMaintenance(status=1, notification=Notification(groupId=2023012802, text='1月24日から1月31日を, ...
```

#### 路線一覧取得

```python
async def get_lines():
    data = await jr.get_lines()
    print(data)

await get_lines()
# AreaMaster(lines={'ako': Line(name='赤穂線', range='相生〜播州赤穂', relatelines=None, st='...
```

#### 駅一覧取得

```python
async def get_stations():
    data = await jr.get_stations()
    print(data)

await get_stations()
# Stations(stations=[StationsItem(info=Info(name='新大阪', code='0415', stopTrains=[1, 2, 5], typeNotice=None, ...
```

#### 運行情報取得

```Python
async def get_traffic_info():
    data = await jr.get_traffic_info()
    print(data)

await get_traffic_info()
# 平常時:
# TrainInfo(lines={}, express={})
# 異常時:
# TrainInfo(lines={'bantan': Info_LineItem(...)}, express={'bantan': Info_ExpressItem(...)})
```

#### エリア名一覧表示

```python
print(jr.areas)
# ['hokuriku', 'kinki', 'okayama', 'hiroshima', 'sanin']
```

#### 路線名一覧表示

```python
print(jr.lines)
# ['hokuriku', 'kobesanyo', 'hokurikubiwako', 'kyoto', 'ako', 'kosei', 'kusatsu', 'nara', 'sagano', 'sanin1', 'sanin2', 'osakahigashi', 'takarazuka']
```

#### 列車環境取得

```python
async def get_train_monitor_info():
    congestion = (await jr.get_train_monitor_info()).trains["3489M"][0].cars[0].congestion
    print(congestion)
    # 26(%)
    temp = (await jr.get_train_monitor_info()).trains["3489M"][0].cars[0].temp
    print(temp)
    # 23(°C)
```

#### 駅に停車する種別を id から名称に変換する

```python
async def get_train_monitor_info():
    station = (await jr.get_stations(line="kyoto")).stations[0]

    print(station.info.name)
    # 山科

    print(jr.convert_stopTrains(station.info.stopTrains))
    # ['新快速', '快速', '特急']
```

#### 列車走行位置の場所を前駅と次駅の名前に変換する

```python
async def get_convert_pos():
    train = (await jr.get_trains(line="kobesanyo")).trains
    tr = train[0]
    prev, next = jr.convert_pos(train=tr)
    print(prev)
    # 塚本
```

## Contribution

* PRを出してください

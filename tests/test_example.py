import async_westjr

jr = async_westjr.WestJR(line="kobesanyo", area="kinki")


async def test_get_trains() -> None:
    """列車走行位置取得
    >> TrainPos(update='2023-03-21T16:54:54.612Z', trains=[TrainsItem(no='502C', ...
    """
    res_trains = await jr.get_trains()
    assert res_trains.update
    assert res_trains.trains


async def test_get_stations() -> None:
    """駅一覧取得
    >> Stations(stations=[StationsItem(info=Info(name='新大阪', code='0415', stopTrains=[1, 2, 5], typeNotice=None, ...
    """
    res_stations = await jr.get_stations()
    assert len(res_stations.stations) > 0


async def test_get_lines() -> None:
    """路線名取得
    >> AreaMaster(lines={'ako': Line(name='赤穂線', range='相生〜播州赤穂', relatelines=None, st='...
    """
    res_lines = await jr.get_lines()
    assert len(res_lines.lines.keys()) > 0


async def test_get_traffic_info() -> None:
    """運行情報取得
    >> TrainInfo(lines={}, express={})
    """
    res_traffic_info = await jr.get_traffic_info()
    assert res_traffic_info.lines is not None
    assert res_traffic_info.express is not None


def test_get_const_areas() -> None:
    """エリア名一覧
    >> ['hokuriku', 'kinki', 'okayama', 'hiroshima', 'sanin']
    """
    areas = jr.areas
    assert type(areas) is tuple


def test_get_const_lines() -> None:
    """路線名一覧
    >> ['hokuriku', 'kobesanyo', 'hokurikubiwako', 'kyoto', 'ako','kosei', 'kusatsu', 'nara', 'sagano', 'sanin1', 'sanin2', 'osakahigashi', 'takarazuka']
    """
    lines = jr.lines
    assert type(lines) is tuple


async def test_convert_stopTrains() -> None:
    """駅に停車する種別を id (0~10) から名称に変換

    JR京都線最初の始発駅を取得
    駅名と停車する列車種を抽出
    """
    station = (await jr.get_stations(line="kyoto")).stations[0]
    assert station.info.name == "山科"

    stopTrain_types = jr.convert_stopTrains(station.info.stopTrains)
    assert stopTrain_types == ["新快速", "快速", "特急"]


async def test_convert_pos() -> None:
    """列車走行位置の場所を前駅と次駅の名前に変換"""
    train = (await jr.get_trains(line="kobesanyo")).trains[0]
    prev, next_st = jr.convert_pos(train=train)
    assert prev is None or type(prev) is str
    assert next_st is None or type(next_st) is str

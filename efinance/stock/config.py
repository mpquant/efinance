from pathlib import Path
HERE = Path(__file__).parent
# K 线表头
EASTMONEY_KLINE_FIELDS = {
    'f51': '日期',
    'f52': '开盘',
    'f53': '收盘',
    'f54': '最高',
    'f55': '最低',
    'f56': '成交量',
    'f57': '成交额',
    'f58': '振幅',
    'f59': '涨跌幅',
    'f60': '涨跌额',
    'f61': '换手率',


}

# 全部沪深A股榜单表头
EASTMONEY_QUOTE_FIELDS = {
    'f12': '股票代码',
    'f14': '股票名称',
    'f13': '市场编号',
    'f3': '涨跌幅',
    'f2': '最新价',
    'f15': '最高',
    'f16':'最低',
    'f4': '涨跌额',
    'f8': '换手率',
    'f9': '动态市盈率',
    'f5': '成交量',
    'f6': '成交额',
    'f18': '昨日收盘',
    'f20': '总市值',
    'f21': '流通市值'
}
# 历史大单数据表头
EASTMONEY_HISTORY_BILL_FIELDS = {
    'f51': '日期',
    'f52': '主力净流入',
    'f53': '小单净流入',
    'f54': '中单净流入',
    'f55': '大单净流入',
    'f56': '超大单净流入',
    'f57': '主力净流入占比',
    'f58': '小单流入净占比',
    'f59': '中单流入净占比',
    'f60': '大单流入净占比',
    'f61': '超大单流入净占比',
    'f62': '收盘价',
    'f63': '涨跌幅'

}
# 请求头
EASTMONEY_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'http://quote.eastmoney.com/center/gridlist.html',
}
# 股票基本信息表头
EASTMONEY_STOCK_BASE_INFO_FIELDS = {
    'f57': '股票代码',
    'f58': '股票名称',
    'f162': '市盈率(动)',
    'f167': '市净率',
    'f127': '所处行业',
    'f116': '总市值',
    'f117': '流通市值',
    'f198': '板块编号',
    'f173': 'ROE',
    'f187': '净利率',
    'f105': '净利润',
    'f186': '毛利率'

}

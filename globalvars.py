#    Linkbit-2kbitpy support on khbit
#    Copyright (C) 2023  Emerald-AM9
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from graia.saya import Channel

import botfunc

channel = Channel[ChannelMeta].current()
channel.meta['name'] = "Linkbit"
channel.meta['description'] = "2kbit/OWbit兼容模块"
channel.meta['author'] = "Emerald-AM9"

try:
    linkbit_not_in_auto_mode = yaml.safe_load(open('linkbit.yaml', 'r', encoding='UTF-8'))
except FileNotFoundError:
    botfunc.safe_file_write('linkbit.yaml', """# LinkBit配置文件
legacy-hanbot-api-ip: ""
legacy-hanbot-api-key: ""
current-unix-timestamp: """)
    logger.error('linkbit.yaml 未创建，程序已自动创建，请填写该文件的内容')
    sys.exit(1)

def linkbit_niam_conf(name: str):
    try:
        return linkbit_not_in_auto_mode[name]
    except KeyError:
        logger.error(f'{name} 在配置文件中找不到，将尝试空载配置文件')
        return None

# 2kbit-py
ops = await botfunc.get_all_admin()
g_ops = await botfunc.get_all_admin()
blocklist = await botfunc.get_all_sb()
g_blocklist = await botfunc.get_all_sb()
ignores = await botfunc.get_all_sb()
g_ignores = await botfunc.get_all_sb()
time_now = linkbit_niam_conf('current-unix-timestamp')
owner_qq = botfunc.get_config('su')
api = linkbit_niam_conf('legacy-hanbot-api-ip')
api_key = linkbit_niam_conf('legacy-hanbot-api-key')
bot_qq = botfunc.get_config('qq')
verify_key = botfunc.get_config('verifyKey')
database_host = botfunc.get_cloud_config('MySQL_Host')
database_user = botfunc.get_cloud_config('MySQL_User')
database_passwd = botfunc.get_cloud_config('MySQL_Pwd')
database_name = botfunc.get_cloud_config('MySQL_db')

# OtherWorldBit
botqq = botfunc.get_config('qq')

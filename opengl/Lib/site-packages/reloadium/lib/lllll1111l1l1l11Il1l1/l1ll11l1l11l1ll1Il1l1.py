from reloadium.corium.vendored import logging
from pathlib import Path
from threading import Thread
import time
from typing import TYPE_CHECKING, List, Optional

from reloadium.corium import lll1l11111l1111lIl1l1
from reloadium.corium.lll1l11111l1111lIl1l1.l1ll111ll11lllllIl1l1 import ll1l111ll111l111Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l111l1ll1ll1llllIl1l1
from reloadium.corium.ll1l11l1l111l11lIl1l1 import llll1l1lllllll11Il1l1
from reloadium.corium.ll1ll1ll1lllll1lIl1l1 import l1ll11lll11ll11lIl1l1
from reloadium.corium.ll1l1l1llll1l1llIl1l1 import l11lll111111l11lIl1l1
from reloadium.corium.l1l1111ll11111l1Il1l1 import l1l1111ll11111l1Il1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from reloadium.vendored.websocket_server import WebsocketServer


__RELOADIUM__ = True

__all__ = ['l11l111ll11l11llIl1l1']



lll11ll11lll1l11Il1l1 = '\n<!--{info}-->\n<script type="text/javascript">\n   // <![CDATA[  <-- For SVG support\n     function refreshCSS() {\n        var sheets = [].slice.call(document.getElementsByTagName("link"));\n        var head = document.getElementsByTagName("head")[0];\n        for (var i = 0; i < sheets.length; ++i) {\n           var elem = sheets[i];\n           var parent = elem.parentElement || head;\n           parent.removeChild(elem);\n           var rel = elem.rel;\n           if (elem.href && typeof rel != "string" || rel.length === 0 || rel.toLowerCase() === "stylesheet") {\n              var url = elem.href.replace(/(&|\\?)_cacheOverride=\\d+/, \'\');\n              elem.href = url + (url.indexOf(\'?\') >= 0 ? \'&\' : \'?\') + \'_cacheOverride=\' + (new Date().valueOf());\n           }\n           parent.appendChild(elem);\n        }\n     }\n     let protocol = window.location.protocol === \'http:\' ? \'ws://\' : \'wss://\';\n     let address = protocol + "{address}:{port}";\n     let socket = undefined;\n     let lost_connection = false;\n\n     function connect() {\n        socket = new WebSocket(address);\n         socket.onmessage = function (msg) {\n            if (msg.data === \'reload\') window.location.href = window.location.href;\n            else if (msg.data === \'refreshcss\') refreshCSS();\n         };\n     }\n\n     function checkConnection() {\n        if ( socket.readyState === socket.CLOSED ) {\n            lost_connection = true;\n            connect();\n        }\n     }\n\n     connect();\n     setInterval(checkConnection, 500)\n\n   // ]]>\n</script>\n'














































@dataclass
class l11l111ll11l11llIl1l1:
    ll111l1111l11111Il1l1: str
    l11ll1l11llllll1Il1l1: int
    l1ll1ll1l1l111l1Il1l1: l1ll11lll11ll11lIl1l1

    lll111111l11l1l1Il1l1: Optional["WebsocketServer"] = field(init=False, default=None)
    ll1l1ll1l1ll111lIl1l1: str = field(init=False, default='')

    l1l1lll1l1ll11l1Il1l1 = 'Reloadium page reloader'

    def lll1lll11l11llllIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        from reloadium.vendored.websocket_server import WebsocketServer

        l1l11l1lll1lllllIl1l1.l1ll1ll1l1l111l1Il1l1.l1l1lll1l1ll11l1Il1l1(''.join(['Starting reload websocket server on port ', '{:{}}'.format(l1l11l1lll1lllllIl1l1.l11ll1l11llllll1Il1l1, '')]))

        l1l11l1lll1lllllIl1l1.lll111111l11l1l1Il1l1 = WebsocketServer(host=l1l11l1lll1lllllIl1l1.ll111l1111l11111Il1l1, port=l1l11l1lll1lllllIl1l1.l11ll1l11llllll1Il1l1)
        l1l11l1lll1lllllIl1l1.lll111111l11l1l1Il1l1.run_forever(threaded=True)

        l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1 = lll11ll11lll1l11Il1l1

        l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1 = l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1.replace('{info}', str(l1l11l1lll1lllllIl1l1.l1l1lll1l1ll11l1Il1l1))
        l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1 = l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1.replace('{port}', str(l1l11l1lll1lllllIl1l1.l11ll1l11llllll1Il1l1))
        l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1 = l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1.replace('{address}', l1l11l1lll1lllllIl1l1.ll111l1111l11111Il1l1)

    def lllll1l1111111llIl1l1(l1l11l1lll1lllllIl1l1, l1ll1ll1ll1lll11Il1l1: str) -> str:
        l11l1l1llll1l111Il1l1 = l1ll1ll1ll1lll11Il1l1.find('<head>')
        if (l11l1l1llll1l111Il1l1 ==  - 1):
            l11l1l1llll1l111Il1l1 = 0
        lll1l1111llll1llIl1l1 = ((l1ll1ll1ll1lll11Il1l1[:l11l1l1llll1l111Il1l1] + l1l11l1lll1lllllIl1l1.ll1l1ll1l1ll111lIl1l1) + l1ll1ll1ll1lll11Il1l1[l11l1l1llll1l111Il1l1:])
        return lll1l1111llll1llIl1l1

    def l1l11ll1l1111ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        try:
            l1l11l1lll1lllllIl1l1.lll1lll11l11llllIl1l1()
        except Exception as l1111ll11l111lllIl1l1:
            l1l11l1lll1lllllIl1l1.l1ll1ll1l1l111l1Il1l1.lll1ll1l1l11l1l1Il1l1('Could not start page reload server', lll111111l1lll1lIl1l1=True)

    def l1l1lll1lllll111Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        if ( not l1l11l1lll1lllllIl1l1.lll111111l11l1l1Il1l1):
            return 

        l1l11l1lll1lllllIl1l1.l1ll1ll1l1l111l1Il1l1.l1l1lll1l1ll11l1Il1l1('Reloading page')
        l1l11l1lll1lllllIl1l1.lll111111l11l1l1Il1l1.send_message_to_all('reload')
        l1l1111ll11111l1Il1l1.llll11lllll111llIl1l1()

    def l1l11lllllll1111Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        if ( not l1l11l1lll1lllllIl1l1.lll111111l11l1l1Il1l1):
            return 

        l1l11l1lll1lllllIl1l1.l1ll1ll1l1l111l1Il1l1.l1l1lll1l1ll11l1Il1l1('Stopping reload server')
        l1l11l1lll1lllllIl1l1.lll111111l11l1l1Il1l1.shutdown()

    def l11l1ll111l1ll11Il1l1(l1l11l1lll1lllllIl1l1, lll111111llll1l1Il1l1: float) -> None:
        def ll1l11111ll1l111Il1l1() -> None:
            time.sleep(lll111111llll1l1Il1l1)
            l1l11l1lll1lllllIl1l1.l1l1lll1lllll111Il1l1()

        ll1l111ll111l111Il1l1(l1llll1111111ll1Il1l1=ll1l11111ll1l111Il1l1, l11l1l11111lll11Il1l1='page-reloader').start()


@dataclass
class lll1l1llll11ll1lIl1l1(l111l1ll1ll1llllIl1l1):
    lll11ll11lll1l11Il1l1: Optional[l11l111ll11l11llIl1l1] = field(init=False, default=None)

    lll1lll11l1111llIl1l1 = '127.0.0.1'
    l111l1llll11l1llIl1l1 = 4512

    def l1l11ll11111l11lIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.lllll11ll1ll1111Il1l1.ll111111llll11llIl1l1('html')

    def l1llll1l11llll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path, lll11lllll1111l1Il1l1: List[l11lll111111l11lIl1l1]) -> None:
        if ( not l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1):
            return 

        from reloadium.corium.l111l11l11111111Il1l1.ll1lll11l11111l1Il1l1 import ll1l111ll11lll1lIl1l1

        if ( not any((isinstance(l1111ll111l11lllIl1l1, ll1l111ll11lll1lIl1l1) for l1111ll111l11lllIl1l1 in lll11lllll1111l1Il1l1))):
            if (l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1):
                l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.l1l1lll1lllll111Il1l1()

    def l11ll1l1l11ll1l1Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        if ( not l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1):
            return 
        l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.l1l1lll1lllll111Il1l1()

    def ll1ll1l1lll111llIl1l1(l1l11l1lll1lllllIl1l1, l11ll1l11llllll1Il1l1: int) -> l11l111ll11l11llIl1l1:
        while True:
            ll111l11ll111111Il1l1 = (l11ll1l11llllll1Il1l1 + l1l11l1lll1lllllIl1l1.l111l1llll11l1llIl1l1)
            try:
                lll1l1111llll1llIl1l1 = l11l111ll11l11llIl1l1(ll111l1111l11111Il1l1=l1l11l1lll1lllllIl1l1.lll1lll11l1111llIl1l1, l11ll1l11llllll1Il1l1=ll111l11ll111111Il1l1, l1ll1ll1l1l111l1Il1l1=l1l11l1lll1lllllIl1l1.l11l1l11ll1l1lllIl1l1)
                lll1l1111llll1llIl1l1.l1l11ll1l1111ll1Il1l1()
                l1l11l1lll1lllllIl1l1.llll1lllll1ll1l1Il1l1()
                break
            except OSError:
                l1l11l1lll1lllllIl1l1.l11l1l11ll1l1lllIl1l1.l1l1lll1l1ll11l1Il1l1(''.join(["Couldn't create page reloader on ", '{:{}}'.format(ll111l11ll111111Il1l1, ''), ' port']))
                l1l11l1lll1lllllIl1l1.l111l1llll11l1llIl1l1 += 1

        return lll1l1111llll1llIl1l1

    def llll1lllll1ll1l1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        l1l11l1lll1lllllIl1l1.l11l1l11ll1l1lllIl1l1.l1l1lll1l1ll11l1Il1l1('Injecting page reloader')

    def l1ll111llll11ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1ll111llll11ll1Il1l1()

        if (l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1):
            l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.l1l11lllllll1111Il1l1()

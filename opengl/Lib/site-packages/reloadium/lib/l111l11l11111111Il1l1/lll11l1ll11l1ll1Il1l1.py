from pathlib import Path
import sys
import threading
from types import CodeType, FrameType, ModuleType
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, cast

from reloadium.corium import llll1l1l11l1ll11Il1l1, l1l111ll1l1l1111Il1l1, public, l1l1111ll11111l1Il1l1, lll1l11111l1111lIl1l1
from reloadium.corium.ll111ll11l1l1l1lIl1l1 import ll1l1ll1l1ll1lllIl1l1, ll11l1111l1l111lIl1l1
from reloadium.corium.l1l111ll1l1l1111Il1l1 import l1lll11111l11l1lIl1l1, l1ll11l1lllll111Il1l1, l1llll11l1ll11llIl1l1
from reloadium.corium.ll1l11l1l111l11lIl1l1 import llll1l1lllllll11Il1l1
from reloadium.corium.ll1ll1ll1lllll1lIl1l1 import ll1ll1ll1lllll1lIl1l1
from reloadium.corium.l111lll1lll11lllIl1l1 import l1111ll11111111lIl1l1
from reloadium.corium.l1l111111l11l11lIl1l1 import ll111l111l1l1lllIl1l1, lll11111l1ll1ll1Il1l1
from dataclasses import dataclass, field


__RELOADIUM__ = True

__all__ = ['l1ll111111ll1l1lIl1l1', 'l1l11llll1lll1llIl1l1', 'll1ll1l1l1ll1l11Il1l1']


l1ll1ll1l1l111l1Il1l1 = ll1ll1ll1lllll1lIl1l1.llll1lll11111111Il1l1(__name__)


class l1ll111111ll1l1lIl1l1:
    @classmethod
    def lll1l1ll111llll1Il1l1(l1l11l1lll1lllllIl1l1) -> Optional[FrameType]:
        ll11l1l111l1l11lIl1l1: FrameType = sys._getframe(2)
        lll1l1111llll1llIl1l1 = next(lll1l11111l1111lIl1l1.ll11l1l111l1l11lIl1l1.lll11lllll11l11lIl1l1(ll11l1l111l1l11lIl1l1))
        return lll1l1111llll1llIl1l1


class l1l11llll1lll1llIl1l1(l1ll111111ll1l1lIl1l1):
    @classmethod
    def l111111l11l1ll1lIl1l1(l1l1l1111lll1lllIl1l1, ll1lll111lllllllIl1l1: List[Any], l11l1l1111l111llIl1l1: Dict[str, Any], ll1l11llll1l111lIl1l1: List[ll111l111l1l1lllIl1l1]) -> Any:  # type: ignore
        with l1ll11l1lllll111Il1l1():
            assert llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l111l11l11111111Il1l1
            ll11l1l111l1l11lIl1l1 = llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l111l11l11111111Il1l1.l1l11111ll11111lIl1l1.ll1111l11ll1ll11Il1l1()
            ll11l1l111l1l11lIl1l1.l1l1l1l1ll1l1111Il1l1()

            l1l1lll1ll11l1llIl1l1 = llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l1111l11ll1llll1Il1l1.lll1lll1ll1l1ll1Il1l1(ll11l1l111l1l11lIl1l1.ll11l111l1ll11llIl1l1, ll11l1l111l1l11lIl1l1.ll11l1l1lllll1llIl1l1.lllll1lll1ll111lIl1l1())
            assert l1l1lll1ll11l1llIl1l1
            l1lll11lll11ll11Il1l1 = l1l1l1111lll1lllIl1l1.lll1l1ll111llll1Il1l1()

            for l11ll1111llll1l1Il1l1 in ll1l11llll1l111lIl1l1:
                l11ll1111llll1l1Il1l1.l1111l1l1l1l1l11Il1l1()

            for l11ll1111llll1l1Il1l1 in ll1l11llll1l111lIl1l1:
                l11ll1111llll1l1Il1l1.l1l1l1ll111l1ll1Il1l1()


        lll1l1111llll1llIl1l1 = l1l1lll1ll11l1llIl1l1(*ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1);        ll11l1l111l1l11lIl1l1.l1ll111ll11lllllIl1l1.additional_info.pydev_step_stop = l1lll11lll11ll11Il1l1  # type: ignore

        return lll1l1111llll1llIl1l1

    @classmethod
    async def l1lll11l11llll11Il1l1(l1l1l1111lll1lllIl1l1, ll1lll111lllllllIl1l1: List[Any], l11l1l1111l111llIl1l1: Dict[str, Any], ll1l11llll1l111lIl1l1: List[lll11111l1ll1ll1Il1l1]) -> Any:  # type: ignore
        with l1ll11l1lllll111Il1l1():
            assert llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l111l11l11111111Il1l1
            ll11l1l111l1l11lIl1l1 = llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l111l11l11111111Il1l1.l1l11111ll11111lIl1l1.ll1111l11ll1ll11Il1l1()
            ll11l1l111l1l11lIl1l1.l1l1l1l1ll1l1111Il1l1()

            l1l1lll1ll11l1llIl1l1 = llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l1111l11ll1llll1Il1l1.lll1lll1ll1l1ll1Il1l1(ll11l1l111l1l11lIl1l1.ll11l111l1ll11llIl1l1, ll11l1l111l1l11lIl1l1.ll11l1l1lllll1llIl1l1.lllll1lll1ll111lIl1l1())
            assert l1l1lll1ll11l1llIl1l1
            l1lll11lll11ll11Il1l1 = l1l1l1111lll1lllIl1l1.lll1l1ll111llll1Il1l1()

            for l11ll1111llll1l1Il1l1 in ll1l11llll1l111lIl1l1:
                await l11ll1111llll1l1Il1l1.l1111l1l1l1l1l11Il1l1()

            for l11ll1111llll1l1Il1l1 in ll1l11llll1l111lIl1l1:
                await l11ll1111llll1l1Il1l1.l1l1l1ll111l1ll1Il1l1()


        lll1l1111llll1llIl1l1 = await l1l1lll1ll11l1llIl1l1(*ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1);        ll11l1l111l1l11lIl1l1.l1ll111ll11lllllIl1l1.additional_info.pydev_step_stop = l1lll11lll11ll11Il1l1  # type: ignore

        return lll1l1111llll1llIl1l1


class ll1ll1l1l1ll1l11Il1l1(l1ll111111ll1l1lIl1l1):
    @classmethod
    def l111111l11l1ll1lIl1l1(l1l1l1111lll1lllIl1l1) -> Optional[ModuleType]:  # type: ignore
        with l1ll11l1lllll111Il1l1():
            assert llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l111l11l11111111Il1l1
            ll11l1l111l1l11lIl1l1 = llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.l111l11l11111111Il1l1.l1l11111ll11111lIl1l1.ll1111l11ll1ll11Il1l1()

            ll11ll1llllll111Il1l1 = Path(ll11l1l111l1l11lIl1l1.l1111ll1llll111lIl1l1.f_globals['__spec__'].origin).absolute()
            l11l1l1l111lllllIl1l1 = ll11l1l111l1l11lIl1l1.l1111ll1llll111lIl1l1.f_globals['__name__']
            ll11l1l111l1l11lIl1l1.l1l1l1l1ll1l1111Il1l1()
            ll11ll111l1lllllIl1l1 = llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.ll1l1ll1l1l11l11Il1l1.l1111l1lll1ll111Il1l1(ll11ll1llllll111Il1l1)

            if ( not ll11ll111l1lllllIl1l1):
                l1ll1ll1l1l111l1Il1l1.l1l11l1ll1lll11lIl1l1('Could not retrieve src.', l1l111l11ll1ll11Il1l1={'file': l1111ll11111111lIl1l1.l11llll11111ll1lIl1l1(ll11ll1llllll111Il1l1), 
'fullname': l1111ll11111111lIl1l1.l11l1l1l111lllllIl1l1(l11l1l1l111lllllIl1l1)})

            assert ll11ll111l1lllllIl1l1

        try:
            ll11ll111l1lllllIl1l1.l11l1llll1l111l1Il1l1()
            ll11ll111l1lllllIl1l1.l1lll1lllll11lllIl1l1(l1l1l1lllllll11lIl1l1=False)
            ll11ll111l1lllllIl1l1.llll1l1ll1l11111Il1l1(l1l1l1lllllll11lIl1l1=False)
        except l1lll11111l11l1lIl1l1 as l1111ll11l111lllIl1l1:
            ll11l1l111l1l11lIl1l1.lll1l1ll11l11l1lIl1l1(l1111ll11l111lllIl1l1)
            return None

        import importlib.util

        l11l1ll1l1l11l1lIl1l1 = ll11l1l111l1l11lIl1l1.l1111ll1llll111lIl1l1.f_locals['__spec__']
        l11ll11ll1ll1lllIl1l1 = importlib.util.module_from_spec(l11l1ll1l1l11l1lIl1l1)

        ll11ll111l1lllllIl1l1.ll1l1ll11ll11l1lIl1l1(l11ll11ll1ll1lllIl1l1)
        return l11ll11ll1ll1lllIl1l1


ll11l1111l1l111lIl1l1.l1111l1l1llll1l1Il1l1(ll1l1ll1l1ll1lllIl1l1.l11ll11llll11l11Il1l1, l1l11llll1lll1llIl1l1.l111111l11l1ll1lIl1l1)
ll11l1111l1l111lIl1l1.l1111l1l1llll1l1Il1l1(ll1l1ll1l1ll1lllIl1l1.lll111l11l11l11lIl1l1, l1l11llll1lll1llIl1l1.l1lll11l11llll11Il1l1)
ll11l1111l1l111lIl1l1.l1111l1l1llll1l1Il1l1(ll1l1ll1l1ll1lllIl1l1.ll111l111l111ll1Il1l1, ll1ll1l1l1ll1l11Il1l1.l111111l11l1ll1lIl1l1)

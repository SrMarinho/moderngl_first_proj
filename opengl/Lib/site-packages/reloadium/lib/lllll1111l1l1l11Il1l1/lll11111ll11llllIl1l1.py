from contextlib import contextmanager
from pathlib import Path
import sys
import types
from threading import Timer, Thread
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type, Set


import reloadium.lib.lllll1111l1l1l11Il1l1.l11l111l111lll11Il1l1
from reloadium.corium import l1l11ll11l11l11lIl1l1, llll1l1l11l1ll11Il1l1, lll1l11111l1111lIl1l1
from reloadium.corium.llll11ll11lll11lIl1l1 import l1l1ll11l11ll11lIl1l1
from reloadium.corium.l1l1111111l11lllIl1l1 import l11lll11ll11111lIl1l1, l11ll1lll1lll1l1Il1l1
from reloadium.corium.lll1l11111l1111lIl1l1.l1ll111ll11lllllIl1l1 import ll1l111ll111l111Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l11l11lll1111l11Il1l1 import ll11lllll1ll11l1Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l111l1ll1ll1llllIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l11l1111lllll1llIl1l1 import l1ll11ll11l1lll1Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.ll1l1l1111lll111Il1l1 import ll111l1ll1ll111lIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l111lll11l1lll11Il1l1 import ll11l11ll1lll1l1Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.ll11llllll1l111lIl1l1 import l1l1l1l1l11l1l1lIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.ll1111ll1lll1ll1Il1l1 import lllll1l11ll11l1lIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l11lll1l1lllll1lIl1l1 import l1ll11ll11ll11llIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.llll1lll1l1l11llIl1l1 import l1l111l11l11llllIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.llllllll11111111Il1l1 import ll1l1llll1l1111lIl1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l111lll1lll11l1lIl1l1 import ll1l11llll1l11llIl1l1
from reloadium.corium.ll1ll1ll1lllll1lIl1l1 import ll1ll1ll1lllll1lIl1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from reloadium.corium.l111lll1l1ll1ll1Il1l1 import l1l11l11ll1llll1Il1l1
    from reloadium.corium.ll1l1l1llll1l1llIl1l1 import l11lll111111l11lIl1l1


__RELOADIUM__ = True

l1ll1ll1l1l111l1Il1l1 = ll1ll1ll1lllll1lIl1l1.llll1lll11111111Il1l1(__name__)


@dataclass
class l1l1l11l11l11l1lIl1l1:
    l111lll1l1ll1ll1Il1l1: "l1l11l11ll1llll1Il1l1"

    lllll1111l1l1l11Il1l1: List[l111l1ll1ll1llllIl1l1] = field(init=False, default_factory=list)

    ll1l1l1llll11lllIl1l1: List[types.ModuleType] = field(init=False, default_factory=list)

    llllll11lllll111Il1l1: List[Type[l111l1ll1ll1llllIl1l1]] = field(init=False, default_factory=lambda :[ll111l1ll1ll111lIl1l1, lllll1l11ll11l1lIl1l1, ll11lllll1ll11l1Il1l1, ll1l1llll1l1111lIl1l1, l1ll11ll11ll11llIl1l1, ll11l11ll1lll1l1Il1l1, l1l111l11l11llllIl1l1, ll1l11llll1l11llIl1l1, l1ll11ll11l1lll1Il1l1, l1l1l1l1l11l1l1lIl1l1])




    l1lll1l111lll1llIl1l1: List[Type[l111l1ll1ll1llllIl1l1]] = field(init=False, default_factory=list)
    llll111111ll111lIl1l1 = 5

    def __post_init__(l1l11l1lll1lllllIl1l1) -> None:
        if (l1l1ll11l11ll11lIl1l1().llll11l1ll1lll1lIl1l1.ll11l1l11l111ll1Il1l1):
            l1l11l1lll1lllllIl1l1.llllll11lllll111Il1l1.remove(l1l111l11l11llllIl1l1)

        ll1l111ll111l111Il1l1(l1llll1111111ll1Il1l1=l1l11l1lll1lllllIl1l1.llll111l1l1l1lllIl1l1, l11l1l11111lll11Il1l1='show-forbidden-dialog').start()

    def llll111l1l1l1lllIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        lll1l11111l1111lIl1l1.ll11l11l1l1l11llIl1l1.lll1ll1l1ll1lll1Il1l1(l1l11l1lll1lllllIl1l1.llll111111ll111lIl1l1)

        l1l11l1lll1lllllIl1l1.l111lll1l1ll1ll1Il1l1.ll111l1llllll111Il1l1.l1111lll111lll11Il1l1()

        if ( not l1l11l1lll1lllllIl1l1.l1lll1l111lll1llIl1l1):
            return 

        lllll1111l1l1l11Il1l1 = [l1111ll11l111lllIl1l1.ll11l1l11lll1111Il1l1 for l1111ll11l111lllIl1l1 in l1l11l1lll1lllllIl1l1.l1lll1l111lll1llIl1l1]
        l1l11l1lll1lllllIl1l1.l111lll1l1ll1ll1Il1l1.ll111l11l1l1ll1lIl1l1.l11l1l11l11l1l1lIl1l1(l11ll1lll1lll1l1Il1l1.l11lll1l111ll1l1Il1l1, llll1l1l11l1ll11Il1l1.l1l1ll11l1llll1lIl1l1.l11l11llll1lll1lIl1l1(lllll1111l1l1l11Il1l1), 
ll1l1ll11ll1l1l1Il1l1='')

    def l1l111l111111l11Il1l1(l1l11l1lll1lllllIl1l1, l1111ll11ll1ll1lIl1l1: types.ModuleType) -> None:
        for l1lll1l11111l1l1Il1l1 in l1l11l1lll1lllllIl1l1.llllll11lllll111Il1l1.copy():
            if (l1lll1l11111l1l1Il1l1.ll11ll1l1ll11lllIl1l1(l1111ll11ll1ll1lIl1l1)):
                if (( not l1lll1l11111l1l1Il1l1.ll111ll1111l1111Il1l1 and l1l11l1lll1lllllIl1l1.l111lll1l1ll1ll1Il1l1.ll111l11l1l1ll1lIl1l1.l1l1111111l11lllIl1l1.llll111lll11111lIl1l1([l1lll1l11111l1l1Il1l1.ll11l1l11lll1111Il1l1]) is False)):
                    l1l11l1lll1lllllIl1l1.l1lll1l111lll1llIl1l1.append(l1lll1l11111l1l1Il1l1)
                    l1l11l1lll1lllllIl1l1.llllll11lllll111Il1l1.remove(l1lll1l11111l1l1Il1l1)
                    continue
                l1l11l1lll1lllllIl1l1.ll1ll111l1l111l1Il1l1(l1lll1l11111l1l1Il1l1)

        if (l1111ll11ll1ll1lIl1l1 in l1l11l1lll1lllllIl1l1.ll1l1l1llll11lllIl1l1):
            return 

        for lll11ll1lll111l1Il1l1 in l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.copy():
            lll11ll1lll111l1Il1l1.l1l111l11l1l11l1Il1l1(l1111ll11ll1ll1lIl1l1)

        l1l11l1lll1lllllIl1l1.ll1l1l1llll11lllIl1l1.append(l1111ll11ll1ll1lIl1l1)

    def ll1ll111l1l111l1Il1l1(l1l11l1lll1lllllIl1l1, l1lll1l11111l1l1Il1l1: Type[l111l1ll1ll1llllIl1l1]) -> None:
        llll111lll1111l1Il1l1 = l1lll1l11111l1l1Il1l1(l1l11l1lll1lllllIl1l1, l1l11l1lll1lllllIl1l1.l111lll1l1ll1ll1Il1l1.ll111l11l1l1ll1lIl1l1.l1l1111111l11lllIl1l1)

        l1l11l1lll1lllllIl1l1.l111lll1l1ll1ll1Il1l1.lll1111l11l11111Il1l1.ll1l1ll1l1lll11lIl1l1.l11lll111lll11l1Il1l1(l1l11ll11l11l11lIl1l1.lll1l1lll11111l1Il1l1(llll111lll1111l1Il1l1))
        llll111lll1111l1Il1l1.l1l11ll11111l11lIl1l1()
        l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.append(llll111lll1111l1Il1l1)

        if (l1lll1l11111l1l1Il1l1 in l1l11l1lll1lllllIl1l1.llllll11lllll111Il1l1):
            l1l11l1lll1lllllIl1l1.llllll11lllll111Il1l1.remove(l1lll1l11111l1l1Il1l1)

    @contextmanager
    def l1l11ll1l11ll11lIl1l1(l1l11l1lll1lllllIl1l1) -> Generator[None, None, None]:
        lllll11lll111lllIl1l1 = [lll11ll1lll111l1Il1l1.l1l11ll1l11ll11lIl1l1() for lll11ll1lll111l1Il1l1 in l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.copy()]

        for lll1l111l1llll1lIl1l1 in lllll11lll111lllIl1l1:
            lll1l111l1llll1lIl1l1.__enter__()

        yield 

        for lll1l111l1llll1lIl1l1 in lllll11lll111lllIl1l1:
            lll1l111l1llll1lIl1l1.__exit__(*sys.exc_info())

    def l111111l1ll1ll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        for lll11ll1lll111l1Il1l1 in l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.copy():
            lll11ll1lll111l1Il1l1.l111111l1ll1ll11Il1l1(l11llll11111ll1lIl1l1)

    def l11ll1l1l11ll1l1Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        for lll11ll1lll111l1Il1l1 in l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.copy():
            lll11ll1lll111l1Il1l1.l11ll1l1l11ll1l1Il1l1(l11llll11111ll1lIl1l1)

    def l1l1l1l11l11ll1lIl1l1(l1l11l1lll1lllllIl1l1, l11111l11l11lll1Il1l1: Exception) -> None:
        for lll11ll1lll111l1Il1l1 in l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.copy():
            lll11ll1lll111l1Il1l1.l1l1l1l11l11ll1lIl1l1(l11111l11l11lll1Il1l1)

    def l1llll1l11llll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path, lll11lllll1111l1Il1l1: List["l11lll111111l11lIl1l1"]) -> None:
        for lll11ll1lll111l1Il1l1 in l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.copy():
            lll11ll1lll111l1Il1l1.l1llll1l11llll11Il1l1(l11llll11111ll1lIl1l1, lll11lllll1111l1Il1l1)

    def l11lll1l11l1ll11Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        l1l11l1lll1lllllIl1l1.lllll1111l1l1l11Il1l1.clear()

from abc import ABC
from contextlib import contextmanager
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, ClassVar, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.l1l1111111l11lllIl1l1 import l11lll11ll11111lIl1l1, l1lll1111l1l111lIl1l1
from reloadium.corium.ll1ll1ll1lllll1lIl1l1 import l1ll11lll11ll11lIl1l1, ll1ll1ll1lllll1lIl1l1
from reloadium.corium.ll1l1l1llll1l1llIl1l1 import l11lll111111l11lIl1l1, lll1l11111111lllIl1l1
from reloadium.corium.l1l111111l11l11lIl1l1 import ll111l111l1l1lllIl1l1, lll11111l1ll1ll1Il1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from reloadium.lib.lllll1111l1l1l11Il1l1.lll11111ll11llllIl1l1 import l1l1l11l11l11l1lIl1l1


__RELOADIUM__ = True

l1ll1ll1l1l111l1Il1l1 = ll1ll1ll1lllll1lIl1l1.llll1lll11111111Il1l1(__name__)


@dataclass
class l111l1ll1ll1llllIl1l1:
    lll11111ll11llllIl1l1: "l1l1l11l11l11l1lIl1l1"
    l1l1111111l11lllIl1l1: l11lll11ll11111lIl1l1

    ll11l1l11lll1111Il1l1: ClassVar[str] = NotImplemented
    lll1lll111ll11l1Il1l1: bool = field(init=False, default=False)

    l11l1l11ll1l1lllIl1l1: l1ll11lll11ll11lIl1l1 = field(init=False)

    ll1ll1ll11ll11llIl1l1: bool = field(init=False, default=False)

    ll111ll1111l1111Il1l1 = False

    def __post_init__(l1l11l1lll1lllllIl1l1) -> None:
        l1l11l1lll1lllllIl1l1.l11l1l11ll1l1lllIl1l1 = ll1ll1ll1lllll1lIl1l1.llll1lll11111111Il1l1(l1l11l1lll1lllllIl1l1.ll11l1l11lll1111Il1l1)
        l1l11l1lll1lllllIl1l1.l11l1l11ll1l1lllIl1l1.l1l1lll1l1ll11l1Il1l1('Creating extension')
        l1l11l1lll1lllllIl1l1.lll11111ll11llllIl1l1.l111lll1l1ll1ll1Il1l1.l11l1l11111l11l1Il1l1.l11l1ll111ll1l11Il1l1(l1l11l1lll1lllllIl1l1.l1ll11l1111l1111Il1l1())
        l1l11l1lll1lllllIl1l1.ll1ll1ll11ll11llIl1l1 = isinstance(l1l11l1lll1lllllIl1l1.l1l1111111l11lllIl1l1, l1lll1111l1l111lIl1l1)

    def l1ll11l1111l1111Il1l1(l1l11l1lll1lllllIl1l1) -> List[Type[lll1l11111111lllIl1l1]]:
        lll1l1111llll1llIl1l1 = []
        ll1l1l1llll1l1llIl1l1 = l1l11l1lll1lllllIl1l1.l111l1l111lll111Il1l1()
        for l1ll1lll11llllllIl1l1 in ll1l1l1llll1l1llIl1l1:
            l1ll1lll11llllllIl1l1.llll111111l111l1Il1l1 = l1l11l1lll1lllllIl1l1.ll11l1l11lll1111Il1l1

        lll1l1111llll1llIl1l1.extend(ll1l1l1llll1l1llIl1l1)
        return lll1l1111llll1llIl1l1

    def ll1llll1lll1ll1lIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        l1l11l1lll1lllllIl1l1.lll1lll111ll11l1Il1l1 = True

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        pass

    @classmethod
    def ll11ll1l1ll11lllIl1l1(l1l1l1111lll1lllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> bool:
        if ( not hasattr(l11ll11ll1ll1lllIl1l1, '__name__')):
            return False

        lll1l1111llll1llIl1l1 = l11ll11ll1ll1lllIl1l1.__name__.split('.')[0].lower() == l1l1l1111lll1lllIl1l1.ll11l1l11lll1111Il1l1.lower()
        return lll1l1111llll1llIl1l1

    def l1ll111llll11ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        l1ll1ll1l1l111l1Il1l1.l1l1lll1l1ll11l1Il1l1(''.join(['Disabling extension ', '{:{}}'.format(l1l11l1lll1lllllIl1l1.ll11l1l11lll1111Il1l1, '')]))

    @contextmanager
    def l1l11ll1l11ll11lIl1l1(l1l11l1lll1lllllIl1l1) -> Generator[None, None, None]:
        yield 

    def l1l11ll11111l11lIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        pass

    def l1l1l1l11l11ll1lIl1l1(l1l11l1lll1lllllIl1l1, l11111l11l11lll1Il1l1: Exception) -> None:
        pass

    def l1lll111ll11lll1Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str, lllll11ll11ll11lIl1l1: bool) -> Optional[ll111l111l1l1lllIl1l1]:
        return None

    async def ll11l1lll1l1l111Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str) -> Optional[lll11111l1ll1ll1Il1l1]:
        return None

    def ll11lll11ll1l1l1Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str) -> Optional[ll111l111l1l1lllIl1l1]:
        return None

    async def lll1111l11ll11l1Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str) -> Optional[lll11111l1ll1ll1Il1l1]:
        return None

    def l11ll1l1l11ll1l1Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        pass

    def l111111l1ll1ll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        pass

    def l1llll1l11llll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path, lll11lllll1111l1Il1l1: List[l11lll111111l11lIl1l1]) -> None:
        pass

    def __eq__(l1l11l1lll1lllllIl1l1, ll1l11llll11111lIl1l1: Any) -> bool:
        return id(ll1l11llll11111lIl1l1) == id(l1l11l1lll1lllllIl1l1)

    def l111l1l111lll111Il1l1(l1l11l1lll1lllllIl1l1) -> List[Type[lll1l11111111lllIl1l1]]:
        return []

    def ll1111lll11ll1llIl1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType, l11l1l11111lll11Il1l1: str) -> bool:
        lll1l1111llll1llIl1l1 = (hasattr(l11ll11ll1ll1lllIl1l1, '__name__') and l11ll11ll1ll1lllIl1l1.__name__ == l11l1l11111lll11Il1l1)
        return lll1l1111llll1llIl1l1


@dataclass(repr=False)
class l1111l11ll1lll11Il1l1(ll111l111l1l1lllIl1l1):
    l1111l1ll1111ll1Il1l1: l111l1ll1ll1llllIl1l1

    def __repr__(l1l11l1lll1lllllIl1l1) -> str:
        return 'ExtensionMemento'


@dataclass(repr=False)
class ll1l11l1l11ll111Il1l1(lll11111l1ll1ll1Il1l1):
    l1111l1ll1111ll1Il1l1: l111l1ll1ll1llllIl1l1

    def __repr__(l1l11l1lll1lllllIl1l1) -> str:
        return 'AsyncExtensionMemento'

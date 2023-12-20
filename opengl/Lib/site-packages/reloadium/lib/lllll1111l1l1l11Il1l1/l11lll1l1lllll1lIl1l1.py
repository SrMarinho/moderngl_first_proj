from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, List

from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l111l1ll1ll1llllIl1l1
from reloadium.corium.ll1l1l1llll1l1llIl1l1 import l11lll111111l11lIl1l1
from reloadium.corium.lll1l11111l1111lIl1l1 import ll11l11l1l1l11llIl1l1
from dataclasses import dataclass, field


__RELOADIUM__ = True


@dataclass
class l1ll11ll11ll11llIl1l1(l111l1ll1ll1llllIl1l1):
    ll11l1l11lll1111Il1l1 = 'PyGame'

    ll111ll1111l1111Il1l1 = True

    lll1l1llll11111lIl1l1: bool = field(init=False, default=False)

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l1lll1ll111ll11lIl1l1: types.ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l1lll1ll111ll11lIl1l1, 'pygame.base')):
            l1l11l1lll1lllllIl1l1.lll1l111lllllll1Il1l1()

    def lll1l111lllllll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        import pygame.display

        l111ll1l1l11ll11Il1l1 = pygame.display.update

        def l1l1l111lllll11lIl1l1(*ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> None:
            if (l1l11l1lll1lllllIl1l1.lll1l1llll11111lIl1l1):
                ll11l11l1l1l11llIl1l1.lll1ll1l1ll1lll1Il1l1(0.1)
                return None
            else:
                return l111ll1l1l11ll11Il1l1(*ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1)

        pygame.display.update = l1l1l111lllll11lIl1l1

    def l111111l1ll1ll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        l1l11l1lll1lllllIl1l1.lll1l1llll11111lIl1l1 = True

    def l1llll1l11llll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path, lll11lllll1111l1Il1l1: List[l11lll111111l11lIl1l1]) -> None:
        l1l11l1lll1lllllIl1l1.lll1l1llll11111lIl1l1 = False

    def l1l1l1l11l11ll1lIl1l1(l1l11l1lll1lllllIl1l1, l11111l11l11lll1Il1l1: Exception) -> None:
        l1l11l1lll1lllllIl1l1.lll1l1llll11111lIl1l1 = False

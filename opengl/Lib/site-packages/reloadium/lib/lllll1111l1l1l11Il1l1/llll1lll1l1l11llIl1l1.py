import dataclasses
import types
from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l111l1ll1ll1llllIl1l1
from reloadium.fast.lllll1111l1l1l11Il1l1.llll1lll1l1l11llIl1l1 import llll11l1l111111lIl1l1

from dataclasses import dataclass

__RELOADIUM__ = True

import types


@dataclass(repr=False, frozen=False)
class l1l111l11l11llllIl1l1(l111l1ll1ll1llllIl1l1):
    ll11l1l11lll1111Il1l1 = 'Pytest'

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'pytest')):
            l1l11l1lll1lllllIl1l1.l11lll1llll1l1llIl1l1(l11ll11ll1ll1lllIl1l1)

    def l11lll1llll1l1llIl1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        import _pytest.assertion.rewrite
        _pytest.assertion.rewrite.AssertionRewritingHook = llll11l1l111111lIl1l1  # type: ignore


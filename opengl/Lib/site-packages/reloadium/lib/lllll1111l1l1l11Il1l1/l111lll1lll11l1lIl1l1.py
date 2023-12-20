import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type, Union, cast

from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l111l1ll1ll1llllIl1l1
from reloadium.lib import l1llll1l111llll1Il1l1

from dataclasses import dataclass

if (TYPE_CHECKING):
    ...


__RELOADIUM__ = True


@dataclass
class ll1l11llll1l11llIl1l1(l111l1ll1ll1llllIl1l1):
    ll11l1l11lll1111Il1l1 = 'Multiprocessing'

    ll111ll1111l1111Il1l1 = True

    def __post_init__(l1l11l1lll1lllllIl1l1) -> None:
        super().__post_init__()

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'multiprocessing.popen_spawn_posix')):
            l1l11l1lll1lllllIl1l1.lll1llllll11l11lIl1l1(l11ll11ll1ll1lllIl1l1)

        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'multiprocessing.popen_spawn_win32')):
            l1l11l1lll1lllllIl1l1.lll1l111l1l111l1Il1l1(l11ll11ll1ll1lllIl1l1)

    def lll1llllll11l11lIl1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_posix
        multiprocessing.popen_spawn_posix.Popen._launch = l1llll1l111llll1Il1l1.l111lll1lll11l1lIl1l1.ll1l111111ll11l1Il1l1  # type: ignore

    def lll1l111l1l111l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        import multiprocessing.popen_spawn_win32
        multiprocessing.popen_spawn_win32.Popen.__init__ = l1llll1l111llll1Il1l1.l111lll1lll11l1lIl1l1.__init__  # type: ignore

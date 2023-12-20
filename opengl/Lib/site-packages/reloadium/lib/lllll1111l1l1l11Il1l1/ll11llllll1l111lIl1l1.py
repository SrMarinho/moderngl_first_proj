from dataclasses import dataclass, field
from types import CodeType, ModuleType
from typing import TYPE_CHECKING, Any, Callable, Optional
import inspect

from reloadium.lib.lllll1111l1l1l11Il1l1.l1ll11l1l11l1ll1Il1l1 import lll1l1llll11ll1lIl1l1

if (TYPE_CHECKING):
    pass


__RELOADIUM__ = True


@dataclass
class l1l1l1l1l11l1l1lIl1l1(lll1l1llll11ll1lIl1l1):
    ll11l1l11lll1111Il1l1 = 'Numba'

    ll111ll1111l1111Il1l1 = True

    def __post_init__(l1l11l1lll1lllllIl1l1) -> None:
        super().__post_init__()

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'numba.core.bytecode')):
            l1l11l1lll1lllllIl1l1.l111ll1lllllllllIl1l1()

    def l111ll1lllllllllIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        import numba.core.bytecode

        def l11l1lll111l1l11Il1l1(lll11lll111ll1l1Il1l1) -> CodeType:  # type: ignore
            import ast
            lll1l1111llll1llIl1l1 = getattr(lll11lll111ll1l1Il1l1, '__code__', getattr(lll11lll111ll1l1Il1l1, 'func_code', None))  # type: ignore

            if ('__rw_mode__' in lll1l1111llll1llIl1l1.co_consts):  # type: ignore
                l11lllllll1111l1Il1l1 = ast.parse(inspect.getsource(lll11lll111ll1l1Il1l1))
                l1111111ll1l1ll1Il1l1 = l11lllllll1111l1Il1l1.body[0]
                l1111111ll1l1ll1Il1l1.decorator_list = []  # type: ignore

                ll11l111l1ll11llIl1l1 = compile(l11lllllll1111l1Il1l1, filename=lll1l1111llll1llIl1l1.co_filename, mode='exec')  # type: ignore
                lll1l1111llll1llIl1l1 = ll11l111l1ll11llIl1l1.co_consts[0]

            return lll1l1111llll1llIl1l1  # type: ignore

        numba.core.bytecode.get_code_object.__code__ = l11l1lll111l1l11Il1l1.__code__

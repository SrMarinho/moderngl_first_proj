import re
from contextlib import contextmanager
import os
import sys
import types
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Set, Tuple, Union

from reloadium.corium.l1l111ll1l1l1111Il1l1 import l1ll11l1lllll111Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l111l1ll1ll1llllIl1l1, l1111l11ll1lll11Il1l1
from reloadium.corium.l1l111111l11l11lIl1l1 import ll111l111l1l1lllIl1l1
from reloadium.corium.lll1l11111l1111lIl1l1 import ll11l11l1l1l11llIl1l1
from dataclasses import dataclass, field

if (TYPE_CHECKING):
    from sqlalchemy.engine.base import Engine, Transaction
    from sqlalchemy.orm.session import Session


__RELOADIUM__ = True


@dataclass(repr=False)
class l111lll1l1l1ll11Il1l1(l1111l11ll1lll11Il1l1):
    l1111l1ll1111ll1Il1l1: "ll1l1llll1l1111lIl1l1"
    l11lllllll111111Il1l1: List["Transaction"] = field(init=False, default_factory=list)

    def l1llll11ll1l11llIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        from sqlalchemy.orm.session import _sessions

        super().l1llll11ll1l11llIl1l1()

        l1l11l1l1l1lll1lIl1l1 = list(_sessions.values())

        for ll111lll1l11llllIl1l1 in l1l11l1l1l1lll1lIl1l1:
            if ( not ll111lll1l11llllIl1l1.is_active):
                continue

            l11111111l11ll1lIl1l1 = ll111lll1l11llllIl1l1.begin_nested()
            l1l11l1lll1lllllIl1l1.l11lllllll111111Il1l1.append(l11111111l11ll1lIl1l1)

    def __repr__(l1l11l1lll1lllllIl1l1) -> str:
        return 'DbMemento'

    def l1111l1l1l1l1l11Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1111l1l1l1l1l11Il1l1()

        while l1l11l1lll1lllllIl1l1.l11lllllll111111Il1l1:
            l11111111l11ll1lIl1l1 = l1l11l1lll1lllllIl1l1.l11lllllll111111Il1l1.pop()
            if (l11111111l11ll1lIl1l1.is_active):
                try:
                    l11111111l11ll1lIl1l1.rollback()
                except :
                    pass

    def l1l1l1ll111l1ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1l1l1ll111l1ll1Il1l1()

        while l1l11l1lll1lllllIl1l1.l11lllllll111111Il1l1:
            l11111111l11ll1lIl1l1 = l1l11l1lll1lllllIl1l1.l11lllllll111111Il1l1.pop()
            if (l11111111l11ll1lIl1l1.is_active):
                try:
                    l11111111l11ll1lIl1l1.commit()
                except :
                    pass


@dataclass
class ll1l1llll1l1111lIl1l1(l111l1ll1ll1llllIl1l1):
    ll11l1l11lll1111Il1l1 = 'Sqlalchemy'

    ll11l111111l111lIl1l1: List["Engine"] = field(init=False, default_factory=list)
    l1l11l1l1l1lll1lIl1l1: Set["Session"] = field(init=False, default_factory=set)
    lllll1ll111ll1l1Il1l1: Tuple[int, ...] = field(init=False)

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'sqlalchemy')):
            l1l11l1lll1lllllIl1l1.llll1ll1111ll111Il1l1(l11ll11ll1ll1lllIl1l1)

        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'sqlalchemy.engine.base')):
            l1l11l1lll1lllllIl1l1.lllll1l1l11ll1llIl1l1(l11ll11ll1ll1lllIl1l1)

    def llll1ll1111ll111Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: Any) -> None:
        ll1l11ll1ll1ll11Il1l1 = Path(l11ll11ll1ll1lllIl1l1.__file__).read_text(encoding='utf-8')
        __version__ = re.findall('__version__\\s*?=\\s*?"(.*?)"', ll1l11ll1ll1ll11Il1l1)[0]

        l111ll1ll1ll111lIl1l1 = [int(ll1ll1lll1l1l1llIl1l1) for ll1ll1lll1l1l1llIl1l1 in __version__.split('.')]
        l1l11l1lll1lllllIl1l1.lllll1ll111ll1l1Il1l1 = tuple(l111ll1ll1ll111lIl1l1)

    def l1lll111ll11lll1Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str, lllll11ll11ll11lIl1l1: bool) -> Optional["ll111l111l1l1lllIl1l1"]:
        lll1l1111llll1llIl1l1 = l111lll1l1l1ll11Il1l1(l11l1l11111lll11Il1l1=l11l1l11111lll11Il1l1, l1111l1ll1111ll1Il1l1=l1l11l1lll1lllllIl1l1)
        lll1l1111llll1llIl1l1.l1llll11ll1l11llIl1l1()
        return lll1l1111llll1llIl1l1

    def lllll1l1l11ll1llIl1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: Any) -> None:
        l1ll11l1lllll1l1Il1l1 = locals().copy()

        l1ll11l1lllll1l1Il1l1.update({'original': l11ll11ll1ll1lllIl1l1.Engine.__init__, 'reloader_code': l1ll11l1lllll111Il1l1, 'engines': l1l11l1lll1lllllIl1l1.ll11l111111l111lIl1l1})





        l111ll1ll11ll111Il1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    proxy: Any = None,\n                    execution_options: Any = None,\n                    hide_parameters: Any = None,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         proxy,\n                         execution_options,\n                         hide_parameters\n                         )\n                with reloader_code():\n                    engines.append(self2)')
























        l1lll1l1llllll1lIl1l1 = dedent('\n            def patched(\n                    self2: Any,\n                    pool: Any,\n                    dialect: Any,\n                    url: Any,\n                    logging_name: Any = None,\n                    echo: Any = None,\n                    query_cache_size: Any = 500,\n                    execution_options: Any = None,\n                    hide_parameters: Any = False,\n            ) -> Any:\n                original(self2,\n                         pool,\n                         dialect,\n                         url,\n                         logging_name,\n                         echo,\n                         query_cache_size,\n                         execution_options,\n                         hide_parameters)\n                with reloader_code():\n                    engines.append(self2)\n        ')
























        if (l1l11l1lll1lllllIl1l1.lllll1ll111ll1l1Il1l1 <= (1, 3, 24, )):
            exec(l111ll1ll11ll111Il1l1, {**globals(), **l1ll11l1lllll1l1Il1l1}, l1ll11l1lllll1l1Il1l1)
        else:
            exec(l1lll1l1llllll1lIl1l1, {**globals(), **l1ll11l1lllll1l1Il1l1}, l1ll11l1lllll1l1Il1l1)

        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(l11ll11ll1ll1lllIl1l1.Engine, '__init__', l1ll11l1lllll1l1Il1l1['patched'])

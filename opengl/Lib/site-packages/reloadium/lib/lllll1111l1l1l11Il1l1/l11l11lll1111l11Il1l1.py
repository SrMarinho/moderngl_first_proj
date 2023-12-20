import asyncio
from contextlib import contextmanager
import os
from pathlib import Path
import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Dict, Generator, List, Optional, Tuple, Type

from reloadium.corium.ll1l11l1l111l11lIl1l1 import llll1l1lllllll11Il1l1
from reloadium.corium.l1l1111111l11lllIl1l1 import l1lll1111l1l111lIl1l1
from reloadium.lib.environ import env
from reloadium.corium.l1l111ll1l1l1111Il1l1 import l1ll11l1lllll111Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l1111l1ll1111ll1Il1l1 import l1111l11ll1lll11Il1l1, ll1l11l1l11ll111Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l1ll11l1l11l1ll1Il1l1 import lll1l1llll11ll1lIl1l1
from reloadium.corium.ll1l1l1llll1l1llIl1l1 import l11lll111111l11lIl1l1, ll1l11l1ll1ll11lIl1l1, lll1l11111111lllIl1l1, l1l11ll1lll1l1l1Il1l1, ll1l1ll111lll111Il1l1
from reloadium.corium.l1l111111l11l11lIl1l1 import ll111l111l1l1lllIl1l1, lll11111l1ll1ll1Il1l1
from reloadium.corium.ll111ll1111lll1lIl1l1 import ll1llll1llll111lIl1l1
from reloadium.corium.lll1l11111l1111lIl1l1 import ll11l11l1l1l11llIl1l1
from dataclasses import dataclass, field


if (TYPE_CHECKING):
    from django.db import transaction
    from django.db.transaction import Atomic


__RELOADIUM__ = True


@dataclass(**ll1l1ll111lll111Il1l1)
class l111111ll1111lllIl1l1(l1l11ll1lll1l1l1Il1l1):
    lll111l1l1ll11llIl1l1 = 'Field'

    @classmethod
    def l1l1lllll11l11l1Il1l1(l1l1l1111lll1lllIl1l1, ll11l1l11111111lIl1l1: ll1llll1llll111lIl1l1.l111ll1ll1l11l1lIl1l1, l1111ll1llll111lIl1l1: Any, l1l1llll1l1l1l1lIl1l1: ll1l11l1ll1ll11lIl1l1) -> bool:
        from django.db.models.fields import Field

        if ((hasattr(l1111ll1llll111lIl1l1, 'field') and isinstance(l1111ll1llll111lIl1l1.field, Field))):
            return True

        return False

    def ll1l1l111l111ll1Il1l1(l1l11l1lll1lllllIl1l1, l11l1l1ll1l111llIl1l1: lll1l11111111lllIl1l1) -> bool:
        return True

    @classmethod
    def l11llll11ll1l1llIl1l1(l1l1l1111lll1lllIl1l1) -> int:
        return 200


@dataclass(repr=False)
class l111lll1l1l1ll11Il1l1(l1111l11ll1lll11Il1l1):
    l1lll1111111ll1lIl1l1: "Atomic" = field(init=False)

    llll111l111ll1llIl1l1: bool = field(init=False, default=False)

    def l1llll11ll1l11llIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1llll11ll1l11llIl1l1()
        from django.db import transaction

        l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1 = transaction.atomic()
        l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1.__enter__()

    def l1111l1l1l1l1l11Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1111l1l1l1l1l11Il1l1()
        if (l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1):
            return 

        l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1 = True
        from django.db import transaction

        transaction.set_rollback(True)
        l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1.__exit__(None, None, None)

    def l1l1l1ll111l1ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1l1l1ll111l1ll1Il1l1()

        if (l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1):
            return 

        l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1 = True
        l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1.__exit__(None, None, None)

    def __repr__(l1l11l1lll1lllllIl1l1) -> str:
        return 'DbMemento'


@dataclass(repr=False)
class l11ll11l1ll11l1lIl1l1(ll1l11l1l11ll111Il1l1):
    l1lll1111111ll1lIl1l1: "Atomic" = field(init=False)

    llll111l111ll1llIl1l1: bool = field(init=False, default=False)

    async def l1llll11ll1l11llIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        await super().l1llll11ll1l11llIl1l1()
        from django.db import transaction
        from asgiref.sync import sync_to_async

        l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1 = transaction.atomic()


        with llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.ll1l11ll11l11lllIl1l1.lll11111l1llllllIl1l1(False):
            await sync_to_async(l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1.__enter__)()

    async def l1111l1l1l1l1l11Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().l1111l1l1l1l1l11Il1l1()
        if (l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1):
            return 

        l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1 = True
        from django.db import transaction

        def l11lll1lll1l1ll1Il1l1() -> None:
            transaction.set_rollback(True)
            l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1.__exit__(None, None, None)
        with llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.ll1l11ll11l11lllIl1l1.lll11111l1llllllIl1l1(False):
            await sync_to_async(l11lll1lll1l1ll1Il1l1)()

    async def l1l1l1ll111l1ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        from asgiref.sync import sync_to_async

        await super().l1l1l1ll111l1ll1Il1l1()

        if (l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1):
            return 

        l1l11l1lll1lllllIl1l1.llll111l111ll1llIl1l1 = True
        with llll1l1lllllll11Il1l1.l111lll1l1ll1ll1Il1l1.ll1l11ll11l11lllIl1l1.lll11111l1llllllIl1l1(False):
            await sync_to_async(l1l11l1lll1lllllIl1l1.l1lll1111111ll1lIl1l1.__exit__)(None, None, None)

    def __repr__(l1l11l1lll1lllllIl1l1) -> str:
        return 'AsyncDbMemento'


@dataclass
class ll11lllll1ll11l1Il1l1(lll1l1llll11ll1lIl1l1):
    ll11l1l11lll1111Il1l1 = 'Django'

    lll11ll1ll1ll1l1Il1l1: Optional[int] = field(init=False)
    l1llll111l11l111Il1l1: Optional[Callable[..., Any]] = field(init=False, default=None)

    lll1ll1l11l11l11Il1l1: Any = field(init=False, default=None)
    l11111l1l111111lIl1l1: Any = field(init=False, default=None)
    l11l1l1l11l1lll1Il1l1: Any = field(init=False, default=None)

    ll111ll1111l1111Il1l1 = True

    def __post_init__(l1l11l1lll1lllllIl1l1) -> None:
        super().__post_init__()
        l1l11l1lll1lllllIl1l1.lll11ll1ll1ll1l1Il1l1 = None

    def l111l1l111lll111Il1l1(l1l11l1lll1lllllIl1l1) -> List[Type[lll1l11111111lllIl1l1]]:
        return [l111111ll1111lllIl1l1]

    def l1l11ll11111l11lIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1l11ll11111l11lIl1l1()
        if ('runserver' in sys.argv):
            sys.argv.append('--noreload')

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l11ll11ll1ll1lllIl1l1: types.ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l11ll11ll1ll1lllIl1l1, 'django.core.management.commands.runserver')):
            l1l11l1lll1lllllIl1l1.l1llll1l1lll11llIl1l1()
            if ( not l1l11l1lll1lllllIl1l1.ll1ll1ll11ll11llIl1l1):
                l1l11l1lll1lllllIl1l1.l111lllll11ll11lIl1l1()

    def l1ll111llll11ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        import django.core.management.commands.runserver

        django.core.management.commands.runserver.Command.handle = l1l11l1lll1lllllIl1l1.lll1ll1l11l11l11Il1l1
        django.core.management.commands.runserver.Command.get_handler = l1l11l1lll1lllllIl1l1.l11l1l1l11l1lll1Il1l1
        django.core.handlers.base.BaseHandler.get_response = l1l11l1lll1lllllIl1l1.l11111l1l111111lIl1l1

    def l1lll111ll11lll1Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str, lllll11ll11ll11lIl1l1: bool) -> Optional["ll111l111l1l1lllIl1l1"]:
        if (l1l11l1lll1lllllIl1l1.ll1ll1ll11ll11llIl1l1):
            return None

        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        if (lllll11ll11ll11lIl1l1):
            return None
        else:
            lll1l1111llll1llIl1l1 = l111lll1l1l1ll11Il1l1(l11l1l11111lll11Il1l1=l11l1l11111lll11Il1l1, l1111l1ll1111ll1Il1l1=l1l11l1lll1lllllIl1l1)
            lll1l1111llll1llIl1l1.l1llll11ll1l11llIl1l1()

        return lll1l1111llll1llIl1l1

    async def ll11l1lll1l1l111Il1l1(l1l11l1lll1lllllIl1l1, l11l1l11111lll11Il1l1: str) -> Optional["lll11111l1ll1ll1Il1l1"]:
        if (l1l11l1lll1lllllIl1l1.ll1ll1ll11ll11llIl1l1):
            return None

        if ( not os.environ.get('DJANGO_SETTINGS_MODULE')):
            return None

        lll1l1111llll1llIl1l1 = l11ll11l1ll11l1lIl1l1(l11l1l11111lll11Il1l1=l11l1l11111lll11Il1l1, l1111l1ll1111ll1Il1l1=l1l11l1lll1lllllIl1l1)
        await lll1l1111llll1llIl1l1.l1llll11ll1l11llIl1l1()
        return lll1l1111llll1llIl1l1

    def l1llll1l1lll11llIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        import django.core.management.commands.runserver

        l1l11l1lll1lllllIl1l1.lll1ll1l11l11l11Il1l1 = django.core.management.commands.runserver.Command.handle

        def ll1llllllll1l1l1Il1l1(*ll1lll111lllllllIl1l1: Any, **l1ll11ll11l1llllIl1l1: Any) -> Any:
            with l1ll11l1lllll111Il1l1():
                l11ll1l11llllll1Il1l1 = l1ll11ll11l1llllIl1l1.get('addrport')
                if ( not l11ll1l11llllll1Il1l1):
                    l11ll1l11llllll1Il1l1 = django.core.management.commands.runserver.Command.default_port

                l11ll1l11llllll1Il1l1 = l11ll1l11llllll1Il1l1.split(':')[ - 1]
                l11ll1l11llllll1Il1l1 = int(l11ll1l11llllll1Il1l1)
                l1l11l1lll1lllllIl1l1.lll11ll1ll1ll1l1Il1l1 = l11ll1l11llllll1Il1l1

            return l1l11l1lll1lllllIl1l1.lll1ll1l11l11l11Il1l1(*ll1lll111lllllllIl1l1, **l1ll11ll11l1llllIl1l1)

        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(django.core.management.commands.runserver.Command, 'handle', ll1llllllll1l1l1Il1l1)

    def l111lllll11ll11lIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        import django.core.management.commands.runserver

        l1l11l1lll1lllllIl1l1.l11l1l1l11l1lll1Il1l1 = django.core.management.commands.runserver.Command.get_handler

        def ll1llllllll1l1l1Il1l1(*ll1lll111lllllllIl1l1: Any, **l1ll11ll11l1llllIl1l1: Any) -> Any:
            with l1ll11l1lllll111Il1l1():
                assert l1l11l1lll1lllllIl1l1.lll11ll1ll1ll1l1Il1l1
                l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1 = l1l11l1lll1lllllIl1l1.ll1ll1l1lll111llIl1l1(l1l11l1lll1lllllIl1l1.lll11ll1ll1ll1l1Il1l1)
                if (env.page_reload_on_start):
                    l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.l11l1ll111l1ll11Il1l1(2.0)

            return l1l11l1lll1lllllIl1l1.l11l1l1l11l1lll1Il1l1(*ll1lll111lllllllIl1l1, **l1ll11ll11l1llllIl1l1)

        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(django.core.management.commands.runserver.Command, 'get_handler', ll1llllllll1l1l1Il1l1)

    def llll1lllll1ll1l1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().llll1lllll1ll1l1Il1l1()

        import django.core.handlers.base

        l1l11l1lll1lllllIl1l1.l11111l1l111111lIl1l1 = django.core.handlers.base.BaseHandler.get_response

        def ll1llllllll1l1l1Il1l1(l1lll111llll1l11Il1l1: Any, l1l1l111ll1llll1Il1l1: Any) -> Any:
            l11ll11l1l1111l1Il1l1 = l1l11l1lll1lllllIl1l1.l11111l1l111111lIl1l1(l1lll111llll1l11Il1l1, l1l1l111ll1llll1Il1l1)

            if ( not l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1):
                return l11ll11l1l1111l1Il1l1

            l1l1111ll1llllllIl1l1 = l11ll11l1l1111l1Il1l1.get('content-type')

            if (( not l1l1111ll1llllllIl1l1 or 'text/html' not in l1l1111ll1llllllIl1l1)):
                return l11ll11l1l1111l1Il1l1

            ll1l11ll1ll1ll11Il1l1 = l11ll11l1l1111l1Il1l1.content

            if (isinstance(ll1l11ll1ll1ll11Il1l1, bytes)):
                ll1l11ll1ll1ll11Il1l1 = ll1l11ll1ll1ll11Il1l1.decode('utf-8')

            llll1lll1l111111Il1l1 = l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.lllll1l1111111llIl1l1(ll1l11ll1ll1ll11Il1l1)

            l11ll11l1l1111l1Il1l1.content = llll1lll1l111111Il1l1.encode('utf-8')
            l11ll11l1l1111l1Il1l1['content-length'] = str(len(l11ll11l1l1111l1Il1l1.content)).encode('ascii')
            return l11ll11l1l1111l1Il1l1

        django.core.handlers.base.BaseHandler.get_response = ll1llllllll1l1l1Il1l1  # type: ignore

    def l111111l1ll1ll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path) -> None:
        super().l111111l1ll1ll11Il1l1(l11llll11111ll1lIl1l1)

        from django.apps.registry import Apps

        l1l11l1lll1lllllIl1l1.l1llll111l11l111Il1l1 = Apps.register_model

        def lll1111ll11111llIl1l1(*ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> Any:
            pass

        Apps.register_model = lll1111ll11111llIl1l1

    def l1llll1l11llll11Il1l1(l1l11l1lll1lllllIl1l1, l11llll11111ll1lIl1l1: Path, lll11lllll1111l1Il1l1: List[l11lll111111l11lIl1l1]) -> None:
        super().l1llll1l11llll11Il1l1(l11llll11111ll1lIl1l1, lll11lllll1111l1Il1l1)

        if ( not l1l11l1lll1lllllIl1l1.l1llll111l11l111Il1l1):
            return 

        from django.apps.registry import Apps

        Apps.register_model = l1l11l1lll1lllllIl1l1.l1llll111l11l111Il1l1

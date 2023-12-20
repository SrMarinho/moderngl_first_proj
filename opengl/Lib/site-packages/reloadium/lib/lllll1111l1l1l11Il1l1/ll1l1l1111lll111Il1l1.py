from contextlib import contextmanager
from pathlib import Path
import types
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Tuple, Type

from reloadium.corium.ll1ll1ll1lllll1lIl1l1 import ll1ll1ll1lllll1lIl1l1
from reloadium.lib.environ import env
from reloadium.corium.l1l111ll1l1l1111Il1l1 import l1ll11l1lllll111Il1l1
from reloadium.lib.lllll1111l1l1l11Il1l1.l1ll11l1l11l1ll1Il1l1 import lll1l1llll11ll1lIl1l1
from reloadium.corium.ll1l1l1llll1l1llIl1l1 import ll1l11l1ll1ll11lIl1l1, lll1l11111111lllIl1l1, l1l11ll1lll1l1l1Il1l1, ll1l1ll111lll111Il1l1
from reloadium.corium.ll111ll1111lll1lIl1l1 import ll1llll1llll111lIl1l1
from reloadium.corium.lll1l11111l1111lIl1l1 import ll11l11l1l1l11llIl1l1
from dataclasses import dataclass, field


__RELOADIUM__ = True

l1ll1ll1l1l111l1Il1l1 = ll1ll1ll1lllll1lIl1l1.llll1lll11111111Il1l1(__name__)


@dataclass(**ll1l1ll111lll111Il1l1)
class llllll1l11lll111Il1l1(l1l11ll1lll1l1l1Il1l1):
    lll111l1l1ll11llIl1l1 = 'FlaskApp'

    @classmethod
    def l1l1lllll11l11l1Il1l1(l1l1l1111lll1lllIl1l1, ll11l1l11111111lIl1l1: ll1llll1llll111lIl1l1.l111ll1ll1l11l1lIl1l1, l1111ll1llll111lIl1l1: Any, l1l1llll1l1l1l1lIl1l1: ll1l11l1ll1ll11lIl1l1) -> bool:
        import flask

        if (isinstance(l1111ll1llll111lIl1l1, flask.Flask)):
            return True

        return False

    def ll11l1l1111ll11lIl1l1(l1l11l1lll1lllllIl1l1) -> bool:
        return True

    @classmethod
    def l11llll11ll1l1llIl1l1(l1l1l1111lll1lllIl1l1) -> int:
        return (super().l11llll11ll1l1llIl1l1() + 10)


@dataclass(**ll1l1ll111lll111Il1l1)
class llll111l1ll1l111Il1l1(l1l11ll1lll1l1l1Il1l1):
    lll111l1l1ll11llIl1l1 = 'Request'

    @classmethod
    def l1l1lllll11l11l1Il1l1(l1l1l1111lll1lllIl1l1, ll11l1l11111111lIl1l1: ll1llll1llll111lIl1l1.l111ll1ll1l11l1lIl1l1, l1111ll1llll111lIl1l1: Any, l1l1llll1l1l1l1lIl1l1: ll1l11l1ll1ll11lIl1l1) -> bool:
        if (repr(l1111ll1llll111lIl1l1) == '<LocalProxy unbound>'):
            return True

        return False

    def ll11l1l1111ll11lIl1l1(l1l11l1lll1lllllIl1l1) -> bool:
        return True

    @classmethod
    def l11llll11ll1l1llIl1l1(l1l1l1111lll1lllIl1l1) -> int:

        return int(10000000000.0)


@dataclass
class ll111l1ll1ll111lIl1l1(lll1l1llll11ll1lIl1l1):
    ll11l1l11lll1111Il1l1 = 'Flask'

    l11lll11l1ll1lllIl1l1: Any = field(init=False, default=None)
    ll1ll11lll1l11l1Il1l1: Any = field(init=False, default=None)
    l111lll11l1l1111Il1l1: Any = field(init=False, default=None)
    l1ll11lll11lll11Il1l1: Any = field(init=False, default=None)

    @contextmanager
    def l1l11ll1l11ll11lIl1l1(l1l11l1lll1lllllIl1l1) -> Generator[None, None, None]:




        from flask import Flask as FlaskLib 

        def ll1l11llll1ll1l1Il1l1(*ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> Any:
            def l11llllllll1ll1lIl1l1(l11l11l11l1ll11lIl1l1: Any) -> Any:
                return l11l11l11l1ll11lIl1l1

            return l11llllllll1ll1lIl1l1

        lll111111111ll11Il1l1 = FlaskLib.route
        FlaskLib.route = ll1l11llll1ll1l1Il1l1  # type: ignore

        try:
            yield 
        finally:
            FlaskLib.route = lll111111111ll11Il1l1  # type: ignore

    def l111l1l111lll111Il1l1(l1l11l1lll1lllllIl1l1) -> List[Type[lll1l11111111lllIl1l1]]:
        return [llllll1l11lll111Il1l1, llll111l1ll1l111Il1l1]

    def l1l111l11l1l11l1Il1l1(l1l11l1lll1lllllIl1l1, l1lll1ll111ll11lIl1l1: types.ModuleType) -> None:
        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l1lll1ll111ll11lIl1l1, 'flask.app')):
            l1l11l1lll1lllllIl1l1.l111lll1111ll111Il1l1()
            l1l11l1lll1lllllIl1l1.ll11l1l1l11lllllIl1l1()
            l1l11l1lll1lllllIl1l1.lll111111111l11lIl1l1()

        if (l1l11l1lll1lllllIl1l1.ll1111lll11ll1llIl1l1(l1lll1ll111ll11lIl1l1, 'flask.cli')):
            l1l11l1lll1lllllIl1l1.l11l1l1111l11ll1Il1l1()

    def l1ll111llll11ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().l1ll111llll11ll1Il1l1()
        try:
            import flask.app  # type: ignore
            import werkzeug.serving  # type: ignore
            import flask.cli  # type: ignore
            flask.app.Flask.dispatch_request = l1l11l1lll1lllllIl1l1.l1ll11lll11lll11Il1l1
            werkzeug.serving.run_simple = l1l11l1lll1lllllIl1l1.l11lll11l1ll1lllIl1l1
            flask.cli.run_simple = l1l11l1lll1lllllIl1l1.l11lll11l1ll1lllIl1l1
            flask.app.Flask.__init__ = l1l11l1lll1lllllIl1l1.ll1ll11lll1l11l1Il1l1
        except ImportError:
            pass

        if (l1l11l1lll1lllllIl1l1.l111lll11l1l1111Il1l1):
            try:
                import waitress  # type: ignore
                waitress.serve = l1l11l1lll1lllllIl1l1.l111lll11l1l1111Il1l1
            except ImportError:
                pass

    def l111lll1111ll111Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        try:
            import werkzeug.serving
            import flask.cli
        except ImportError:
            return 

        l1l11l1lll1lllllIl1l1.l11lll11l1ll1lllIl1l1 = werkzeug.serving.run_simple

        def ll1llllllll1l1l1Il1l1(*ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> Any:
            with l1ll11l1lllll111Il1l1():
                l11ll1l11llllll1Il1l1 = l11l1l1111l111llIl1l1.get('port')
                if ( not l11ll1l11llllll1Il1l1):
                    l11ll1l11llllll1Il1l1 = ll1lll111lllllllIl1l1[1]

                l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1 = l1l11l1lll1lllllIl1l1.ll1ll1l1lll111llIl1l1(l11ll1l11llllll1Il1l1)
                if (env.page_reload_on_start):
                    l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.l11l1ll111l1ll11Il1l1(1.0)
            l1l11l1lll1lllllIl1l1.l11lll11l1ll1lllIl1l1(*ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1)

        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(werkzeug.serving, 'run_simple', ll1llllllll1l1l1Il1l1)
        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(flask.cli, 'run_simple', ll1llllllll1l1l1Il1l1)

    def lll111111111l11lIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        try:
            import flask
        except ImportError:
            return 

        l1l11l1lll1lllllIl1l1.ll1ll11lll1l11l1Il1l1 = flask.app.Flask.__init__

        def ll1llllllll1l1l1Il1l1(l1ll1lllll111l11Il1l1: Any, *ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> Any:
            l1l11l1lll1lllllIl1l1.ll1ll11lll1l11l1Il1l1(l1ll1lllll111l11Il1l1, *ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1)
            with l1ll11l1lllll111Il1l1():
                l1ll1lllll111l11Il1l1.config['TEMPLATES_AUTO_RELOAD'] = True

        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(flask.app.Flask, '__init__', ll1llllllll1l1l1Il1l1)

    def ll11l1l1l11lllllIl1l1(l1l11l1lll1lllllIl1l1) -> None:
        try:
            import waitress  # type: ignore
        except ImportError:
            return 

        l1l11l1lll1lllllIl1l1.l111lll11l1l1111Il1l1 = waitress.serve


        def ll1llllllll1l1l1Il1l1(*ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> Any:
            with l1ll11l1lllll111Il1l1():
                l11ll1l11llllll1Il1l1 = l11l1l1111l111llIl1l1.get('port')
                if ( not l11ll1l11llllll1Il1l1):
                    l11ll1l11llllll1Il1l1 = int(ll1lll111lllllllIl1l1[1])

                l11ll1l11llllll1Il1l1 = int(l11ll1l11llllll1Il1l1)

                l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1 = l1l11l1lll1lllllIl1l1.ll1ll1l1lll111llIl1l1(l11ll1l11llllll1Il1l1)
                if (env.page_reload_on_start):
                    l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.l11l1ll111l1ll11Il1l1(1.0)

            l1l11l1lll1lllllIl1l1.l111lll11l1l1111Il1l1(*ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1)

        ll11l11l1l1l11llIl1l1.lll1ll1lll111l11Il1l1(waitress, 'serve', ll1llllllll1l1l1Il1l1)

    def l11l1l1111l11ll1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        try:
            from flask import cli
        except ImportError:
            return 

        ll1111ll1111ll1lIl1l1 = Path(cli.__file__).read_text(encoding='utf-8')
        ll1111ll1111ll1lIl1l1 = ll1111ll1111ll1lIl1l1.replace('.tb_next', '.tb_next.tb_next')

        exec(ll1111ll1111ll1lIl1l1, cli.__dict__)

    def llll1lllll1ll1l1Il1l1(l1l11l1lll1lllllIl1l1) -> None:
        super().llll1lllll1ll1l1Il1l1()
        import flask.app

        l1l11l1lll1lllllIl1l1.l1ll11lll11lll11Il1l1 = flask.app.Flask.dispatch_request

        def ll1llllllll1l1l1Il1l1(*ll1lll111lllllllIl1l1: Any, **l11l1l1111l111llIl1l1: Any) -> Any:
            l11ll11l1l1111l1Il1l1 = l1l11l1lll1lllllIl1l1.l1ll11lll11lll11Il1l1(*ll1lll111lllllllIl1l1, **l11l1l1111l111llIl1l1)

            if ( not l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1):
                return l11ll11l1l1111l1Il1l1

            if (isinstance(l11ll11l1l1111l1Il1l1, str)):
                lll1l1111llll1llIl1l1 = l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.lllll1l1111111llIl1l1(l11ll11l1l1111l1Il1l1)
                return lll1l1111llll1llIl1l1
            elif ((isinstance(l11ll11l1l1111l1Il1l1, flask.app.Response) and 'text/html' in l11ll11l1l1111l1Il1l1.content_type)):
                l11ll11l1l1111l1Il1l1.data = l1l11l1lll1lllllIl1l1.lll11ll11lll1l11Il1l1.lllll1l1111111llIl1l1(l11ll11l1l1111l1Il1l1.data.decode('utf-8')).encode('utf-8')
                return l11ll11l1l1111l1Il1l1
            else:
                return l11ll11l1l1111l1Il1l1

        flask.app.Flask.dispatch_request = ll1llllllll1l1l1Il1l1  # type: ignore

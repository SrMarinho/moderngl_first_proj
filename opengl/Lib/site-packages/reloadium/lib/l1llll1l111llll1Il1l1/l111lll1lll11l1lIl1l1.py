import sys

__RELOADIUM__ = True


def ll1l111111ll11l1Il1l1(l1ll1lllll111l11Il1l1, llll11111l1111llIl1l1):
    from reloadium.lib.environ import env
    from pathlib import Path
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    import io
    import os

    env.sub_process += 1
    env.save_to_os_environ()

    def l1ll1111111111llIl1l1(*l1l1l111111l1ll1Il1l1):

        for llll1l1111lllll1Il1l1 in l1l1l111111l1ll1Il1l1:
            os.close(llll1l1111lllll1Il1l1)

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
    else:
        from multiprocessing import semaphore_tracker as tracker 

    l1l11l11lll1lll1Il1l1 = tracker.getfd()
    l1ll1lllll111l11Il1l1._fds.append(l1l11l11lll1lll1Il1l1)
    ll11ll1ll11111l1Il1l1 = spawn.get_preparation_data(llll11111l1111llIl1l1._name)
    ll1llllllllll111Il1l1 = io.BytesIO()
    set_spawning_popen(l1ll1lllll111l11Il1l1)

    try:
        reduction.dump(ll11ll1ll11111l1Il1l1, ll1llllllllll111Il1l1)
        reduction.dump(llll11111l1111llIl1l1, ll1llllllllll111Il1l1)
    finally:
        set_spawning_popen(None)

    lll11ll11l11l1l1Il1l1l11ll11l111ll111Il1l1ll1ll1ll11llll11Il1l1l1lll11l1lll111lIl1l1 = None
    try:
        (lll11ll11l11l1l1Il1l1, l11ll11l111ll111Il1l1, ) = os.pipe()
        (ll1ll1ll11llll11Il1l1, l1lll11l1lll111lIl1l1, ) = os.pipe()
        lll11llllll11l1lIl1l1 = spawn.get_command_line(tracker_fd=l1l11l11lll1lll1Il1l1, pipe_handle=ll1ll1ll11llll11Il1l1)


        ll11ll1llllll111Il1l1 = str(Path(ll11ll1ll11111l1Il1l1['sys_argv'][0]).absolute())
        lll11llllll11l1lIl1l1 = [lll11llllll11l1lIl1l1[0], '-B', '-m', 'reloadium_launcher', 'spawn_process', str(l1l11l11lll1lll1Il1l1), 
str(ll1ll1ll11llll11Il1l1), ll11ll1llllll111Il1l1]
        l1ll1lllll111l11Il1l1._fds.extend([ll1ll1ll11llll11Il1l1, l11ll11l111ll111Il1l1])
        l1ll1lllll111l11Il1l1.pid = util.spawnv_passfds(spawn.get_executable(), 
lll11llllll11l1lIl1l1, l1ll1lllll111l11Il1l1._fds)
        l1ll1lllll111l11Il1l1.sentinel = lll11ll11l11l1l1Il1l1
        with open(l1lll11l1lll111lIl1l1, 'wb', closefd=False) as l11l11l11l1ll11lIl1l1:
            l11l11l11l1ll11lIl1l1.write(ll1llllllllll111Il1l1.getbuffer())
    finally:
        ll1111l11l1ll1llIl1l1 = []
        for llll1l1111lllll1Il1l1 in (lll11ll11l11l1l1Il1l1, l1lll11l1lll111lIl1l1, ):
            if (llll1l1111lllll1Il1l1 is not None):
                ll1111l11l1ll1llIl1l1.append(llll1l1111lllll1Il1l1)
        l1ll1lllll111l11Il1l1.finalizer = util.Finalize(l1ll1lllll111l11Il1l1, l1ll1111111111llIl1l1, ll1111l11l1ll1llIl1l1)

        for llll1l1111lllll1Il1l1 in (ll1ll1ll11llll11Il1l1, l11ll11l111ll111Il1l1, ):
            if (llll1l1111lllll1Il1l1 is not None):
                os.close(llll1l1111lllll1Il1l1)


def __init__(l1ll1lllll111l11Il1l1, llll11111l1111llIl1l1):
    from reloadium.lib.environ import env
    from multiprocessing import util, spawn
    from multiprocessing.context import reduction, set_spawning_popen
    from multiprocessing.popen_spawn_win32 import TERMINATE, WINEXE, WINSERVICE, WINENV, _path_eq
    from pathlib import Path
    import os
    import msvcrt
    import sys
    import _winapi

    env.sub_process += 1
    env.save_to_os_environ()

    if (sys.version_info > (3, 8, )):
        from multiprocessing import resource_tracker as tracker 
        from multiprocessing.popen_spawn_win32 import _close_handles
    else:
        from multiprocessing import semaphore_tracker as tracker 
        _close_handles = _winapi.CloseHandle

    ll11ll1ll11111l1Il1l1 = spawn.get_preparation_data(llll11111l1111llIl1l1._name)







    (l1l11ll1111l1l1lIl1l1, lll1l11ll111lll1Il1l1, ) = _winapi.CreatePipe(None, 0)
    ll1l11llll111111Il1l1 = msvcrt.open_osfhandle(lll1l11ll111lll1Il1l1, 0)
    ll1lll11l111ll11Il1l1 = spawn.get_executable()
    ll11ll1llllll111Il1l1 = str(Path(ll11ll1ll11111l1Il1l1['sys_argv'][0]).absolute())
    lll11llllll11l1lIl1l1 = ' '.join([ll1lll11l111ll11Il1l1, '-B', '-m', 'reloadium_launcher', 'spawn_process', str(os.getpid()), 
str(l1l11ll1111l1l1lIl1l1), ll11ll1llllll111Il1l1])



    if ((WINENV and _path_eq(ll1lll11l111ll11Il1l1, sys.executable))):
        ll1lll11l111ll11Il1l1 = sys._base_executable
        env = os.environ.copy()
        env['__PYVENV_LAUNCHER__'] = sys.executable
    else:
        env = None

    with open(ll1l11llll111111Il1l1, 'wb', closefd=True) as l1l1ll1l1ll1ll1lIl1l1:

        try:
            (lll11llllllll111Il1l1, lll1l111l1ll1111Il1l1, l11l1l11ll1lllllIl1l1, l11111lll1111l11Il1l1, ) = _winapi.CreateProcess(ll1lll11l111ll11Il1l1, lll11llllll11l1lIl1l1, None, None, False, 0, env, None, None)


            _winapi.CloseHandle(lll1l111l1ll1111Il1l1)
        except :
            _winapi.CloseHandle(l1l11ll1111l1l1lIl1l1)
            raise 


        l1ll1lllll111l11Il1l1.pid = l11l1l11ll1lllllIl1l1
        l1ll1lllll111l11Il1l1.returncode = None
        l1ll1lllll111l11Il1l1._handle = lll11llllllll111Il1l1
        l1ll1lllll111l11Il1l1.sentinel = int(lll11llllllll111Il1l1)
        if (sys.version_info > (3, 8, )):
            l1ll1lllll111l11Il1l1.finalizer = util.Finalize(l1ll1lllll111l11Il1l1, _close_handles, (l1ll1lllll111l11Il1l1.sentinel, int(l1l11ll1111l1l1lIl1l1), 
))
        else:
            l1ll1lllll111l11Il1l1.finalizer = util.Finalize(l1ll1lllll111l11Il1l1, _close_handles, (l1ll1lllll111l11Il1l1.sentinel, ))



        set_spawning_popen(l1ll1lllll111l11Il1l1)
        try:
            reduction.dump(ll11ll1ll11111l1Il1l1, l1l1ll1l1ll1ll1lIl1l1)
            reduction.dump(llll11111l1111llIl1l1, l1l1ll1l1ll1ll1lIl1l1)
        finally:
            set_spawning_popen(None)

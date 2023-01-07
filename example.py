from pyloggerhelper import log


def testrun() -> None:
    log.info("test", x="我是谁")


if __name__ == "__main__":
    log.initialize_for_app("testapp", binds={"ip": "0.0.0.0"}, json_render_kws={"ensure_ascii": False})
    testrun()

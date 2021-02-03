from pyloggerhelper import log


def testrun():
    log.info("test")


if __name__ == "__main__":
    log.initialize_for_app("testapp", binds={"ip": "0.0.0.0"})
    testrun()

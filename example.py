from git_router import Router

ipv4 = '192.168.10.1'
username = 'test'
password = 'test'
os = 'JUNOS'


router = Router(ipv4, username, password, os)

router.login()

router_config = router.get_config()
hostname = router.get_hostname()

router.gitpush_config( router_config )
router.logout()


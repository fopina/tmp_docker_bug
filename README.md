# tmp_docker_bug
Example for https://code.djangoproject.com/ticket/31632

## Setup

* Run mysql docker with autocommit disabled

```
docker run --net host \
           --name testmysql \
           -e MYSQL_ALLOW_EMPTY_PASSWORD=1 \
           mysql:5.7.28 sh -c 'echo autocommit = 0 >> /etc/mysql/conf.d/docker.cnf; /usr/local/bin/docker-entrypoint.sh mysqld'
```

* Install requirements `pip install -r requirements.txt` (`mysqlclient` requires system packages with MySQL client libs)

## Test it

```
➜  ./test_autocommit.py 
Traceback (most recent call last):
  File "./test_autocommit.py", line 36, in <module>
    test()
  File "./test_autocommit.py", line 32, in test
    assert o.text == 2
AssertionError
```

[This assert](https://github.com/fopina/tmp_docker_bug/blob/master/test_autocommit.py#L29-L32) fails as value was not persisted after conneciton was closed.

Adding `set autocommit = 1` to `init_command` in `settings.py` (as highlighted [there](https://github.com/fopina/tmp_docker_bug/blob/master/mysite/mysite/settings.py#L83-L84)), will make the test pass

Downgrade to `Django<2.2` will also pass the test.

# Pipeline Error Report

## Action
running pipeline

## Error
```text

```

## Traceback
```text
Traceback (most recent call last):
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    yield
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_transports/default.py", line 394, in handle_async_request
    resp = await self._pool.handle_async_request(req)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_async/connection_pool.py", line 256, in handle_async_request
    raise exc from None
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_async/connection_pool.py", line 236, in handle_async_request
    response = await connection.handle_async_request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        pool_request.request
        ^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_async/connection.py", line 101, in handle_async_request
    raise exc
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_async/connection.py", line 78, in handle_async_request
    stream = await self._connect(request)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_async/connection.py", line 156, in _connect
    stream = await stream.start_tls(**kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_backends/anyio.py", line 67, in start_tls
    with map_exceptions(exc_map):
         ~~~~~~~~~~~~~~^^^^^^^^^
  File "/usr/lib/python3.14/contextlib.py", line 162, in __exit__
    self.gen.throw(value)
    ~~~~~~~~~~~~~~^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ConnectTimeout

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/trapplus/Projects/ITtop-journal-api-doc/main.py", line 81, in main
    asyncio.run(run_pipeline())
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/asyncio/runners.py", line 204, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/asyncio/runners.py", line 127, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/usr/lib/python3.14/asyncio/base_events.py", line 719, in run_until_complete
    return future.result()
           ~~~~~~~~~~~~~^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/main.py", line 51, in run_pipeline
    raw = await client.collect_all(ENDPOINTS)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/src/collector/client.py", line 116, in collect_all
    await self.authenticate()
  File "/home/trapplus/Projects/ITtop-journal-api-doc/src/collector/client.py", line 52, in authenticate
    response = await self.client.post(LOGIN_PATH, json=payload)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_client.py", line 1859, in post
    return await self.request(
           ^^^^^^^^^^^^^^^^^^^
    ...<13 lines>...
    )
    ^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_client.py", line 1540, in request
    return await self.send(request, auth=auth, follow_redirects=follow_redirects)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_client.py", line 1629, in send
    response = await self._send_handling_auth(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
    )
    ^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_client.py", line 1657, in _send_handling_auth
    response = await self._send_handling_redirects(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_client.py", line 1694, in _send_handling_redirects
    response = await self._send_single_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_client.py", line 1730, in _send_single_request
    response = await transport.handle_async_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_transports/default.py", line 393, in handle_async_request
    with map_httpcore_exceptions():
         ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.14/contextlib.py", line 162, in __exit__
    self.gen.throw(value)
    ~~~~~~~~~~~~~~^^^^^^^
  File "/home/trapplus/Projects/ITtop-journal-api-doc/.venv/lib/python3.14/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ConnectTimeout

```

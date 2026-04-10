# Pipeline Error Report

## Action
running pipeline

## Error
```text
'JOURNAL_LOGIN'
```

## Traceback
```text
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
  File "/home/trapplus/Projects/ITtop-journal-api-doc/main.py", line 46, in run_pipeline
    login = os.environ["JOURNAL_LOGIN"]
            ~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 709, in __getitem__
KeyError: 'JOURNAL_LOGIN'

```

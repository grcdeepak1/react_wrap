# react_wrap
```
Error:
>>pc run                                                            
──────────────────────────────────────── Starting Pynecone App ─────────────────────────────────────────
Traceback (most recent call last):
  File "/Users/xxx/Developer/pynecone/py3/bin/pc", line 8, in <module>
    sys.exit(main())
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/typer/main.py", line 214, in __call__
    return get_command(self)(*args, **kwargs)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/click/core.py", line 1130, in __call__
    return self.main(*args, **kwargs)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/click/core.py", line 1055, in main
    rv = self.invoke(ctx)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/click/core.py", line 1657, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/click/core.py", line 1404, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/click/core.py", line 760, in invoke
    return __callback(*args, **kwargs)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/typer/main.py", line 532, in wrapper
    return callback(**use_params)  # type: ignore
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/pynecone/pc.py", line 91, in run
    app = utils.get_app()
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/pynecone/utils.py", line 362, in get_app
    return __import__(module, fromlist=(constants.APP_VAR,))
  File "/Users/xxx/Developer/pynecone/react_wrap/react_wrap/react_wrap.py", line 42, in <module>
    app.add_page(index)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/pynecone/app.py", line 207, in add_page
    component = component if isinstance(component, Component) else component()
  File "/Users/xxx/Developer/pynecone/react_wrap/react_wrap/react_wrap.py", line 31, in index
    color_picker(
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/pynecone/components/component.py", line 306, in create
    return cls(children=children, **props)
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/pynecone/components/component.py", line 82, in __init__
    triggers = self.get_triggers()
  File "/Users/xxx/Developer/pynecone/py3/lib/python3.10/site-packages/pynecone/components/component.py", line 210, in get_triggers
    return EVENT_TRIGGERS | cls.get_controlled_triggers()
  File "/Users/xxx/Developer/pynecone/react_wrap/react_wrap/react_wrap.py", line 21, in get_controlled_triggers
    return {"on_change": pc.EVENT_ARG}
AttributeError: module 'pynecone' has no attribute 'EVENT_ARG'
```

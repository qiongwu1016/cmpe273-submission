1<h1>Assignment1</h1>
1, Run pg_recvlogical and write WAL to WAL.file.<br/>
<pre>eg: pg_recvlogical -d college --slot test_slot --start -o pretty-print=1 -o add-msg-prefixes=wal2json -f - |tee WAL.file</pre>
2, Start the Server. server_repl.py listen to client's call and update any change to MongoDB<br/>
3, Start the client. client_repl.py keep tracking WAL.file see if there's an new update. If is, call grpc service LogicCopy to write the Postgres change to MongoDB<br/>
4, Do insert/update/delete to postgres and see the replication in MongoDB.<br/>

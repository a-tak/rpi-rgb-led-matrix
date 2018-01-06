Raspberry Pi LED時計 REST API
====

Raspberry PiとRGB Matrix LED Panelを繋げて時計を表示するプログラムを外部から操作するREST API

通信を受け付けたら特定のディレクトリに特定の文字列が入ったファイルを作製し、時計側がそのファイルを見に行くという仕組みにしてある。
外部からのアクセスは考えていないので、セキュリティについてはまったく意識していないので、注意。

## API呼出サンプル

```bash
curl http://192.168.1.xxx:3000/api/v1/clock/mode -X PUT -d "value=temp"
curl http://192.168.1.xxx:3000/api/v1/clock/mode -X PUT -d "value=clock"
curl http://192.168.1.xxx:3000/api/v1/clock/mode -X PUT -d "value=date"
```



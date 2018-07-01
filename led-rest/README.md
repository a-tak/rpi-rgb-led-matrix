Raspberry Pi LED時計 REST API
====

Raspberry PiとRGB Matrix LED Panelを繋げて時計を表示するプログラムを外部から操作するREST API

通信を受け付けたら特定のディレクトリに特定の文字列が入ったファイルを作製し、時計側がそのファイルを見に行くという仕組みにしてある。
外部からのアクセスは考えていないので、セキュリティについてはまったく意識していないので、注意。

## 必要モジュールインストール

```bash
sudo apt-get install -y nodejs npm

sudo npm cache clean
sudo npm install n -g
sudo n stable

node -v

cd /home/pi/rpi-rgb-led-matrix/led-rest/led-rest
npm install
```
apt-getで

> 以下のパッケージには満たせない依存関係があります:  
> npm : 依存: node-gyp (>= 0.10.9) しかし、インストールされようとしていません  
>E: 問題を解決することができません。壊れた変更禁止パッケージがあります。

のようなエラーが出たら以下で解決する。

```bash
sudo aptitude install npm
```

## 設定

```bash
sudo mkdir /etc/pi-settings

cd /home/pi/rpi-rgb-led-matrix/led-rest/led-rest/config
cp -p default.yaml.sample default.yaml
vim default.yaml
```

```yaml
config:
    modeFilePath: "/etc/pi-settings/"
```

Python側の設定読み込みと合わせる

## API呼出サンプル

```bash
curl http://192.168.1.xxx:3000/api/v1/clock/mode -X PUT -d "value=temp"
curl http://192.168.1.xxx:3000/api/v1/clock/mode -X PUT -d "value=clock"
curl http://192.168.1.xxx:3000/api/v1/clock/mode -X PUT -d "value=date"
```



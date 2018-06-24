時計アプリケーション
====
時計アプリケーションのPython部分

## 必要モジュール
```bash
sudo pip3 install pyyaml
```

## 実行方法
```bash
sudo ./clock.py --led-rows=16 --led-brightness=40
```

## 自動起動設定
```bash
sudo ln -sf /home/pi/rpi-rgb-led-matrix/rpi-rgb-led-matrix/bindings/python/samples/clockdisp.service /etc/systemd/system/clockdisp.service
```

## settings ディレクトリ
ここにREST API側からファイル書き込み、clock.pyが監視して時計に反映する

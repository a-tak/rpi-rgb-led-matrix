#!/usr/bin/env python3
# coding: UTF-8
# Display Ambient Sender
#
from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
import ambient
from temperature_mod import TemperatureSensor
import yaml

class AmbientSender():
    u"""温度湿度取得クラス
    """
    def __init__(self):
        pass

    def send(self):
        u"""Ambient温度湿度送信モジュール
        ドをstartすると__call__が暗黙的に呼ばれる
        """
        logger.debug("AmbientSender Module Start")
        
        #設定読み込み
        yamlfile = "./setting.yaml"
        with open(yamlfile, "rt") as fp:
            text = fp.read()
        setting = yaml.safe_load(text)
        print("Setting Loading...")
        print(setting["ambient-channel"])
        print(setting["ambient-writekey"])
         
        sensor = TemperatureSensor() 

        value = sensor.get()
        
        ambi = ambient.Ambient(setting["ambient-channel"],setting["ambient-writekey"])
        
        #hpaは小数点切り捨てる Ambientで縦軸が見きれるので
        r = ambi.send({"d1":round(value.temp,1), "d2":round(value.hum,1), "d3":round(value.hpa,1)})
        print(r) 

# Main function
if __name__ == "__main__":
    obj = AmbientSender()
    obj.send()


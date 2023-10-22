# DualShock4コントローラをRaspBerryPiにBluetoothで接続

## コントローラー接続環境をインストール

```
pip install --break-system-packages pyPS4Controller
```

※もしかしたら、ds4drvは不要かも、、、
```
pip install --break-system-packages ds4drv
export PATH="$PATH:/home/pi/.local/bin"
```

## コントローラーを認識

bluetoothctlを起動
```
bluetoothctl
```

### bluetoothctlコマンド

```
power on
```

```
検出してもらうように、SHAREボタンとPS（HOME）ボタンを同時に長押しする。
```

```
scan on
```

```
Wireless Controllerの[アドレス]（例：98:B6:E9:35:3D:DF）をコピーする。
```

```
pair [アドレス]

trust [アドレス]
```

## コントローラーを接続

```
sudo reboot
```

```
ラズパイを起動後、PS（HOME）ボタンをクリックしてBluetooth接続する。
```

## コントローラーの接続を確認

```
ls -al /dev/input
```
# bluetoothのライブラリをインストール

## 開発ライブラリをインストール
```
sudo apt install bluetooth
```

```
sudo apt install pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python3-dev
```

# Python実行環境を構築

## 仮想環境を作成
```
python -m venv bluetooth-env
source bluetooth-env/bin/activate
```

## Pythonライブラリをインストール

```
pip install --break-system-packages git+https://github.com/pybluez/pybluez
```

```
pip install --break-system-packages gattlib
```

```
pip install --break-system-packages bleak
```

# sudo権限でスクリプトを実行

## BLEデバイスのMacアドレス列挙

When using the gattlib library.
```
sudo -E env PATH=$PATH ./ble_discover_devices.py
```

When using the bleak library.
```
sudo -E env PATH=$PATH ./bleak_discover_devices.py
```

## BLEデバイスのUUID列挙
The argument is the target mac address.
```
sudo -E env PATH=$PATH ./bleak_device_uuids.py xx:xx:xx:xx:xx:xx
```
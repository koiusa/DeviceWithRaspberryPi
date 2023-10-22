# RspberryPiでpicowの開発環境を構築する

## pico-setupスクリプトを取得

```
git clone https://github.com/raspberrypi/pico-setup.git
```

## pico-setupを実行

```
cd pico-setup
./pico-setup.sh
```

---

---

# VSCodeでpicowのMicroPython開発環境を構築する

## VSCodeのPicow開発用のプラグインを追加

```
VSCodeの拡張機能からMicroPicoをインストール
```

## VSCodeのPicow開発用のプラグインの起動

コマンドパレットでMicroPicoの設定ファイルを作成
```
>MicroPico: Configure project
```

VSCode下部のMicroPicoメニューからPicoW内のスクリプトファイルをブラウズ
```
Toggle Pico-W-FS
```
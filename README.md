# mypkg 

[![test](https://github.com/teresuke/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/teresuke/mypkg/actions/workflows/test.yml)

## 本リポジトリについて
このリポジトリはtalkerとlistenerとの間で通信をするROS 2のパッケージです.

## ノード 
* パブリッシャ(talker)
  * 実行すると0.5秒ごとにトピック(countup)を通して数字を1ずつ増やしていく.
* サブスクライバ(listener)
  * トピック(countup)からメッセージを受け取り、talker.pyから受け取った内容を表示する.
## トピック(countup)
  * ROS2内でノードを通信するときに使うデータの経路のこと.
  * トピック(countup)は16ビット符号付き整数データであり、talker.pyノードからのデータを生成してlistener.pyから受けとり、ログに表示する.

## 実行方法
➀ 2つのターミナルを開く.2つのターミナルを端末1、端末2とする.

➁　端末1に
```
$ ros2 run mypkg talker
```
と実行する.
```

```
何も出ない.

➂  端末2に
```
$ ros2 run mypkg listener
```
と実行する.

④ 実行結果

```
[INFO] [1703742678.270138053] [listener]: Listen: 0
[INFO] [1703742678.745021817] [listener]: Listen: 1
[INFO] [1703742679.245405478] [listener]: Listen: 2
[INFO] [1703742679.745058842] [listener]: Listen: 3
[INFO] [1703742680.245325938] [listener]: Listen: 4
[INFO] [1703742680.745370106] [listener]: Listen: 5
[INFO] [1703742681.245143670] [listener]: Listen: 6
[INFO] [1703742681.745156353] [listener]: Listen: 7
[INFO] [1703742682.245437660] [listener]: Listen: 8
```

## 端末1つで実行するとき
```
$ ros2 launch mypkg talk_listen.launch.py
```

と実行する.

```
[INFO] [launch]: All log files can be found below /home/teresa/.ros/log/2024-01-02-14-47-54-769601-Shunsuke-210
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [212]
[INFO] [listener-2]: process started with pid [214]
[listener-2] [INFO] [1704174475.638498199] [listener]: Listen: 0
[listener-2] [INFO] [1704174476.126395106] [listener]: Listen: 1
[listener-2] [INFO] [1704174476.626191810] [listener]: Listen: 2
[listener-2] [INFO] [1704174477.126173443] [listener]: Listen: 3
```

## テスト内容
* 2023年に上田隆一先生のロボットシステム学の授業で用いられたテストに利用するコンテナを使用しています.
  * [ryuichiueda/ubuntu22.04-ros2](https://hub.docker.com/r/ryuichiueda/ubuntu22.04-ros2)


## 必要なソフトウェア
  * python
  * ROS 2 foxy
## 動作確認済み環境
  * Ubuntu 20.04.5 LTS
## ライセンス表示
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* このパッケージのコードは、下記のスライド (CC-BY- 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです.
  * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©　2023 Shunsuke Otani

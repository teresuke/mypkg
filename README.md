# mypkg 

[![test](https://github.com/teresuke/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/teresuke/mypkg/actions/workflows/test.yml)

## 課題
これはロボットシステム学の課題2である。

## ノード 
  * パブリッシャ(talker)
  * 実行すると0.5秒ごとに数字が1増えていく。
  * サブスクライバー(listener)
  * トピックからメッセージを受け取り、talker.pyから受け取った内容を標準出力する。
## トピック
  * ROS2内でノードを通信するときに使うデータの流れのこと。talkerからデータを受信してそのデータを
listenerに送信する。talkerとlistenerをつなぎ、複数のノードの間でデータを共有する。
  * talkerからlistenerにデータを送る。一ずつカウントしていく。 
    
## 実行するまでのやり方
* ➀　二つのターミナルを開く。二つの端末を端末1$、端末2$とする。
* ➁　端末1$に
```
ros2 run mypkg talker
```
と実行
```

```
何も出ない。

* ➂  端末2$に
```
ros2 run mypkg listener
```
と実行する

* ④ 実行結果

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
## インストール方法
➀  クローンする
```
git clone https://github.com/teresuke/mypkg.git
```
➁  ディレクトリに移動
```
cd ros2_ws
```
## テスト内容
* 2023年に上田隆一先生のロボットシステム学の授業で用いられたテストに利用するコンテナを使用しています。 
```
https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2
```
## 必要なソフトウェア
  * python
  * ROS2 foxy
## テスト環境
  * Ubuntu 20.04
## ライセンス表示
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* このパッケージのコードは、下記のスライド (CC-BY- 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです.
         (https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©　2023 Shunsuke Otani

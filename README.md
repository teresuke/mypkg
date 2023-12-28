# mypkg 

[![test](https://github.com/teresuke/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/teresuke/mypkg/actions/workflows/test.yml)

## 紹介
これはロボットシステム学で使われているコードである。
ROS2を使い、talkerとlistenerの二つを通信するプログラムである。
0.5秒ごとに数字を1ずつ増やしていく。

ros2のリポジトリを作る。
## ノード 
  * パブリッシャ(talker)
  * 実行すると0.5秒ごとに数字が1増えていく。
  * サブスクライバー(listener)
  * トピックからメッセージを受け取り、talker.pyから受け取った内容を標準出力する。
## トピック
  * talkerからlistenerにデータを送る。一ずつカウントしていく。 
    
## 実行するまでのやり方
* ➀　二つのターミナルを開く。二つの端末を端末1$、端末2$とする。
* ➁　端末1$に
```
ros2 run mypkg talker
```

* ➂  端末2$に
```
ros2 run mypkg listener
```
と実行する

## 実行結果

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

## launchファイル
➀ 以下のように実行する。
```
ros2 launch mypkg talk_listen.launch.py
```

➁ 実行結果が下のようになる。
```
[INFO] [launch]: All log files can be found below /home/teresa/.ros/log/2023-12-28-23-17-03-756393-Shunsuke-23630
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [23632]
[INFO] [listener-2]: process started with pid [23634]
[listener-2] [INFO] [1703773024.573352936] [listener]: Listen: 0
[listener-2] [INFO] [1703773025.066765814] [listener]: Listen: 1
[listener-2] [INFO] [1703773025.566138127] [listener]: Listen: 2
[listener-2] [INFO] [1703773026.066300581] [listener]: Listen: 3
[listener-2] [INFO] [1703773026.566372063] [listener]: Listen: 4
[listener-2] [INFO] [1703773027.066459991] [listener]: Listen: 5
[listener-2] [INFO] [1703773027.566437296] [listener]: Listen: 6
[listener-2] [INFO] [1703773028.066514275] [listener]: Listen: 7
[listener-2] [INFO] [1703773028.566751857] [listener]: Listen: 8
[listener-2] [INFO] [1703773029.066722078] [listener]: Listen: 9
[listener-2] [INFO] [1703773029.566191497] [listener]: Listen: 10
[listener-2] [INFO] [1703773030.066744086] [listener]: Listen: 11

```

## 必要なソフトウェア
  * python
  * テスト済み　3.7～3.10
  * ROS2 foxy
## テスト環境
  * Ubuntu 20.04
## ライセンス表示
このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます.
* このパッケージのコードは、下記のスライド (CC-BY- 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです.
         (https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ©　2023 Shunsuke Otani

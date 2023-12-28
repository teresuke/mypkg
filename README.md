## 課題2の説明
これはロボットシステム学で使われているコードである。
ROS2を使い、talkerとlistenerの二つを通信するプログラムである。
0.5秒ごとに数字を1ずつ増やしていく。

## ros2_ws 

コード必須

ros2のリポジトリを作る。
## ノード 
  * パブリッシャ
  実行すると0.5秒ごとに数字が1増えていく。
  * サブスクライバー
  トピックからメッセージを受け取り、talker.pyから受け取った内容を標準出力する。
## トピック

## 実行するまでのやり方
➀　端末1$に
```
ros2 run mypkg talker
```

➁　端末2$に
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


# はじめに

2018年6月20日にダイキン工業様で行われたセミナーで使用したサンプルデータです。

スライドは以下のURLで公開しています。

https://www.slideshare.net/ryotakahashisporty/python20180620


## ご使用上の注意

含まれるファイルは全てMITライセンスで公開しています。

LICENSEまたはLICENSE_jaをご覧になり、同意される場合のみご利用ください。


# Maya

## パスを通して起動

Maya2018.bat

## stuRename

```
stuRename
```


# MODO

## パスを通す

作業コピーはC:\sampleになっていることを前提にした例です。
以下のファイルを作成し、パスを通します。


%USERPROFILE%\AppData\Roaming\Luxology\Configs\stu.cfg

```
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <import>C:\sample\modo</import>
</configuration>
```

## 起動

"C:\Program Files\Foundry\Modo\12.0v1j\modo.exe"

## stuRename

```
stu.node.rename
```
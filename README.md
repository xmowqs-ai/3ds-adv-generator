# 3DS ADV Generator

3DS用ADV（アドベンチャーゲーム）を直感的に作成・管理し、DevKit Proを使ってC言語にコンパイル、3DSXファイル生成するツールです。

## 機能

- **直感的なGUI**: シナリオエディタで物語を簡単に作成
- **キャラクター管理**: キャラクター立ち絵・音声の管理
- **シーン編集**: 背景、テキスト、選択肢の配置
- **自動C言語生成**: Python→C言語へ自動トランスレート
- **DevKit Pro統合**: ワンクリックで3DSX生成
- **デバッグ機能**: エミュレータ上での動作確認

## ディレクトリ構造

```
3ds-adv-generator/
├── adv_generator/          # メインパッケージ
│   ├── __init__.py
│   ├── gui/               # GUI関連
│   │   ├── __init__.py
│   │   ├── main_window.py # メインウィンドウ
│   │   ├── scene_editor.py
│   │   ├── character_manager.py
│   │   ├── project_manager.py
│   │   └── dialogs.py
│   ├── core/              # コア処理
│   │   ├── __init__.py
│   │   ├── project.py     # プロジェクト管理
│   │   ├── parser.py      # シナリオパース
│   │   ├── codegen.py     # C言語生成
│   │   └── compiler.py    # DevKit Pro連携
│   ├── templates/         # C言語テンプレート
│   │   ├── main_template.c
│   │   ├── scene_template.c
│   │   └── character_template.c
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
├── assets/                # テンプレートアセット
│   ├── backgrounds/
│   ├── characters/
│   └── sounds/
├── projects/              # ユーザープロジェクト
├── output/                # 生成ファイル
├── requirements.txt
├── setup.py
└── main.py               # エントリーポイント
```

## インストール

```bash
git clone https://github.com/xmowqs-ai/3ds-adv-generator.git
cd 3ds-adv-generator
pip install -r requirements.txt
```

## 使用方法

```bash
python main.py
```

## 必要な環境

- Python 3.8+
- DevKit Pro（3DS開発環境）
- arm-none-eabi-gcc（クロスコンパイラ）

## ライセンス

MIT

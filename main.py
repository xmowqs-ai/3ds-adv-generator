#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3DS ADV Generator - メインエントリーポイント
"""

import sys
from adv_generator.gui.main_window import ADVGeneratorApp
from adv_generator.utils.logger import setup_logger


def main():
    """アプリケーション起動"""
    logger = setup_logger("ADV Generator")
    logger.info("3DS ADV Generator を起動しています...")
    
    try:
        app = ADVGeneratorApp()
        sys.exit(app.run())
    except Exception as e:
        logger.error(f"アプリケーション起動エラー: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()

import sys
import os

# 다른 폴더의 스크립트를 import 할 수 있도록 상위폴더 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

if __name__ == '__main__':
    print("hi!")
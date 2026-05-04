import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# 1. Streamlitアプリのタイトル
st.title("Streamlit × Matplotlib のテスト")
st.write("これはStreamlit上でMatplotlibのグラフを表示するデモです。")

# 2. データの準備
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 3. グラフの作成
# ※Streamlitで描画する場合は、Figureオブジェクトを明示的に作成するのが推奨されます
fig, ax = plt.subplots()

# axesに対してプロットや装飾を行う
ax.plot(x, y, color="red", label="sin(x)")
ax.set_title("Sine Wave")
ax.set_xlabel("X")
ax.set_ylabel("sin(X)")
ax.legend()
ax.grid(True)

# 4. Streamlitでグラフを表示
st.pyplot(fig)

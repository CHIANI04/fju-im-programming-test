# W 型樣板：沒有筆數，讀到指定關鍵字（例如 0）就停止
# v1（9/26）：初版

while True:
    line = input().strip()
    if line == "0":
        break
    S = line.split()
    # ---- 處理 ----
    ans = S[0]
    print(ans)

# ===== 變化型 =====
# 結束字是 -1：         if line == "-1": break
# 一行多值、第一個是 0 才停：
#                       S = line.split()
#                       if S[0] == "0": break
# 逗號分隔：            S = line.split(',')

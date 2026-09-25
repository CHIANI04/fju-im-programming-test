# N 型樣板：第一行給筆數 N，後面有 N 行測資
# v1（9/26）：初版

N = int(input())
for i in range(N):
    S = input().split()
    a = int(S[0])
    # ---- 處理 ----
    ans = a
    print(ans)

# ===== 變化型 =====
# 不確定整數或小數：    N = eval(input())
# 一次轉整數：          a, b = map(int, input().split())
# 整行轉成整數串列：    nums = list(map(int, input().split()))
# 逗號分隔：            S = input().split(',')
# 一筆資料有很多行：    x = int(input()); y = int(input())
# 輸出小數 2 位：       print(f"{ans:.2f}")
# 串列用空白接起來：    print(" ".join(map(str, lst)))

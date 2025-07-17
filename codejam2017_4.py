def fashion_show(N, M, existing_models):
    # 0: empty, 1: '+', 2: 'x', 3: 'o'
    board = [[0]*N for _ in range(N)]
    row_used = [False]*N
    col_used = [False]*N
    diag1_used = [False]*(2*N-1)
    diag2_used = [False]*(2*N-1)

    for model, r, c in existing_models:
        r -= 1
        c -= 1
        if model == 'o':
            board[r][c] = 3
            row_used[r] = col_used[c] = True
            diag1_used[r+c] = diag2_used[r-c+N-1] = True
        elif model == 'x':
            board[r][c] |= 2
            row_used[r] = col_used[c] = True
        elif model == '+':
            board[r][c] |= 1
            diag1_used[r+c] = diag2_used[r-c+N-1] = True

    original = [row[:] for row in board]

    # Place 'x'
    for r in range(N):
        for c in range(N):
            if not row_used[r] and not col_used[c]:
                if board[r][c] == 0:
                    board[r][c] = 2
                elif board[r][c] == 1:
                    board[r][c] = 3
                row_used[r] = col_used[c] = True

    # Place '+'
    for r in range(N):
        for c in range(N):
            d1 = r+c
            d2 = r-c+N-1
            if not diag1_used[d1] and not diag2_used[d2]:
                if board[r][c] == 0:
                    board[r][c] = 1
                elif board[r][c] == 2:
                    board[r][c] = 3
                diag1_used[d1] = diag2_used[d2] = True

    score = sum(2 if board[r][c]==3 else 1 if board[r][c] else 0 for r in range(N) for c in range(N))
    changes = []
    for r in range(N):
        for c in range(N):
            if board[r][c] != original[r][c]:
                if board[r][c] == 1:
                    changes.append(('+', r+1, c+1))
                elif board[r][c] == 2:
                    changes.append(('x', r+1, c+1))
                elif board[r][c] == 3:
                    changes.append(('o', r+1, c+1))
    return score, changes


def main():
    T = int(input())
    for case_num in range(1, T+1):
        n, m = map(int, input().split())
        models = []
        for _ in range(m):
            parts = input().split()
            models.append((parts[0], int(parts[1]), int(parts[2])))
        score, changes = fashion_show(n, m, models)
        print(f"Case #{case_num}: {score} {len(changes)}")
        for model, r, c in changes:
            print(f"{model} {r} {c}")

if __name__ == "__main__":
    main()
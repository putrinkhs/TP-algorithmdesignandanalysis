def is_safe(board, row, col, n):
    # Cek baris pada sisi kiri
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Cek diagonal atas kiri
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Cek diagonal bawah kiri
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        # Semua ratu sudah ditempatkan
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            # Tempatkan ratu dan lanjutkan ke kolom berikutnya
            board[i][col] = 1

            # Rekursif untuk menempatkan ratu pada kolom berikutnya
            if solve_n_queens_util(board, col + 1, n):
                return True

            # Jika tidak ada solusi, backtrack
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Maaf, tidak ada solusi yang mungkin.")
        return

    # Tampilkan solusi
    for row in board:
        print(row)

# Contoh pemanggilan fungsi
solve_n_queens(9)

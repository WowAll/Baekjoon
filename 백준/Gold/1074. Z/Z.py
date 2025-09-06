def z(r, c, N):
    if N == 0:
        return 0
    half = 2 ** (N - 1)
    if r >= half and c >= half:
        return 3 * (4 ** (N - 1)) + z(r - half, c - half, N - 1)
    elif r < half and c >= half:
        return (4 ** (N - 1)) + z(r, c - half, N - 1)
    elif r >= half and c < half:
        return 2 * (4 ** (N - 1)) + z(r - half, c, N - 1)
    else:
        return z(r, c, N - 1)


N, r, c = map(int, input().split())

print(z(r, c, N))
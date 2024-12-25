A = "A"
N = None
# lesson5 複数音 で追加
B = "B"
#

music_a = {
    # lesson5 複数音 で変更
    "score": [
        A, N, B, N, A, N, N, N,
        A, N, A, B, N, N, N, N,
        A, N, B, N, A, N, N, N,
        A, N, A, B, N, N, N, N,
    ],
    #
    # lesson4 音楽の再生 で変更
    "fps": 60000 / 121 / 5,
    "bpm": 121,
    #
    "title": "sample A",
    # lesson4 音楽の再生 で追加
    "music": 'sounds/MusMus-CT-NV-TT.mp3',
    #
    # lesson4 音楽の再生 で追加
    "delay": 1630,
    #
    # lessson4 画面の作成 で追加 ※ スコア表示時短のため変更75000→15000
    "time": 5000,
    #
}

music_b = {
    "score": [],
    "fps": 125,
    "bpm": 96,
    "title": "sample B",
}

music_list = [
    music_a,
    music_b,
]